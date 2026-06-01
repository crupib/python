import math
import random
import pygame
from dataclasses import dataclass
from typing import Callable

WIDTH, HEIGHT = 1200, 800
FPS = 60
HEX_SIZE = 32
MAP_COLS = 17
MAP_ROWS = 12

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

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sun Tzu Hex Tactics")
clock = pygame.time.Clock()
font = pygame.font.SysFont("consolas", 18)
big_font = pygame.font.SysFont("consolas", 28)

DIRECTIONS = [(1, 0), (1, -1), (0, -1), (-1, 0), (-1, 1), (0, 1)]


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


def draw_text(text, x, y, color=TEXT, f=font):
    img = f.render(text, True, color)
    screen.blit(img, (x, y))


def wrap_text(text, width):
    words = text.split()
    lines = []
    line = ""

    for word in words:
        if len(line) + len(word) + 1 > width:
            lines.append(line)
            line = word
        else:
            line += (" " if line else "") + word

    if line:
        lines.append(line)

    return lines


def get_unit_at(pos):
    for u in units:
        if u.hp > 0 and u.pos == pos:
            return u
    return None


def friendly_units(side):
    return [u for u in units if u.side == side and u.hp > 0]


def enemy_units(side):
    return [u for u in units if u.side != side and u.hp > 0]


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


def valid_deploy_hex(pos):
    q, r = pos

    if current_scenario.key == "gaugamela":
        return pos in tiles and q <= 4 and not get_unit_at(pos)

    if current_scenario.key == "austerlitz":
        return pos in tiles and q <= 5 and 3 <= r <= 9 and not get_unit_at(pos)

    return False


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

    if unit.role == "elephant" and terrain == "rough":
        extra_cost += 1

    if terrain == "frozen" and unit.role in ["artillery", "infantry", "guard"]:
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

    if defender_tile.terrain in ["rough", "heights", "village"]:
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
            hints.append("Chariots favor prepared plain. Pull them into bad ground or screen them.")
        if any(u.role == "elephant" and u.hp > 0 for u in ai_units()):
            hints.append("Elephants are slow shock units. Avoid cavalry contact.")
        if any(u.role == "cavalry" and u.hp > 0 for u in ai_units()):
            hints.append("Persian cavalry will pressure your wings.")
        darius = next((u for u in units if u.name == "Darius" and u.hp > 0), None)
        if darius and not darius.hidden:
            hints.append("Darius is visible. A center strike can collapse enemy morale.")

    elif current_scenario.key == "austerlitz":
        hints.append("The Coalition wants your right flank. Let them overextend.")
        hints.append("Hold the center weakly, then strike the Pratzen Heights.")
        if any(u.role == "guard" and u.hp > 0 for u in player_units()):
            hints.append("The Imperial Guard is your decisive reserve. Do not waste it early.")

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

        message = "False weakness shown on the right. Coalition forces overextend toward your flank."


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
        else:
            target = min(targets, key=lambda p: hex_distance(e.pos, p.pos))

        if hex_distance(e.pos, target.pos) <= e.range and not e.acted:
            attack_unit(e, target)
            continue

        candidates = [c for c in neighbors(e.q, e.r) if c in tiles and not get_unit_at(c)]

        if not candidates:
            continue

        if e.role == "chariot":
            candidates.sort(key=lambda c: (hex_distance(c, target.pos), 0 if tiles[c].terrain == "prepared" else 1))
        elif e.role == "elephant":
            candidates.sort(key=lambda c: (10 if tiles[c].terrain == "rough" else 0, hex_distance(c, target.pos)))
        elif e.role == "cavalry":
            candidates.sort(key=lambda c: (hex_distance(c, target.pos), -abs(c[1] - 5)))
        elif e.role == "commander":
            main_threat = next((p for p in players if p.role == "commander"), None)
            if main_threat:
                candidates.sort(key=lambda c: -hex_distance(c, main_threat.pos))
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
]


def start_scenario(index):
    global current_scenario, screen_mode

    current_scenario = scenarios[index]
    current_scenario.setup_func()
    screen_mode = "GAME"


def draw_scenario_select():
    screen.fill(BG)

    draw_text("SUN TZU HEX TACTICS", 370, 60, TEXT, big_font)
    draw_text("Select a scenario by principle", 410, 100, MUTED)

    card_w = 820
    card_h = 150
    start_y = 180

    for i, scenario in enumerate(scenarios):
        x = 190
        y = start_y + i * 190

        pygame.draw.rect(screen, PANEL, (x, y, card_w, card_h), border_radius=12)
        pygame.draw.rect(screen, GRID, (x, y, card_w, card_h), 2, border_radius=12)

        draw_text(f"{i + 1}. {scenario.principle}", x + 25, y + 20, SELECT)
        draw_text(scenario.title, x + 25, y + 50, TEXT, big_font)
        draw_text(scenario.subtitle, x + 25, y + 85, MUTED)

        lines = wrap_text(scenario.description, 80)
        yy = y + 112
        for line in lines[:2]:
            draw_text(line, x + 25, yy, TEXT)
            yy += 22

    draw_text("Press 1-9 or click a scenario card.", 385, 700, TEXT)


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
    }

    return colors.get(tile.terrain, PLAIN)


def valid_deploy_preview(q, r):
    if current_scenario.key == "gaugamela":
        return q <= 4
    if current_scenario.key == "austerlitz":
        return q <= 5 and 3 <= r <= 9
    return False


def draw_map():
    for pos, tile in tiles.items():
        cx, cy = axial_to_pixel(tile.q, tile.r)
        pygame.draw.polygon(screen, tile_color(tile), hex_corners(cx, cy))
        pygame.draw.polygon(screen, GRID, hex_corners(cx, cy), 2)

        if selected and selected.pos == pos:
            pygame.draw.polygon(screen, SELECT, hex_corners(cx, cy), 4)


def draw_units():
    for u in units:
        if u.hp <= 0 or u.hidden:
            continue

        cx, cy = axial_to_pixel(u.q, u.r)

        if u.role == "elephant":
            color = BROWN
        elif u.side == current_scenario.player_side:
            color = BLUE
        else:
            color = RED

        pygame.draw.circle(screen, color, (cx, cy), 19)
        pygame.draw.circle(screen, (20, 20, 20), (cx, cy), 19, 2)

        label = "EL" if u.role == "elephant" else u.name[:2].upper()
        draw_text(label, cx - 12, cy - 9, (255, 255, 255))
        draw_text(str(u.hp), cx - 9, cy + 18, TEXT)


def draw_sidebar():
    x = 760
    pygame.draw.rect(screen, PANEL, (740, 0, 460, HEIGHT))

    draw_text("SUN TZU HEX TACTICS", x, 20, TEXT, big_font)
    draw_text(current_scenario.principle, x, 55, SELECT)
    draw_text(current_scenario.title, x, 82, TEXT)

    draw_text(f"Turn: {turn_number if turn_number else 'Pre-Battle'}", x, 120)
    draw_text(f"Phase: {phase}", x, 145)

    if phase == "DEPLOY":
        draw_text(f"Deployment Points: {deployment_points}", x, 175)
    else:
        draw_text(f"Assessment Points: {assessment_points}", x, 175)
        draw_text(f"{current_scenario.player_side} Morale: {player_morale}", x, 200)
        draw_text(f"{current_scenario.enemy_side} Morale: {enemy_morale}", x, 225)
        draw_text(f"Logistics: {logistics}", x, 250)

    draw_text("Controls", x, 290, TEXT, big_font)

    if phase == "DEPLOY":
        draw_text("Click player unit: select", x, 330)
        draw_text("Click blue hex: redeploy", x, 355)
        draw_text("S: scout selected unit area", x, 380)
        draw_text("I: estimate enemy intent", x, 405)
        draw_text("F: scenario feint/deception", x, 430)
        draw_text("B: begin battle", x, 455)
        draw_text("M: scenario menu", x, 480)
    else:
        draw_text("Click unit: select", x, 330)
        draw_text("Click empty hex: move", x, 355)
        draw_text("Click enemy: attack", x, 380)
        draw_text("S: scout selected unit area", x, 405)
        draw_text("I: estimate enemy intent", x, 430)
        draw_text("F: scenario feint/deception", x, 455)
        draw_text("E: end turn", x, 480)
        draw_text("M: scenario menu", x, 505)

    draw_text("Selected", x, 540, TEXT, big_font)

    if selected:
        draw_text(selected.name, x, 580)
        draw_text(f"Role: {selected.role}", x, 605)
        draw_text(f"HP: {selected.hp}", x, 630)
        draw_text(f"ATK: {selected.atk}", x, 655)
        draw_text(f"MOVE: {selected.move}", x, 680)
    else:
        draw_text("None", x, 580)

    wrapped = wrap_text(message, 42)
    yy = 715
    for line in wrapped[:3]:
        draw_text(line, x, yy)
        yy += 22


def draw_legend():
    draw_text("Terrain: green=plain, tan=prepared, gray=rough, blue=supply/deploy, brown=heights, icy=frozen, red=village", 30, 742)


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
    card_h = 150
    x = 190
    start_y = 180

    for i in range(len(scenarios)):
        y = start_y + i * 190
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
            draw_text(game_over, 245, 335, TEXT, big_font)
            draw_text("Press M to return to scenario selection.", 245, 385)

    pygame.display.flip()

pygame.quit()
