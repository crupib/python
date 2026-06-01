import math
import random
import pygame
from dataclasses import dataclass

# -----------------------------
# Config
# -----------------------------

WIDTH, HEIGHT = 1200, 800
FPS = 60

HEX_SIZE = 32
MAP_COLS = 17
MAP_ROWS = 12

BG = (28, 26, 22)
GRID = (95, 85, 65)
TEXT = (235, 225, 205)
SELECT = (255, 230, 120)

MACEDONIAN = (70, 130, 220)
PERSIAN = (190, 70, 60)
HIDDEN = (65, 55, 50)
TERRAIN_PLAIN = (92, 116, 62)
TERRAIN_ROUGH = (88, 80, 62)
TERRAIN_PREPARED = (125, 105, 58)
TERRAIN_SUPPLY = (75, 110, 135)
DEPLOY_ZONE = (65, 95, 125)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gaugamela: Strategic Assessment")
clock = pygame.time.Clock()
font = pygame.font.SysFont("consolas", 18)
big_font = pygame.font.SysFont("consolas", 28)

DIRECTIONS = [
    (1, 0), (1, -1), (0, -1),
    (-1, 0), (-1, 1), (0, 1)
]


def axial_to_pixel(q, r):
    x = HEX_SIZE * math.sqrt(3) * (q + r / 2) + 90
    y = HEX_SIZE * 1.5 * r + 80
    return int(x), int(y)


def hex_corners(cx, cy):
    points = []
    for i in range(6):
        angle = math.radians(60 * i - 30)
        x = cx + HEX_SIZE * math.cos(angle)
        y = cy + HEX_SIZE * math.sin(angle)
        points.append((x, y))
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
    morale: int = 100

    @property
    def pos(self):
        return self.q, self.r


tiles = {}

for q in range(MAP_COLS):
    for r in range(MAP_ROWS):
        terrain = "plain"

        if 8 <= q <= 13 and 3 <= r <= 8:
            terrain = "prepared"

        if q >= 12 and r <= 3:
            terrain = "rough"

        if q <= 2 and 4 <= r <= 7:
            terrain = "supply"

        tiles[(q, r)] = Tile(q, r, terrain)


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
    Unit("Bactrian Cav", "Persia", 13, 3, 10, 4, 4, 1, "cavalry", hidden=True),
    Unit("Mazaeus Cav", "Persia", 13, 7, 10, 4, 4, 1, "cavalry", hidden=True),
    Unit("Persian Guard", "Persia", 14, 6, 12, 4, 1, 1, "guard", hidden=True),
]

selected = None
turn = "Macedon"
phase = "DEPLOY"
message = "Pre-battle deployment. Spend assessment points, reposition units, then press B."
assessment_points = 3
deployment_points = 6
macedon_morale = 100
persia_morale = 100
logistics = 100
turn_number = 0


def get_unit_at(pos):
    for u in units:
        if u.hp > 0 and u.pos == pos:
            return u
    return None


def friendly_units(side):
    return [u for u in units if u.side == side and u.hp > 0]


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
        message = f"Scouting revealed {revealed_count} Persian formation(s)."
    else:
        message = "Scouting improved terrain knowledge, but found no hidden formations."


def all_persians_visible():
    return all(not u.hidden for u in units if u.side == "Persia" and u.hp > 0)


def valid_deploy_hex(pos):
    q, r = pos
    return pos in tiles and q <= 4 and not get_unit_at(pos)


def deploy_unit(unit, target):
    global deployment_points, message

    if deployment_points <= 0:
        message = "No deployment points left."
        return

    if unit.side != "Macedon":
        return

    if not valid_deploy_hex(target):
        message = "Invalid deployment hex. Use the Macedonian deployment zone."
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

    if terrain == "rough" and unit.role in ["cavalry", "chariot"]:
        extra_cost = 1

    if dist + extra_cost > unit.move:
        message = "Terrain slows that unit."
        return

    unit.q, unit.r = target
    unit.acted = True
    logistics -= 2
    message = f"{unit.name} moved."


def attack_unit(attacker, defender):
    global macedon_morale, persia_morale, message

    if attacker.acted:
        message = f"{attacker.name} has already acted."
        return

    if defender.hidden:
        message = "Cannot attack unrevealed enemy."
        return

    dist = hex_distance(attacker.pos, defender.pos)

    if dist > attacker.range:
        message = "Target out of range."
        return

    terrain_bonus = 0

    if tiles[defender.pos].terrain == "rough":
        terrain_bonus += 1

    if defender.role == "phalanx" and attacker.role == "chariot":
        terrain_bonus += 2

    damage = max(1, attacker.atk + random.randint(-1, 2) - terrain_bonus)

    if all_persians_visible() and attacker.side == "Macedon":
        damage += 1

    defender.hp -= damage
    attacker.acted = True

    if defender.hp <= 0:
        defender.hp = 0
        if defender.side == "Persia":
            persia_morale -= 15
        else:
            macedon_morale -= 15
        message = f"{attacker.name} destroyed {defender.name}!"
    else:
        message = f"{attacker.name} hit {defender.name} for {damage}."


def reset_actions(side):
    for u in units:
        if u.side == side and u.hp > 0:
            u.acted = False


def estimate_ai_intent():
    persian_cav = [u for u in units if u.side == "Persia" and u.role == "cavalry" and u.hp > 0]
    chariots = [u for u in units if u.side == "Persia" and u.role == "chariot" and u.hp > 0]

    hints = []

    if chariots:
        hints.append("Chariots favor prepared plain. Use rough ground or skirmishers.")

    if persian_cav:
        hints.append("Persian cavalry will pressure your wings.")

    darius = next((u for u in units if u.name == "Darius" and u.hp > 0), None)

    if darius and not darius.hidden:
        hints.append("Darius is visible. A center strike can collapse Persian morale.")

    return " ".join(hints) if hints else "Persian intent unclear."


def ai_turn():
    global turn, phase, message, logistics, turn_number, assessment_points

    persians = friendly_units("Persia")
    macedonians = friendly_units("Macedon")

    for p in persians:
        if p.hidden:
            if any(hex_distance(p.pos, m.pos) <= 2 for m in macedonians):
                p.hidden = False

        if p.hp <= 0:
            continue

        targets = [m for m in macedonians if m.hp > 0]

        if not targets:
            break

        target = min(targets, key=lambda m: hex_distance(p.pos, m.pos))
        dist = hex_distance(p.pos, target.pos)

        if dist <= p.range and not p.acted:
            attack_unit(p, target)
            continue

        candidates = neighbors(p.q, p.r)
        candidates = [c for c in candidates if c in tiles and not get_unit_at(c)]

        if not candidates:
            continue

        if p.role == "chariot":
            candidates.sort(key=lambda c: (
                hex_distance(c, target.pos),
                0 if tiles[c].terrain == "prepared" else 1
            ))
        elif p.role == "cavalry":
            candidates.sort(key=lambda c: (
                hex_distance(c, target.pos),
                -abs(c[1] - 5)
            ))
        elif p.name == "Darius":
            alex = next((m for m in macedonians if m.name == "Alexander"), None)
            if alex:
                candidates.sort(key=lambda c: -hex_distance(c, alex.pos))
        else:
            candidates.sort(key=lambda c: hex_distance(c, target.pos))

        chosen = candidates[0]
        p.q, p.r = chosen
        p.acted = True

    reset_actions("Persia")
    reset_actions("Macedon")
    turn = "Macedon"
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

    turn = "Persia"
    phase = "AI"
    message = "Persian AI is moving..."
    pygame.time.set_timer(pygame.USEREVENT, 500)


def check_victory():
    alex = next((u for u in units if u.name == "Alexander"), None)
    darius = next((u for u in units if u.name == "Darius"), None)

    if alex is None or alex.hp <= 0:
        return "Persia wins. Alexander has fallen."

    if darius is None or darius.hp <= 0:
        return "Macedon wins. Darius is routed."

    if persia_morale <= 0:
        return "Macedon wins. Persian morale collapses."

    if macedon_morale <= 0:
        return "Persia wins. Macedonian morale collapses."

    if logistics <= 0:
        return "Persia wins. Macedonian logistics are exhausted."

    return None


def draw_text(text, x, y, color=TEXT, f=font):
    img = f.render(text, True, color)
    screen.blit(img, (x, y))


def draw_map():
    for pos, tile in tiles.items():
        cx, cy = axial_to_pixel(tile.q, tile.r)

        if phase == "DEPLOY" and tile.q <= 4:
            color = DEPLOY_ZONE
        elif not tile.revealed and tile.q > 6:
            color = HIDDEN
        elif tile.terrain == "plain":
            color = TERRAIN_PLAIN
        elif tile.terrain == "rough":
            color = TERRAIN_ROUGH
        elif tile.terrain == "prepared":
            color = TERRAIN_PREPARED
        elif tile.terrain == "supply":
            color = TERRAIN_SUPPLY
        else:
            color = TERRAIN_PLAIN

        pygame.draw.polygon(screen, color, hex_corners(cx, cy))
        pygame.draw.polygon(screen, GRID, hex_corners(cx, cy), 2)

        if selected and selected.pos == pos:
            pygame.draw.polygon(screen, SELECT, hex_corners(cx, cy), 4)


def draw_units():
    for u in units:
        if u.hp <= 0:
            continue

        if u.hidden:
            continue

        cx, cy = axial_to_pixel(u.q, u.r)
        color = MACEDONIAN if u.side == "Macedon" else PERSIAN

        pygame.draw.circle(screen, color, (cx, cy), 19)
        pygame.draw.circle(screen, (20, 20, 20), (cx, cy), 19, 2)

        label = u.name[:2].upper()
        draw_text(label, cx - 12, cy - 9, (255, 255, 255))
        draw_text(str(u.hp), cx - 9, cy + 18, TEXT)


def draw_sidebar():
    x = 760
    pygame.draw.rect(screen, (38, 35, 30), (740, 0, 460, HEIGHT))

    draw_text("GAUGAMELA: STRATEGIC ASSESSMENT", x, 20, TEXT, big_font)
    draw_text(f"Turn: {turn_number if turn_number else 'Pre-Battle'}", x, 65)
    draw_text(f"Phase: {phase}", x, 90)

    if phase == "DEPLOY":
        draw_text(f"Deployment Points: {deployment_points}", x, 115)
        draw_text("Use deployment before battle.", x, 145)
    else:
        draw_text(f"Assessment Points: {assessment_points}", x, 115)
        draw_text(f"Macedon Morale: {macedon_morale}", x, 145)
        draw_text(f"Persia Morale: {persia_morale}", x, 170)
        draw_text(f"Logistics: {logistics}", x, 195)

    draw_text("Controls", x, 235, TEXT, big_font)

    if phase == "DEPLOY":
        draw_text("Click Macedonian unit: select", x, 275)
        draw_text("Click blue zone hex: redeploy", x, 300)
        draw_text("S: scout selected unit area", x, 325)
        draw_text("I: estimate Persian intent", x, 350)
        draw_text("F: pre-battle feint right", x, 375)
        draw_text("B: begin battle", x, 400)
    else:
        draw_text("Click unit: select", x, 275)
        draw_text("Click empty hex: move", x, 300)
        draw_text("Click enemy: attack", x, 325)
        draw_text("S: scout selected unit area", x, 350)
        draw_text("I: estimate Persian intent", x, 375)
        draw_text("F: feint right", x, 400)
        draw_text("E: end turn", x, 425)

    draw_text("Selected", x, 470, TEXT, big_font)

    if selected:
        draw_text(f"{selected.name}", x, 510)
        draw_text(f"Role: {selected.role}", x, 535)
        draw_text(f"HP: {selected.hp}", x, 560)
        draw_text(f"ATK: {selected.atk}", x, 585)
        draw_text(f"MOVE: {selected.move}", x, 610)
    else:
        draw_text("None", x, 510)

    draw_text("Report", x, 655, TEXT, big_font)

    wrapped = wrap_text(message, 42)
    yy = 695
    for line in wrapped[:4]:
        draw_text(line, x, yy)
        yy += 22


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


def draw_legend():
    draw_text("Terrain: green=plain, tan=prepared chariot ground, gray=rough, blue=supply/deployment", 40, 740)


def feint_right():
    global message, assessment_points, deployment_points

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

    alex = next((u for u in units if u.name == "Alexander" and u.hp > 0), None)
    cav = next((u for u in units if u.name == "Companion Cav" and u.hp > 0), None)

    if not alex or not cav:
        return

    for u in [alex, cav]:
        target = (min(MAP_COLS - 1, u.q + 1), max(0, u.r - 1))
        if target in tiles and not get_unit_at(target):
            u.q, u.r = target

    for p in units:
        if p.side == "Persia" and p.role == "cavalry" and p.hp > 0:
            if random.random() < 0.65:
                p.r = max(0, p.r - 1)
                p.hidden = False

    message = "Feint right executed. Persian cavalry shifts outward. Look for a center gap."


for pos, tile in tiles.items():
    if tile.q <= 6:
        tile.revealed = True

running = True
game_over = None

while running:
    clock.tick(FPS)
    screen.fill(BG)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.USEREVENT:
            pygame.time.set_timer(pygame.USEREVENT, 0)
            ai_turn()

        if event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_b and phase == "DEPLOY":
                begin_battle()

            elif event.key == pygame.K_e and turn == "Macedon":
                end_player_turn()

            elif event.key == pygame.K_s and selected and turn == "Macedon":
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

            elif event.key == pygame.K_i and turn == "Macedon":
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

            elif event.key == pygame.K_f and turn == "Macedon":
                feint_right()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            mx, my = pygame.mouse.get_pos()

            if mx < 730 and turn == "Macedon":
                clicked = pixel_to_axial(mx, my)
                clicked_unit = get_unit_at(clicked)

                if clicked_unit and clicked_unit.side == "Macedon":
                    selected = clicked_unit
                    message = f"Selected {selected.name}."

                elif selected and phase == "DEPLOY" and not clicked_unit:
                    deploy_unit(selected, clicked)

                elif selected and phase != "DEPLOY" and clicked_unit and clicked_unit.side != selected.side:
                    attack_unit(selected, clicked_unit)

                elif selected and phase != "DEPLOY" and not clicked_unit:
                    move_unit(selected, clicked)

    game_over = check_victory()

    draw_map()
    draw_units()
    draw_sidebar()
    draw_legend()

    if game_over:
        pygame.draw.rect(screen, (20, 20, 20), (230, 300, 720, 120))
        draw_text(game_over, 260, 335, TEXT, big_font)
        draw_text("Close the window to exit.", 260, 380)

    pygame.display.flip()

pygame.quit()
