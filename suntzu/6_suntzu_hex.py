import math
import random
from pathlib import Path
import pygame
from dataclasses import dataclass
from typing import Callable

WIDTH, HEIGHT = 1200, 800
FPS = 60
HEX_SIZE = 32
MAP_COLS = 17
MAP_ROWS = 12
UNIT_IMAGE_SIZE = 42

ASSET_ROOT = Path("assets")
UNIT_ASSET_ROOT = ASSET_ROOT / "units"

BG = (28, 26, 22)
PANEL = (38, 35, 30)
GRID = (95, 85, 65)
TEXT = (235, 225, 205)
MUTED = (170, 160, 140)
SELECT = (255, 230, 120)

BLUE = (70, 130, 220)
RED = (190, 70, 60)
BROWN = (145, 95, 55)
HIDDEN = (65, 55, 50)

PLAIN = (92, 116, 62)
ROUGH = (88, 80, 62)
PREPARED = (125, 105, 58)
SUPPLY = (75, 110, 135)
DEPLOY = (65, 95, 125)
HEIGHTS = (115, 92, 63)
FROZEN = (112, 132, 140)
VILLAGE = (120, 85, 70)
BEACH = (185, 160, 105)
SEA = (55, 85, 120)
BOCAGE = (60, 95, 55)
BUNKER = (95, 95, 95)
DROPZONE = (90, 110, 80)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sun Tzu Hex Tactics")
clock = pygame.time.Clock()
font = pygame.font.SysFont("consolas", 18)
small_font = pygame.font.SysFont("consolas", 15)
big_font = pygame.font.SysFont("consolas", 28)

DIRECTIONS = [(1, 0), (1, -1), (0, -1), (-1, 0), (-1, 1), (0, 1)]
UNIT_IMAGES = {}


@dataclass
class Tile:
    q: int
    r: int
    terrain: str = "plain"
    revealed: bool = False


@dataclass
class Unit:
    name: str
    side: str
    q: int
    r: int
    hp: int
    atk: int
    move: int
    range: int
    role: str
    hidden: bool = False
    acted: bool = False

    @property
    def pos(self):
        return self.q, self.r


@dataclass
class Scenario:
    key: str
    principle: str
    title: str
    subtitle: str
    description: str
    player_side: str
    enemy_side: str
    setup_func: Callable


tiles = {}
units = []
scenarios = []

selected = None
current_scenario = None

screen_mode = "SCENARIO_SELECT"
turn = ""
phase = ""
message = ""
assessment_points = 3
deployment_points = 6
player_morale = 100
enemy_morale = 100
logistics = 100
turn_number = 0


def draw_text(text, x, y, color=TEXT, f=font, center=False, center_x=None):
    img = f.render(str(text), True, color)
    rect = img.get_rect()

    if center and center_x is not None:
        rect.centerx = center_x
        rect.y = y
        screen.blit(img, rect)
    else:
        screen.blit(img, (x, y))


def wrap_text(text, width):
    words = str(text).split()
    lines = []
    line = ""

    for word in words:
        if len(line) + len(word) + 1 > width:
            if line:
                lines.append(line)
            line = word
        else:
            line += (" " if line else "") + word

    if line:
        lines.append(line)

    return lines


def draw_wrapped_text(
    text,
    x,
    y,
    width_chars,
    color=TEXT,
    f=font,
    line_height=21,
    max_lines=None,
    center=False,
    center_x=None,
):
    lines = wrap_text(text, width_chars)

    if max_lines is not None:
        lines = lines[:max_lines]

    for line in lines:
        draw_text(line, x, y, color, f, center=center, center_x=center_x)
        y += line_height

    return y


def candidate_filenames_for_role(role):
    files = {
        "commander": ["commander.png", "hq.png", "leader.png"],
        "cavalry": ["cavalry.png", "horse.png"],
        "infantry": ["infantry.png", "soldier.png"],
        "elite infantry": ["infantry.png", "elite_infantry.png"],
        "phalanx": ["phalanx.png"],
        "skirmisher": ["skirmisher.png"],
        "guard": ["guard.png"],
        "artillery": ["artillery.png", "gun.png"],
        "chariot": ["chariot.png"],
        "elephant": ["elephant.png"],
        "paratrooper": [
            "paratrooper.png",
            "paratroopers.png",
            "airborne.png",
            "airborne_infantry.png",
        ],
        "armor": ["armor.png", "tank.png", "sherman.png"],
        "naval": ["naval.png", "ship.png", "battleship.png"],
        "bunker": ["bunker.png", "fortification.png"],
    }

    return files.get(role, [f"{role}.png"])


def load_first_existing_image(paths):
    for path in paths:
        if not path.exists():
            continue

        try:
            img = pygame.image.load(str(path)).convert_alpha()
            return pygame.transform.smoothscale(img, (UNIT_IMAGE_SIZE, UNIT_IMAGE_SIZE))
        except pygame.error:
            continue

    return None


def load_unit_images_for_scenario(scenario_key):
    UNIT_IMAGES.clear()

    roles = [
        "commander",
        "cavalry",
        "infantry",
        "elite infantry",
        "phalanx",
        "skirmisher",
        "guard",
        "artillery",
        "chariot",
        "elephant",
        "paratrooper",
        "armor",
        "naval",
        "bunker",
    ]

    for role in roles:
        filenames = candidate_filenames_for_role(role)
        paths = []

        for filename in filenames:
            paths.append(UNIT_ASSET_ROOT / scenario_key / filename)

        for filename in filenames:
            paths.append(UNIT_ASSET_ROOT / "common" / filename)

        UNIT_IMAGES[role] = load_first_existing_image(paths)


def axial_to_pixel(q, r):
    x = HEX_SIZE * math.sqrt(3) * (q + r / 2) + 90
    y = HEX_SIZE * 1.5 * r + 80
    return int(x), int(y)


def hex_corners(cx, cy):
    points = []
    for i in range(6):
        angle = math.radians(60 * i - 30)
        points.append((cx + HEX_SIZE * math.cos(angle), cy + HEX_SIZE * math.sin(angle)))
    return points


def hex_distance(a, b):
    aq, ar = a
    bq, br = b
    return int((abs(aq - bq) + abs(aq + ar - bq - br) + abs(ar - br)) / 2)


def neighbors(q, r):
    return [(q + dq, r + dr) for dq, dr in DIRECTIONS]


def pixel_to_axial(mx, my):
    best = None
    best_dist = 999999

    for q in range(MAP_COLS):
        for r in range(MAP_ROWS):
            cx, cy = axial_to_pixel(q, r)
            d = (mx - cx) ** 2 + (my - cy) ** 2

            if d < best_dist:
                best_dist = d
                best = (q, r)

    return best


def get_unit_at(pos):
    for u in units:
        if u.hp > 0 and u.pos == pos:
            return u
    return None


def friendly_units(side):
    return [u for u in units if u.side == side and u.hp > 0]


def player_units():
    return friendly_units(current_scenario.player_side)


def ai_units():
    return friendly_units(current_scenario.enemy_side)


def reset_actions(side):
    for u in units:
        if u.side == side and u.hp > 0:
            u.acted = False


def reveal_around(pos, radius=2):
    global message

    revealed_count = 0

    for tile_pos, tile in tiles.items():
        if hex_distance(pos, tile_pos) <= radius:
            tile.revealed = True

    for u in units:
        if u.hidden and hex_distance(pos, u.pos) <= radius:
            u.hidden = False
            revealed_count += 1

    if revealed_count:
        message = f"Scouting revealed {revealed_count} enemy formation(s)."
    else:
        message = "Scouting improved terrain knowledge, but found no hidden formations."


def all_enemy_visible():
    return all(not u.hidden for u in units if u.side == current_scenario.enemy_side and u.hp > 0)


def valid_deploy_preview(q, r):
    if current_scenario.key == "gaugamela":
        return q <= 4

    if current_scenario.key == "austerlitz":
        return q <= 5 and 3 <= r <= 9

    if current_scenario.key == "normaninv":
        return q <= 3 or (4 <= q <= 5 and r in [2, 8])

    return False


def valid_deploy_hex(pos):
    q, r = pos
    return pos in tiles and valid_deploy_preview(q, r) and not get_unit_at(pos)


def deploy_unit(unit, target):
    global deployment_points, message

    if deployment_points <= 0:
        message = "No deployment points left."
        return

    if unit.side != current_scenario.player_side:
        return

    if not valid_deploy_hex(target):
        message = "Invalid deployment hex."
        return

    unit.q, unit.r = target
    deployment_points -= 1
    message = f"{unit.name} redeployed. Deployment points left: {deployment_points}."


def move_unit(unit, target):
    global logistics, message

    if unit.acted:
        message = f"{unit.name} has already acted."
        return

    if target not in tiles:
        return

    if get_unit_at(target):
        message = "Tile occupied."
        return

    dist = hex_distance(unit.pos, target)

    if dist > unit.move:
        message = "Too far."
        return

    terrain = tiles[target].terrain
    extra_cost = 0

    if terrain == "rough" and unit.role in ["cavalry", "chariot", "elephant"]:
        extra_cost += 1

    if terrain == "frozen" and unit.role in ["artillery", "infantry", "guard"]:
        extra_cost += 1

    if terrain == "bocage" and unit.role in ["armor", "infantry", "artillery"]:
        extra_cost += 1

    if terrain == "beach" and unit.role in ["armor", "artillery"]:
        extra_cost += 1

    if terrain == "sea" and unit.role != "naval":
        message = "Only naval units can enter sea hexes."
        return

    if unit.role == "elephant" and terrain == "rough":
        extra_cost += 1

    if dist + extra_cost > unit.move:
        message = "Terrain slows that unit."
        return

    unit.q, unit.r = target
    unit.acted = True
    logistics -= 2
    message = f"{unit.name} moved."


def attack_unit(attacker, defender):
    global player_morale, enemy_morale, message

    if attacker.acted:
        message = f"{attacker.name} has already acted."
        return

    if defender.hidden:
        message = "Cannot attack unrevealed enemy."
        return

    if hex_distance(attacker.pos, defender.pos) > attacker.range:
        message = "Target out of range."
        return

    terrain_bonus = 0
    bonus = 0

    defender_tile = tiles[defender.pos]

    if defender_tile.terrain in ["rough", "heights", "village", "bocage", "bunker"]:
        terrain_bonus += 1

    if attacker.role == "chariot" and defender.role == "phalanx":
        terrain_bonus += 2

    if attacker.role == "elephant" and defender.role == "cavalry":
        bonus += 2

    if attacker.role == "skirmisher" and defender.role == "elephant":
        bonus += 3

    if attacker.role == "phalanx" and defender.role == "elephant":
        bonus += 1

    if current_scenario.key == "austerlitz":
        if attacker.side == current_scenario.player_side and defender_tile.terrain == "heights":
            bonus += 1

        if attacker.role == "guard" and defender.role in ["infantry", "commander"]:
            bonus += 1

    if current_scenario.key == "normaninv":
        if attacker.role == "naval" and defender_tile.terrain in ["bunker", "beach"]:
            bonus += 2

        if attacker.role == "paratrooper" and defender.role in ["artillery", "bunker"]:
            bonus += 2

        if attacker.role == "armor" and defender_tile.terrain == "bocage":
            terrain_bonus += 1

        if attacker.role == "infantry" and defender_tile.terrain == "bunker":
            terrain_bonus += 1

    damage = max(1, attacker.atk + bonus + random.randint(-1, 2) - terrain_bonus)

    if all_enemy_visible() and attacker.side == current_scenario.player_side:
        damage += 1

    defender.hp -= damage
    attacker.acted = True

    if defender.hp <= 0:
        defender.hp = 0

        if defender.side == current_scenario.enemy_side:
            enemy_morale -= 15
        else:
            player_morale -= 15

        message = f"{attacker.name} destroyed {defender.name}!"
    else:
        message = f"{attacker.name} hit {defender.name} for {damage}."


def estimate_ai_intent():
    hints = []

    if current_scenario.key == "gaugamela":
        if any(u.role == "chariot" and u.hp > 0 for u in ai_units()):
            hints.append("Chariots favor prepared plain. Pull them into poor ground or screen them.")

        if any(u.role == "elephant" and u.hp > 0 for u in ai_units()):
            hints.append("Elephants are slow shock units. Avoid cavalry contact; use skirmishers or phalanx.")

        if any(u.role == "cavalry" and u.hp > 0 for u in ai_units()):
            hints.append("Persian cavalry will pressure your wings.")

        darius = next((u for u in units if u.name == "Darius" and u.hp > 0), None)
        if darius and not darius.hidden:
            hints.append("Darius is visible. A center strike can collapse Persian morale.")

    elif current_scenario.key == "austerlitz":
        hints.append("The Coalition wants your right flank.")
        hints.append("Let them overextend, then strike the Pratzen Heights.")
        hints.append("Keep the Imperial Guard as a decisive reserve.")

    elif current_scenario.key == "normaninv":
        hints.append("German bunkers guard the beach exits.")
        hints.append("Use naval fire and airborne disruption before pushing armor inland.")
        hints.append("Logistics matter: protect the beachhead and avoid slow bocage advances too early.")

    return " ".join(hints) if hints else "Enemy intent unclear."


def special_feint():
    global assessment_points, deployment_points, message

    if phase == "DEPLOY":
        if deployment_points <= 0:
            message = "No deployment points left."
            return
        deployment_points -= 1
    else:
        if assessment_points <= 0:
            message = "No assessment points left."
            return
        assessment_points -= 1

    if current_scenario.key == "gaugamela":
        alex = next((u for u in units if u.name == "Alexander" and u.hp > 0), None)
        cav = next((u for u in units if u.name == "Companion Cav" and u.hp > 0), None)

        for u in [alex, cav]:
            if u:
                target = (min(MAP_COLS - 1, u.q + 1), max(0, u.r - 1))
                if target in tiles and not get_unit_at(target):
                    u.q, u.r = target

        for p in ai_units():
            if p.role == "cavalry" and random.random() < 0.65:
                p.r = max(0, p.r - 1)
                p.hidden = False

        message = "Feint right executed. Persian cavalry shifts outward. Look for a center gap."

    elif current_scenario.key == "austerlitz":
        for enemy in ai_units():
            if enemy.role in ["infantry", "cavalry"] and random.random() < 0.7:
                enemy.q = max(0, enemy.q - 1)
                enemy.r = min(MAP_ROWS - 1, enemy.r + 1)
                enemy.hidden = False

        message = "False weakness shown on the right. Coalition forces overextend."

    elif current_scenario.key == "normaninv":
        for enemy in ai_units():
            if enemy.role in ["infantry", "armor"] and random.random() < 0.65:
                enemy.hidden = False
                enemy.q = min(MAP_COLS - 1, enemy.q + 1)

        message = "Deception and resistance reports confuse German reserves. Some enemy units reveal or delay."


def ai_turn():
    global turn, phase, message, logistics, turn_number, assessment_points

    enemies = ai_units()
    players = player_units()

    for e in enemies:
        if e.hidden:
            if any(hex_distance(e.pos, p.pos) <= 2 for p in players):
                e.hidden = False

        if e.hp <= 0:
            continue

        targets = [p for p in players if p.hp > 0]

        if not targets:
            break

        if current_scenario.key == "gaugamela" and e.role == "elephant":
            cavalry_targets = [p for p in targets if p.role == "cavalry"]
            target = min(cavalry_targets or targets, key=lambda p: hex_distance(e.pos, p.pos))

        elif current_scenario.key == "austerlitz" and e.role in ["infantry", "cavalry"]:
            right_flank = [p for p in targets if p.r >= 7]
            target = min(right_flank or targets, key=lambda p: hex_distance(e.pos, p.pos))

        elif current_scenario.key == "normaninv":
            beach_targets = [p for p in targets if tiles[p.pos].terrain in ["beach", "supply"]]
            target = min(beach_targets or targets, key=lambda p: hex_distance(e.pos, p.pos))

        else:
            target = min(targets, key=lambda p: hex_distance(e.pos, p.pos))

        if hex_distance(e.pos, target.pos) <= e.range and not e.acted:
            attack_unit(e, target)
            continue

        candidates = [c for c in neighbors(e.q, e.r) if c in tiles and not get_unit_at(c)]

        if not candidates:
            continue

        if e.role == "chariot":
            candidates.sort(key=lambda c: (
                hex_distance(c, target.pos),
                0 if tiles[c].terrain == "prepared" else 1,
            ))

        elif e.role == "elephant":
            candidates.sort(key=lambda c: (
                10 if tiles[c].terrain == "rough" else 0,
                hex_distance(c, target.pos),
            ))

        elif e.role == "cavalry":
            candidates.sort(key=lambda c: (
                hex_distance(c, target.pos),
                -abs(c[1] - 5),
            ))

        elif e.role == "commander":
            player_commander = next((p for p in players if p.role == "commander"), None)
            if player_commander:
                candidates.sort(key=lambda c: -hex_distance(c, player_commander.pos))
            else:
                candidates.sort(key=lambda c: hex_distance(c, target.pos))

        elif current_scenario.key == "normaninv" and e.role == "armor":
            candidates.sort(key=lambda c: (
                10 if tiles[c].terrain == "bocage" else 0,
                hex_distance(c, target.pos),
            ))

        else:
            candidates.sort(key=lambda c: hex_distance(c, target.pos))

        e.q, e.r = candidates[0]
        e.acted = True

    reset_actions(current_scenario.enemy_side)
    reset_actions(current_scenario.player_side)

    turn = current_scenario.player_side
    phase = "ASSESS"
    assessment_points = 3
    logistics -= 4
    turn_number += 1
    message = "New turn. Assess before committing."


def begin_battle():
    global phase, turn_number, assessment_points, message

    phase = "ASSESS"
    turn_number = 1
    assessment_points = 3
    message = "Battle begins. Assess the field, then commit your attack."


def end_player_turn():
    global turn, phase, message

    if phase == "DEPLOY":
        message = "Press B to begin battle after deployment."
        return

    turn = current_scenario.enemy_side
    phase = "AI"
    message = "Enemy AI is moving..."
    pygame.time.set_timer(pygame.USEREVENT, 500)


def check_victory():
    commanders = [u for u in units if u.role == "commander"]

    player_commander = next((u for u in commanders if u.side == current_scenario.player_side), None)
    enemy_commander = next((u for u in commanders if u.side == current_scenario.enemy_side), None)

    if player_commander is None or player_commander.hp <= 0:
        return f"{current_scenario.enemy_side} wins. Your commander has fallen."

    if enemy_commander is None or enemy_commander.hp <= 0:
        return f"{current_scenario.player_side} wins. Enemy commander is routed."

    if enemy_morale <= 0:
        return f"{current_scenario.player_side} wins. Enemy morale collapses."

    if player_morale <= 0:
        return f"{current_scenario.enemy_side} wins. Your morale collapses."

    if logistics <= 0:
        return f"{current_scenario.enemy_side} wins. Your logistics are exhausted."

    return None


def make_base_tiles():
    global tiles

    tiles = {}

    for q in range(MAP_COLS):
        for r in range(MAP_ROWS):
            tiles[(q, r)] = Tile(q, r, "plain")


def setup_gaugamela():
    global units, turn, phase, message, assessment_points, deployment_points
    global player_morale, enemy_morale, logistics, turn_number, selected

    make_base_tiles()

    for pos, tile in tiles.items():
        q, r = pos

        if 8 <= q <= 13 and 3 <= r <= 8:
            tile.terrain = "prepared"

        if q >= 12 and r <= 3:
            tile.terrain = "rough"

        if q <= 2 and 4 <= r <= 7:
            tile.terrain = "supply"

        if q <= 6:
            tile.revealed = True

    units = [
        Unit("Alexander", "Macedon", 2, 5, 12, 5, 3, 1, "commander"),
        Unit("Companion Cav", "Macedon", 2, 4, 10, 4, 4, 1, "cavalry"),
        Unit("Hypaspists", "Macedon", 3, 5, 11, 4, 2, 1, "elite infantry"),
        Unit("Phalanx I", "Macedon", 2, 6, 13, 3, 1, 1, "phalanx"),
        Unit("Phalanx II", "Macedon", 3, 6, 13, 3, 1, 1, "phalanx"),
        Unit("Agrianians", "Macedon", 3, 4, 8, 3, 2, 2, "skirmisher"),
        Unit("Darius", "Persia", 14, 5, 10, 2, 2, 1, "commander", hidden=True),
        Unit("Persian Center", "Persia", 13, 5, 14, 3, 1, 1, "infantry", hidden=True),
        Unit("Scythed Chariots", "Persia", 11, 5, 8, 6, 4, 1, "chariot", hidden=True),
        Unit("Indian Elephants", "Persia", 12, 6, 16, 5, 2, 1, "elephant", hidden=True),
        Unit("Bactrian Cav", "Persia", 13, 3, 10, 4, 4, 1, "cavalry", hidden=True),
        Unit("Mazaeus Cav", "Persia", 13, 7, 10, 4, 4, 1, "cavalry", hidden=True),
        Unit("Persian Guard", "Persia", 14, 6, 12, 4, 1, 1, "guard", hidden=True),
    ]

    selected = None
    turn = "Macedon"
    phase = "DEPLOY"
    message = "Gaugamela deployment. Scout, redeploy, feint right, then press B."
    assessment_points = 3
    deployment_points = 6
    player_morale = 100
    enemy_morale = 100
    logistics = 100
    turn_number = 0


def setup_austerlitz():
    global units, turn, phase, message, assessment_points, deployment_points
    global player_morale, enemy_morale, logistics, turn_number, selected

    make_base_tiles()

    for pos, tile in tiles.items():
        q, r = pos

        if 7 <= q <= 11 and 3 <= r <= 6:
            tile.terrain = "heights"

        if q >= 10 and r >= 7:
            tile.terrain = "frozen"

        if 5 <= q <= 6 and 5 <= r <= 7:
            tile.terrain = "village"

        if q <= 2 and 4 <= r <= 8:
            tile.terrain = "supply"

        if q <= 6:
            tile.revealed = True

    units = [
        Unit("Napoleon", "France", 2, 6, 12, 4, 3, 1, "commander"),
        Unit("Soult IV Corps", "France", 3, 5, 12, 4, 2, 1, "infantry"),
        Unit("Vandamme Div", "France", 3, 6, 11, 4, 2, 1, "infantry"),
        Unit("Legrand Right", "France", 4, 8, 10, 3, 2, 1, "infantry"),
        Unit("Murat Cavalry", "France", 2, 4, 10, 4, 4, 1, "cavalry"),
        Unit("Imperial Guard", "France", 2, 7, 13, 5, 2, 1, "guard"),
        Unit("French Artillery", "France", 3, 7, 8, 3, 1, 3, "artillery"),
        Unit("Tsar Alexander", "Coalition", 14, 4, 10, 2, 2, 1, "commander", hidden=True),
        Unit("Pratzen Center", "Coalition", 10, 5, 13, 3, 1, 1, "infantry", hidden=True),
        Unit("Bagration Wing", "Coalition", 13, 3, 10, 4, 3, 1, "cavalry", hidden=True),
        Unit("Allied Left Column", "Coalition", 12, 8, 13, 3, 2, 1, "infantry", hidden=True),
        Unit("Allied Right Column", "Coalition", 12, 2, 11, 3, 2, 1, "infantry", hidden=True),
        Unit("Russian Guard", "Coalition", 14, 5, 13, 5, 2, 1, "guard", hidden=True),
        Unit("Coalition Artillery", "Coalition", 13, 6, 8, 3, 1, 3, "artillery", hidden=True),
    ]

    selected = None
    turn = "France"
    phase = "DEPLOY"
    message = "Austerlitz deployment. Look weak, lure the enemy, then strike the Pratzen Heights."
    assessment_points = 3
    deployment_points = 6
    player_morale = 100
    enemy_morale = 100
    logistics = 100
    turn_number = 0


def setup_normaninv():
    global units, turn, phase, message, assessment_points, deployment_points
    global player_morale, enemy_morale, logistics, turn_number, selected

    make_base_tiles()

    for pos, tile in tiles.items():
        q, r = pos

        if q <= 1:
            tile.terrain = "sea"
        elif 2 <= q <= 4:
            tile.terrain = "beach"
        elif 5 <= q <= 6 and 3 <= r <= 8:
            tile.terrain = "supply"
        elif 7 <= q <= 11 and 2 <= r <= 9:
            tile.terrain = "bocage"
        elif q >= 12 and r in [3, 6, 8]:
            tile.terrain = "bunker"
        elif q >= 10 and r <= 2:
            tile.terrain = "village"
        elif q >= 10 and r >= 9:
            tile.terrain = "rough"

        if q <= 5:
            tile.revealed = True

    units = [
        Unit("Eisenhower HQ", "Allies", 1, 5, 12, 3, 2, 1, "commander"),
        Unit("Omaha Infantry", "Allies", 2, 5, 12, 4, 2, 1, "infantry"),
        Unit("Utah Infantry", "Allies", 2, 7, 12, 4, 2, 1, "infantry"),
        Unit("Rangers", "Allies", 3, 4, 10, 5, 2, 1, "infantry"),
        Unit("Airborne North", "Allies", 5, 2, 9, 4, 3, 1, "paratrooper"),
        Unit("Airborne South", "Allies", 5, 8, 9, 4, 3, 1, "paratrooper"),
        Unit("Sherman Armor", "Allies", 2, 6, 13, 5, 3, 1, "armor"),
        Unit("Naval Fire Support", "Allies", 1, 6, 10, 5, 1, 4, "naval"),
        Unit("Beach Engineers", "Allies", 3, 6, 8, 3, 2, 1, "infantry"),
        Unit("German Command", "Germany", 14, 5, 10, 2, 2, 1, "commander", hidden=True),
        Unit("Atlantic Wall Bunker", "Germany", 12, 5, 14, 4, 0, 3, "bunker", hidden=True),
        Unit("Coastal Artillery", "Germany", 13, 6, 9, 4, 1, 3, "artillery", hidden=True),
        Unit("Beach Defenders", "Germany", 10, 5, 11, 3, 1, 1, "infantry", hidden=True),
        Unit("Panzer Reserve", "Germany", 14, 8, 13, 5, 3, 1, "armor", hidden=True),
        Unit("Bocage Infantry", "Germany", 11, 8, 11, 3, 1, 1, "infantry", hidden=True),
        Unit("Village Strongpoint", "Germany", 11, 2, 10, 3, 1, 2, "bunker", hidden=True),
    ]

    selected = None
    turn = "Allies"
    phase = "DEPLOY"
    message = "Normandy deployment. Scout defenses, coordinate airborne drops, naval fire, and beach logistics."
    assessment_points = 3
    deployment_points = 8
    player_morale = 100
    enemy_morale = 100
    logistics = 125
    turn_number = 0


scenarios = [
    Scenario(
        key="gaugamela",
        principle="Principle 1: Strategic Assessment",
        title="Gaugamela, 331 BC",
        subtitle="Alexander vs. Darius",
        description="Scout prepared ground, read Persian cavalry, avoid chariots and elephants, then strike Darius.",
        player_side="Macedon",
        enemy_side="Persia",
        setup_func=setup_gaugamela,
    ),
    Scenario(
        key="austerlitz",
        principle="Principle 1: Strategic Assessment",
        title="Austerlitz, 1805",
        subtitle="Napoleon vs. Third Coalition",
        description="Appear weak on the right, lure the Coalition off the heights, then smash the exposed center.",
        player_side="France",
        enemy_side="Coalition",
        setup_func=setup_austerlitz,
    ),
    Scenario(
        key="normaninv",
        principle="Principle 1: Strategic Assessment",
        title="Normandy Invasion, 1944",
        subtitle="Allied landings vs. German coastal defense",
        description="Massive intelligence and logistical planning: scout beach defenses, coordinate airborne drops, naval fire, armor, and supply.",
        player_side="Allies",
        enemy_side="Germany",
        setup_func=setup_normaninv,
    ),
]


def start_scenario(index):
    global current_scenario, screen_mode

    current_scenario = scenarios[index]
    load_unit_images_for_scenario(current_scenario.key)
    current_scenario.setup_func()
    screen_mode = "GAME"


def draw_scenario_select():
    screen.fill(BG)

    center_x = WIDTH // 2
    draw_text("SUN TZU HEX TACTICS", 0, 45, TEXT, big_font, center=True, center_x=center_x)
    draw_text("Select a scenario by principle", 0, 84, MUTED, font, center=True, center_x=center_x)

    card_w = 820
    card_h = 135
    x = (WIDTH - card_w) // 2
    start_y = 150
    gap = 155

    for i, scenario in enumerate(scenarios):
        y = start_y + i * gap
        card_center = x + card_w // 2

        pygame.draw.rect(screen, PANEL, (x, y, card_w, card_h), border_radius=12)
        pygame.draw.rect(screen, GRID, (x, y, card_w, card_h), 2, border_radius=12)

        draw_text(f"{i + 1}. {scenario.principle}", 0, y + 15, SELECT, small_font, center=True, center_x=card_center)
        draw_text(scenario.title, 0, y + 40, TEXT, big_font, center=True, center_x=card_center)
        draw_text(scenario.subtitle, 0, y + 75, MUTED, small_font, center=True, center_x=card_center)

        draw_wrapped_text(
            scenario.description,
            x + 25,
            y + 99,
            80,
            TEXT,
            small_font,
            18,
            max_lines=2,
            center=True,
            center_x=card_center,
        )

    draw_text("Press 1-9 or click a scenario card.", 0, 705, TEXT, font, center=True, center_x=center_x)


def tile_color(tile):
    if phase == "DEPLOY" and valid_deploy_preview(tile.q, tile.r):
        return DEPLOY

    if not tile.revealed and tile.q > 6:
        return HIDDEN

    colors = {
        "plain": PLAIN,
        "rough": ROUGH,
        "prepared": PREPARED,
        "supply": SUPPLY,
        "heights": HEIGHTS,
        "frozen": FROZEN,
        "village": VILLAGE,
        "beach": BEACH,
        "sea": SEA,
        "bocage": BOCAGE,
        "bunker": BUNKER,
        "dropzone": DROPZONE,
    }

    return colors.get(tile.terrain, PLAIN)


def draw_map():
    for pos, tile in tiles.items():
        cx, cy = axial_to_pixel(tile.q, tile.r)

        pygame.draw.polygon(screen, tile_color(tile), hex_corners(cx, cy))
        pygame.draw.polygon(screen, GRID, hex_corners(cx, cy), 2)

        if selected and selected.pos == pos:
            pygame.draw.polygon(screen, SELECT, hex_corners(cx, cy), 4)


def tint_image(img, color):
    tinted = img.copy()
    tint = pygame.Surface(tinted.get_size(), pygame.SRCALPHA)
    tint.fill((*color, 90))
    tinted.blit(tint, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
    return tinted


def draw_fallback_unit_icon(u, cx, cy):
    if u.role == "elephant":
        color = BROWN
    elif u.side == current_scenario.player_side:
        color = BLUE
    else:
        color = RED

    pygame.draw.circle(screen, color, (cx, cy), 19)
    pygame.draw.circle(screen, (20, 20, 20), (cx, cy), 19, 2)

    label = {
        "commander": "CM",
        "cavalry": "CV",
        "infantry": "IN",
        "elite infantry": "EI",
        "phalanx": "PH",
        "skirmisher": "SK",
        "guard": "GD",
        "artillery": "AR",
        "chariot": "CH",
        "elephant": "EL",
        "paratrooper": "PT",
        "armor": "TK",
        "naval": "NV",
        "bunker": "BK",
    }.get(u.role, u.name[:2].upper())

    draw_text(label, 0, cy - 9, (255, 255, 255), small_font, center=True, center_x=cx)


def draw_units():
    for u in units:
        if u.hp <= 0 or u.hidden:
            continue

        cx, cy = axial_to_pixel(u.q, u.r)
        img = UNIT_IMAGES.get(u.role)

        if img:
            border_color = BLUE if u.side == current_scenario.player_side else RED

            if u.role == "elephant":
                border_color = BROWN

            pygame.draw.circle(screen, border_color, (cx, cy), 23)
            pygame.draw.circle(screen, (20, 20, 20), (cx, cy), 23, 2)

            final_img = tint_image(img, border_color)
            rect = final_img.get_rect(center=(cx, cy))
            screen.blit(final_img, rect)
        else:
            draw_fallback_unit_icon(u, cx, cy)

        draw_text(str(u.hp), 0, cy + 21, TEXT, small_font, center=True, center_x=cx)


def draw_sidebar():
    x = 750
    w = 430
    center_x = x + w // 2

    pygame.draw.rect(screen, PANEL, (740, 0, 460, HEIGHT))

    draw_text("SUN TZU HEX TACTICS", 0, 18, TEXT, big_font, center=True, center_x=center_x)

    y = 54
    y = draw_wrapped_text(current_scenario.principle, x, y, 38, SELECT, small_font, 18, max_lines=2, center=True, center_x=center_x)
    y = draw_wrapped_text(current_scenario.title, x, y + 3, 38, TEXT, font, 21, max_lines=2, center=True, center_x=center_x)

    y += 10
    draw_text(f"Turn: {turn_number if turn_number else 'Pre-Battle'}", 0, y, TEXT, font, center=True, center_x=center_x)
    y += 23
    draw_text(f"Phase: {phase}", 0, y, TEXT, font, center=True, center_x=center_x)
    y += 30

    if phase == "DEPLOY":
        draw_text(f"Deployment Points: {deployment_points}", 0, y, TEXT, font, center=True, center_x=center_x)
        y += 25
    else:
        draw_text(f"Assessment Points: {assessment_points}", 0, y, TEXT, font, center=True, center_x=center_x)
        y += 22
        draw_text(f"{current_scenario.player_side} Morale: {player_morale}", 0, y, TEXT, font, center=True, center_x=center_x)
        y += 22
        draw_text(f"{current_scenario.enemy_side} Morale: {enemy_morale}", 0, y, TEXT, font, center=True, center_x=center_x)
        y += 22
        draw_text(f"Logistics: {logistics}", 0, y, TEXT, font, center=True, center_x=center_x)
        y += 25

    draw_text("Controls", 0, y, TEXT, big_font, center=True, center_x=center_x)
    y += 38

    if phase == "DEPLOY":
        controls = [
            "Click player unit: select",
            "Click blue hex: redeploy",
            "S: scout selected unit area",
            "I: estimate enemy intent",
            "F: scenario feint/deception",
            "B: begin battle",
            "M: scenario menu",
        ]
    else:
        controls = [
            "Click unit: select",
            "Click empty hex: move",
            "Click enemy: attack",
            "S: scout selected unit area",
            "I: estimate enemy intent",
            "F: scenario feint/deception",
            "E: end turn",
            "M: scenario menu",
        ]

    for item in controls:
        y = draw_wrapped_text(item, x, y, 39, TEXT, small_font, 18, max_lines=2, center=True, center_x=center_x)

    y += 12
    draw_text("Selected", 0, y, TEXT, big_font, center=True, center_x=center_x)
    y += 38

    if selected:
        selected_lines = [
            selected.name,
            f"Role: {selected.role}",
            f"HP: {selected.hp}",
            f"ATK: {selected.atk}",
            f"MOVE: {selected.move}",
            f"RANGE: {selected.range}",
        ]

        for item in selected_lines:
            y = draw_wrapped_text(item, x, y, 39, TEXT, small_font, 18, max_lines=2, center=True, center_x=center_x)
    else:
        draw_text("None", 0, y, TEXT, small_font, center=True, center_x=center_x)
        y += 22

    report_y = 688
    pygame.draw.rect(screen, (30, 28, 24), (750, report_y - 8, 430, 98), border_radius=8)
    pygame.draw.rect(screen, GRID, (750, report_y - 8, 430, 98), 1, border_radius=8)

    draw_text("Report", 0, report_y, TEXT, font, center=True, center_x=center_x)
    draw_wrapped_text(message, x, report_y + 26, 41, TEXT, small_font, 18, max_lines=3, center=True, center_x=center_x)


def draw_legend():
    pygame.draw.rect(screen, (25, 24, 21), (25, 732, 1080, 42), border_radius=8)
    draw_wrapped_text(
        "Terrain: green=plain, tan=prepared, gray=rough, blue=supply/deploy, brown=heights, icy=frozen, red=village, sand=beach, dark blue=sea, dark green=bocage, gray=bunker",
        35,
        739,
        125,
        TEXT,
        small_font,
        18,
        max_lines=2,
        center=True,
        center_x=565,
    )


def draw_game():
    screen.fill(BG)
    draw_map()
    draw_units()
    draw_sidebar()
    draw_legend()


def handle_game_key(event):
    global screen_mode, selected, message, assessment_points, deployment_points

    if event.key == pygame.K_m:
        screen_mode = "SCENARIO_SELECT"
        selected = None
        return

    if event.key == pygame.K_b and phase == "DEPLOY":
        begin_battle()
        return

    if event.key == pygame.K_e and turn == current_scenario.player_side:
        end_player_turn()
        return

    if event.key == pygame.K_s and selected and turn == current_scenario.player_side:
        if phase == "DEPLOY":
            if deployment_points > 0:
                reveal_around(selected.pos, radius=3)
                deployment_points -= 1
            else:
                message = "No deployment points left."
        else:
            if assessment_points > 0:
                reveal_around(selected.pos, radius=2)
                assessment_points -= 1
            else:
                message = "No assessment points left."
        return

    if event.key == pygame.K_i and turn == current_scenario.player_side:
        if phase == "DEPLOY":
            if deployment_points > 0:
                message = estimate_ai_intent()
                deployment_points -= 1
            else:
                message = "No deployment points left."
        else:
            if assessment_points > 0:
                message = estimate_ai_intent()
                assessment_points -= 1
            else:
                message = "No assessment points left."
        return

    if event.key == pygame.K_f and turn == current_scenario.player_side:
        special_feint()


def handle_game_click(mx, my):
    global selected, message

    if mx >= 730 or turn != current_scenario.player_side:
        return

    clicked = pixel_to_axial(mx, my)
    clicked_unit = get_unit_at(clicked)

    if clicked_unit and clicked_unit.side == current_scenario.player_side:
        selected = clicked_unit
        message = f"Selected {selected.name}."
        return

    if selected and phase == "DEPLOY" and not clicked_unit:
        deploy_unit(selected, clicked)
        return

    if selected and phase != "DEPLOY" and clicked_unit and clicked_unit.side != selected.side:
        attack_unit(selected, clicked_unit)
        return

    if selected and phase != "DEPLOY" and not clicked_unit:
        move_unit(selected, clicked)


def handle_scenario_click(mx, my):
    card_w = 820
    card_h = 135
    x = (WIDTH - card_w) // 2
    start_y = 150
    gap = 155

    for i in range(len(scenarios)):
        y = start_y + i * gap

        if x <= mx <= x + card_w and y <= my <= y + card_h:
            start_scenario(i)
            return


def handle_scenario_key(event):
    if pygame.K_1 <= event.key <= pygame.K_9:
        idx = event.key - pygame.K_1

        if idx < len(scenarios):
            start_scenario(idx)


running = True
game_over = None

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if screen_mode == "SCENARIO_SELECT":
            if event.type == pygame.KEYDOWN:
                handle_scenario_key(event)

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                handle_scenario_click(*pygame.mouse.get_pos())

        elif screen_mode == "GAME":
            if event.type == pygame.USEREVENT:
                pygame.time.set_timer(pygame.USEREVENT, 0)
                ai_turn()

            if event.type == pygame.KEYDOWN and not game_over:
                handle_game_key(event)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
                handle_game_click(*pygame.mouse.get_pos())

    if screen_mode == "SCENARIO_SELECT":
        game_over = None
        draw_scenario_select()

    elif screen_mode == "GAME":
        game_over = check_victory()
        draw_game()

        if game_over:
            pygame.draw.rect(screen, (20, 20, 20), (210, 300, 760, 140))
            draw_wrapped_text(game_over, 245, 335, 60, TEXT, big_font, 32, max_lines=2, center=True, center_x=590)
            draw_text("Press M to return to scenario selection.", 0, 405, TEXT, font, center=True, center_x=590)

    pygame.display.flip()

pygame.quit()
