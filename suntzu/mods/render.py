
import pygame

import constants as C
from hex_utils import axial_to_screen, hex_corners
from assets import UNIT_IMAGES
from logic import valid_deploy_preview

WIDTH = C.WIDTH
HEIGHT = C.HEIGHT
BG = C.BG
PANEL = C.PANEL
GRID = C.GRID
TEXT = C.TEXT
MUTED = C.MUTED
SELECT = C.SELECT
BUTTON = C.BUTTON
BUTTON_HOVER = C.BUTTON_HOVER
BLUE = C.BLUE
RED = C.RED
BROWN = C.BROWN
HIDDEN = C.HIDDEN
DEPLOY = C.DEPLOY
PLAIN = C.PLAIN
TERRAIN_COLORS = C.TERRAIN_COLORS
BACK_BUTTON_RECT = C.BACK_BUTTON_RECT
PRINCIPLE_DROPDOWN_RECT = C.PRINCIPLE_DROPDOWN_RECT
DROPDOWN_OPTION_HEIGHT = C.DROPDOWN_OPTION_HEIGHT
DROPDOWN_PANEL_PADDING = C.DROPDOWN_PANEL_PADDING
DROPDOWN_MAX_VISIBLE_OPTIONS = C.DROPDOWN_MAX_VISIBLE_OPTIONS
MAP_VIEW_RECT = getattr(C, "MAP_VIEW_RECT", pygame.Rect(0, 0, 735, 720))


def draw_text(screen, font, text, x, y, color=TEXT, center=False, center_x=None):
    img = font.render(str(text), True, color)
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


def draw_wrapped_text(screen, font, text, x, y, width_chars, color=TEXT, line_height=21, max_lines=None, center=False, center_x=None):
    lines = wrap_text(text, width_chars)
    if max_lines is not None:
        lines = lines[:max_lines]
    for line in lines:
        draw_text(screen, font, line, x, y, color, center=center, center_x=center_x)
        y += line_height
    return y


def tile_color(state, tile):
    if state.phase == "DEPLOY" and valid_deploy_preview(state, tile.q, tile.r):
        return DEPLOY
    if not tile.revealed and tile.q > 6:
        return HIDDEN
    return TERRAIN_COLORS.get(tile.terrain, PLAIN)


def draw_map(screen, state):
    pygame.draw.rect(screen, BG, MAP_VIEW_RECT)
    for pos, tile in state.tiles.items():
        cx, cy = axial_to_screen(tile.q, tile.r, state.camera_x, state.camera_y)
        if not (-60 <= cx <= MAP_VIEW_RECT.right + 60 and -60 <= cy <= MAP_VIEW_RECT.bottom + 60):
            continue
        pygame.draw.polygon(screen, tile_color(state, tile), hex_corners(cx, cy))
        pygame.draw.polygon(screen, GRID, hex_corners(cx, cy), 2)
        if state.selected and state.selected.pos == pos:
            pygame.draw.polygon(screen, SELECT, hex_corners(cx, cy), 4)
    pygame.draw.rect(screen, GRID, MAP_VIEW_RECT, 2)


def draw_terrain_decorations(screen, state):
    for pos, tile in state.tiles.items():
        if not tile.revealed and tile.q > 6:
            continue
        cx, cy = axial_to_screen(tile.q, tile.r, state.camera_x, state.camera_y)
        if not (-60 <= cx <= MAP_VIEW_RECT.right + 60 and -60 <= cy <= MAP_VIEW_RECT.bottom + 60):
            continue
        if tile.terrain == "forest":
            pygame.draw.circle(screen, (25, 70, 30), (cx - 8, cy + 4), 6)
            pygame.draw.circle(screen, (25, 80, 35), (cx, cy - 5), 7)
            pygame.draw.circle(screen, (25, 70, 30), (cx + 9, cy + 5), 6)
        elif tile.terrain == "city":
            pygame.draw.rect(screen, (70, 65, 60), (cx - 14, cy - 8, 8, 16))
            pygame.draw.rect(screen, (80, 75, 68), (cx - 3, cy - 13, 8, 21))
            pygame.draw.rect(screen, (65, 60, 55), (cx + 8, cy - 6, 8, 14))
        elif tile.terrain == "bridge":
            pygame.draw.line(screen, (55, 110, 150), (cx - 22, cy + 8), (cx + 22, cy - 8), 6)
            pygame.draw.line(screen, (180, 135, 80), (cx - 20, cy), (cx + 20, cy), 3)
        elif tile.terrain == "river":
            pygame.draw.line(screen, (70, 140, 185), (cx - 20, cy + 8), (cx + 20, cy - 8), 7)
        elif tile.terrain == "blockade":
            pygame.draw.circle(screen, (190, 230, 240), (cx, cy), 15, 2)
            pygame.draw.line(screen, (190, 230, 240), (cx, cy - 15), (cx, cy + 15), 2)
        elif tile.terrain == "road":
            pygame.draw.line(screen, (155, 135, 95), (cx - 22, cy), (cx + 22, cy), 5)
        elif tile.terrain == "airfield":
            pygame.draw.line(screen, (190, 190, 180), (cx - 20, cy), (cx + 20, cy), 4)
            pygame.draw.line(screen, (190, 190, 180), (cx, cy - 16), (cx, cy + 16), 2)
        elif tile.terrain == "bunker":
            pygame.draw.rect(screen, (55, 55, 55), (cx - 14, cy - 8, 28, 16))
            pygame.draw.rect(screen, (25, 25, 25), (cx - 6, cy - 3, 12, 6))
        elif tile.terrain == "objective":
            pygame.draw.circle(screen, (190, 155, 55), (cx, cy), 11, 3)
        elif tile.terrain == "supply":
            pygame.draw.rect(screen, (45, 85, 120), (cx - 12, cy - 10, 24, 20), 2)
            pygame.draw.circle(screen, (160, 190, 210), (cx - 5, cy + 10), 3)
            pygame.draw.circle(screen, (160, 190, 210), (cx + 7, cy + 10), 3)
        elif tile.terrain == "village":
            pygame.draw.rect(screen, (75, 55, 45), (cx - 12, cy - 5, 10, 12))
            pygame.draw.polygon(screen, (120, 70, 55), [(cx - 14, cy - 5), (cx - 7, cy - 13), (cx, cy - 5)])


def tint_image(img, color):
    tinted = img.copy()
    tint = pygame.Surface(tinted.get_size(), pygame.SRCALPHA)
    tint.fill((*color, 90))
    tinted.blit(tint, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
    return tinted


def draw_fallback_unit_icon(screen, small_font, state, unit, cx, cy):
    color = BROWN if unit.role == "elephant" else (BLUE if unit.side == state.current_scenario.player_side else RED)
    pygame.draw.circle(screen, color, (cx, cy), 19)
    pygame.draw.circle(screen, (20, 20, 20), (cx, cy), 19, 2)
    label = {"commander":"CM","cavalry":"CV","infantry":"IN","elite infantry":"EI","phalanx":"PH","skirmisher":"SK","guard":"GD","artillery":"AR","chariot":"CH","elephant":"EL","paratrooper":"PT","armor":"TK","naval":"NV","bunker":"BK","aircraft":"JF","mechanized":"MC","airdefense":"AD"}.get(unit.role, unit.name[:2].upper())
    draw_text(screen, small_font, label, 0, cy - 9, (255, 255, 255), center=True, center_x=cx)


def draw_units(screen, small_font, state):
    for unit in state.units:
        if unit.hp <= 0 or unit.hidden:
            continue
        cx, cy = axial_to_screen(unit.q, unit.r, state.camera_x, state.camera_y)
        if not (-60 <= cx <= MAP_VIEW_RECT.right + 60 and -60 <= cy <= MAP_VIEW_RECT.bottom + 60):
            continue
        img = UNIT_IMAGES.get(unit.role)
        if img:
            border_color = BLUE if unit.side == state.current_scenario.player_side else RED
            if unit.role == "elephant": border_color = BROWN
            pygame.draw.circle(screen, border_color, (cx, cy), 23)
            pygame.draw.circle(screen, (20, 20, 20), (cx, cy), 23, 2)
            final_img = tint_image(img, border_color)
            screen.blit(final_img, final_img.get_rect(center=(cx, cy)))
        else:
            draw_fallback_unit_icon(screen, small_font, state, unit, cx, cy)
        draw_text(screen, small_font, str(unit.hp), 0, cy + 21, TEXT, center=True, center_x=cx)


def draw_dropdown(screen, font, state):
    mx, my = pygame.mouse.get_pos()
    color = BUTTON_HOVER if PRINCIPLE_DROPDOWN_RECT.collidepoint(mx, my) else BUTTON
    pygame.draw.rect(screen, color, PRINCIPLE_DROPDOWN_RECT, border_radius=8)
    pygame.draw.rect(screen, GRID, PRINCIPLE_DROPDOWN_RECT, 2, border_radius=8)
    selected_principle = state.principles[state.selected_principle_index]
    draw_text(screen, font, f"Principle: {selected_principle.title}  v", 0, PRINCIPLE_DROPDOWN_RECT.y + 11, TEXT, center=True, center_x=PRINCIPLE_DROPDOWN_RECT.centerx)
    if not state.dropdown_open:
        return
    visible_count = min(len(state.principles), DROPDOWN_MAX_VISIBLE_OPTIONS)
    panel_rect = pygame.Rect(PRINCIPLE_DROPDOWN_RECT.x, PRINCIPLE_DROPDOWN_RECT.bottom + 6, PRINCIPLE_DROPDOWN_RECT.width, visible_count * DROPDOWN_OPTION_HEIGHT + DROPDOWN_PANEL_PADDING * 2)
    pygame.draw.rect(screen, (30, 28, 24), panel_rect, border_radius=10)
    pygame.draw.rect(screen, SELECT, panel_rect, 2, border_radius=10)
    for principle_index, principle in enumerate(state.principles[:visible_count]):
        option_rect = pygame.Rect(panel_rect.x + DROPDOWN_PANEL_PADDING, panel_rect.y + DROPDOWN_PANEL_PADDING + principle_index * DROPDOWN_OPTION_HEIGHT, panel_rect.width - DROPDOWN_PANEL_PADDING * 2, DROPDOWN_OPTION_HEIGHT)
        pygame.draw.rect(screen, (75,65,35) if principle_index == state.selected_principle_index else PANEL, option_rect, border_radius=6)
        draw_text(screen, font, principle.title, 0, option_rect.y + 12, SELECT if principle_index == state.selected_principle_index else TEXT, center=True, center_x=option_rect.centerx)


def draw_scenario_select(screen, font, small_font, big_font, state):
    screen.fill(BG)
    center_x = WIDTH // 2
    draw_text(screen, big_font, "SUN TZU HEX TACTICS", 0, 35, TEXT, center=True, center_x=center_x)
    draw_text(screen, font, "Select a principle, then choose a scenario", 0, 72, MUTED, center=True, center_x=center_x)
    principle = state.principles[state.selected_principle_index]
    draw_wrapped_text(screen, small_font, principle.description, 180, 162, 95, MUTED, 18, max_lines=2, center=True, center_x=center_x)
    visible_scenarios = state.scenarios_for_selected_principle()
    card_w, card_h = 820, 125
    x, start_y, gap = (WIDTH - card_w) // 2, 215, 140
    for scenario_index, scenario in enumerate(visible_scenarios):
        y = start_y + scenario_index * gap
        card_center = x + card_w // 2
        pygame.draw.rect(screen, PANEL, (x, y, card_w, card_h), border_radius=12)
        pygame.draw.rect(screen, GRID, (x, y, card_w, card_h), 2, border_radius=12)
        draw_text(screen, big_font, f"{scenario_index + 1}. {scenario.title}", 0, y + 18, TEXT, center=True, center_x=card_center)
        draw_text(screen, small_font, scenario.subtitle, 0, y + 53, MUTED, center=True, center_x=card_center)
        draw_wrapped_text(screen, small_font, scenario.description, x + 25, y + 78, 80, TEXT, 18, max_lines=2, center=True, center_x=card_center)
    draw_text(screen, font, "Press 1-9, click a scenario, or click the principle selector.", 0, 720, TEXT, center=True, center_x=center_x)
    draw_dropdown(screen, font, state)


def draw_back_button(screen, small_font):
    mx, my = pygame.mouse.get_pos()
    color = BUTTON_HOVER if BACK_BUTTON_RECT.collidepoint(mx, my) else BUTTON
    pygame.draw.rect(screen, color, BACK_BUTTON_RECT, border_radius=8)
    pygame.draw.rect(screen, GRID, BACK_BUTTON_RECT, 2, border_radius=8)
    draw_text(screen, small_font, "Back to Scenarios  (M / ESC)", 0, BACK_BUTTON_RECT.y + 8, TEXT, center=True, center_x=BACK_BUTTON_RECT.centerx)


def draw_supply_bar(screen, small_font, x, y, width, height, state):
    logistics = max(0, min(state.logistics, 140))
    pct = min(logistics / 140, 1.0)
    fill = (70,145,90) if state.logistics >= 80 else ((185,155,60) if state.logistics >= 50 else ((190,105,45) if state.logistics >= 30 else (190,60,45)))
    pygame.draw.rect(screen, (25,25,25), (x, y, width, height), border_radius=5)
    pygame.draw.rect(screen, fill, (x, y, int(width * pct), height), border_radius=5)
    pygame.draw.rect(screen, GRID, (x, y, width, height), 1, border_radius=5)
    draw_text(screen, small_font, f"Logistics / Supply: {state.logistics}", 0, y + height + 4, TEXT, center=True, center_x=x + width // 2)


def draw_sidebar(screen, font, small_font, big_font, state):
    x, w = 750, 430
    center_x = x + w // 2
    pygame.draw.rect(screen, PANEL, (740, 0, 460, HEIGHT))
    draw_text(screen, big_font, "SUN TZU HEX TACTICS", 0, 18, TEXT, center=True, center_x=center_x)
    y = 54
    principle = next(p for p in state.principles if p.key == state.current_scenario.principle_key)
    y = draw_wrapped_text(screen, small_font, principle.title, x, y, 38, SELECT, 18, max_lines=2, center=True, center_x=center_x)
    y = draw_wrapped_text(screen, font, state.current_scenario.title, x, y + 3, 38, TEXT, 21, max_lines=2, center=True, center_x=center_x)
    y += 10
    draw_text(screen, font, f"Turn: {state.turn_number if state.turn_number else 'Pre-Battle'}", 0, y, TEXT, center=True, center_x=center_x); y += 23
    draw_text(screen, font, f"Phase: {state.phase}", 0, y, TEXT, center=True, center_x=center_x); y += 25
    draw_supply_bar(screen, small_font, x + 30, y, 360, 14, state); y += 43
    if state.phase == "DEPLOY":
        draw_text(screen, font, f"Deployment Points: {state.deployment_points}", 0, y, TEXT, center=True, center_x=center_x); y += 25
    else:
        draw_text(screen, font, f"Assessment Points: {state.assessment_points}", 0, y, TEXT, center=True, center_x=center_x); y += 22
        draw_text(screen, font, f"{state.current_scenario.player_side} Morale: {state.player_morale}", 0, y, TEXT, center=True, center_x=center_x); y += 22
        draw_text(screen, font, f"{state.current_scenario.enemy_side} Morale: {state.enemy_morale}", 0, y, TEXT, center=True, center_x=center_x); y += 25
    if state.logistics <= 30:
        y = draw_wrapped_text(screen, small_font, "SUPPLY WARNING: Press L to check supply. Press R to resupply if units are on supply, road, or bridge hexes.", x, y, 39, (255,190,120), 18, max_lines=3, center=True, center_x=center_x)
        y += 6
    draw_text(screen, big_font, "Controls", 0, y, TEXT, center=True, center_x=center_x); y += 34
    controls = ["Arrow/WASD: scroll map", "Wheel: vertical scroll", "Shift+wheel: horizontal", "Home: reset camera", "L: check logistics", "R: resupply on supply/road/bridge"]
    controls += ["Click unit: select", "Click empty hex: move/redeploy", "Click enemy: attack", "S: scout", "I: enemy intent", "F: special action", "B: begin battle" if state.phase == "DEPLOY" else "E: end turn"]
    for item in controls:
        y = draw_wrapped_text(screen, small_font, item, x, y, 39, TEXT, 18, max_lines=2, center=True, center_x=center_x)
    report_y = 638
    pygame.draw.rect(screen, (30,28,24), (750, report_y - 8, 430, 90), border_radius=8)
    pygame.draw.rect(screen, GRID, (750, report_y - 8, 430, 90), 1, border_radius=8)
    draw_text(screen, font, "Report", 0, report_y, TEXT, center=True, center_x=center_x)
    draw_wrapped_text(screen, small_font, state.message, x, report_y + 26, 41, TEXT, 18, max_lines=3, center=True, center_x=center_x)
    draw_back_button(screen, small_font)


def draw_legend(screen, small_font):
    pygame.draw.rect(screen, (25,24,21), (25, 732, 700, 42), border_radius=8)
    draw_wrapped_text(screen, small_font, "Terrain: blue=supply/river/sea/blockade. Roads/bridges help resupply. Supply hexes restore most logistics.", 35, 739, 80, TEXT, 18, max_lines=2, center=True, center_x=375)


def draw_game(screen, font, small_font, big_font, state):
    screen.fill(BG)
    draw_map(screen, state)
    draw_terrain_decorations(screen, state)
    draw_units(screen, small_font, state)
    draw_sidebar(screen, font, small_font, big_font, state)
    draw_legend(screen, small_font)


def draw_game_over(screen, font, big_font, state):
    if not state.game_over:
        return
    pygame.draw.rect(screen, (20,20,20), (210, 300, 760, 150))
    pygame.draw.rect(screen, SELECT, (210, 300, 760, 150), 2)
    draw_wrapped_text(screen, big_font, state.game_over, 245, 328, 60, TEXT, 32, max_lines=2, center=True, center_x=590)
    draw_text(screen, font, "Press M or ESC to return to scenarios.", 0, 405, TEXT, center=True, center_x=590)

