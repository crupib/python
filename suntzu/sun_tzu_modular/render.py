# sun_tzu_hex_modular/render.py

import pygame
from constants import *
from hex_utils import axial_to_pixel, hex_corners
from assets import UNIT_IMAGES
from logic import valid_deploy_preview


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
    for pos, tile in state.tiles.items():
        cx, cy = axial_to_pixel(tile.q, tile.r)
        pygame.draw.polygon(screen, tile_color(state, tile), hex_corners(cx, cy))
        pygame.draw.polygon(screen, GRID, hex_corners(cx, cy), 2)
        if state.selected and state.selected.pos == pos:
            pygame.draw.polygon(screen, SELECT, hex_corners(cx, cy), 4)


def draw_terrain_decorations(screen, state):
    for pos, tile in state.tiles.items():
        if not tile.revealed and tile.q > 6:
            continue
        cx, cy = axial_to_pixel(tile.q, tile.r)
        if tile.terrain == "forest":
            pygame.draw.circle(screen, (25, 70, 30), (cx - 8, cy + 4), 6)
            pygame.draw.circle(screen, (25, 80, 35), (cx, cy - 5), 7)
            pygame.draw.circle(screen, (25, 70, 30), (cx + 9, cy + 5), 6)
            pygame.draw.rect(screen, (70, 45, 25), (cx - 2, cy + 4, 4, 8))
        elif tile.terrain == "city":
            pygame.draw.rect(screen, (70, 65, 60), (cx - 14, cy - 8, 8, 16))
            pygame.draw.rect(screen, (80, 75, 68), (cx - 3, cy - 13, 8, 21))
            pygame.draw.rect(screen, (65, 60, 55), (cx + 8, cy - 6, 8, 14))
            pygame.draw.line(screen, (160, 150, 130), (cx - 16, cy + 12), (cx + 16, cy + 12), 2)
        elif tile.terrain == "bridge":
            pygame.draw.line(screen, (55, 110, 150), (cx - 22, cy + 8), (cx + 22, cy - 8), 6)
            pygame.draw.line(screen, (80, 55, 35), (cx - 20, cy), (cx + 20, cy), 7)
            pygame.draw.line(screen, (180, 135, 80), (cx - 20, cy), (cx + 20, cy), 3)
        elif tile.terrain == "river":
            pygame.draw.line(screen, (70, 140, 185), (cx - 20, cy + 8), (cx + 20, cy - 8), 7)
            pygame.draw.line(screen, (100, 170, 210), (cx - 18, cy + 3), (cx + 18, cy - 13), 2)
        elif tile.terrain == "road":
            pygame.draw.line(screen, (155, 135, 95), (cx - 22, cy), (cx + 22, cy), 5)
            pygame.draw.line(screen, (95, 80, 55), (cx - 22, cy), (cx + 22, cy), 1)
        elif tile.terrain == "airfield":
            pygame.draw.line(screen, (190, 190, 180), (cx - 20, cy), (cx + 20, cy), 4)
            pygame.draw.line(screen, (190, 190, 180), (cx, cy - 16), (cx, cy + 16), 2)
            pygame.draw.circle(screen, (60, 60, 60), (cx, cy), 4)
        elif tile.terrain == "bunker":
            pygame.draw.rect(screen, (55, 55, 55), (cx - 14, cy - 8, 28, 16))
            pygame.draw.rect(screen, (25, 25, 25), (cx - 6, cy - 3, 12, 6))
            pygame.draw.line(screen, (120, 120, 120), (cx - 12, cy - 9), (cx + 12, cy - 9), 2)
        elif tile.terrain == "objective":
            pygame.draw.circle(screen, (190, 155, 55), (cx, cy), 11, 3)
            pygame.draw.line(screen, (190, 155, 55), (cx, cy - 14), (cx, cy + 14), 2)
            pygame.draw.line(screen, (190, 155, 55), (cx - 14, cy), (cx + 14, cy), 2)
        elif tile.terrain == "supply":
            pygame.draw.rect(screen, (45, 85, 120), (cx - 12, cy - 10, 24, 20), 2)
            pygame.draw.circle(screen, (160, 190, 210), (cx - 5, cy + 10), 3)
            pygame.draw.circle(screen, (160, 190, 210), (cx + 7, cy + 10), 3)
        elif tile.terrain == "village":
            pygame.draw.rect(screen, (75, 55, 45), (cx - 12, cy - 5, 10, 12))
            pygame.draw.polygon(screen, (120, 70, 55), [(cx - 14, cy - 5), (cx - 7, cy - 13), (cx, cy - 5)])
            pygame.draw.rect(screen, (85, 65, 50), (cx + 4, cy - 3, 11, 10))
            pygame.draw.polygon(screen, (120, 70, 55), [(cx + 2, cy - 3), (cx + 10, cy - 11), (cx + 18, cy - 3)])


def tint_image(img, color):
    tinted = img.copy()
    tint = pygame.Surface(tinted.get_size(), pygame.SRCALPHA)
    tint.fill((*color, 90))
    tinted.blit(tint, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
    return tinted


def draw_fallback_unit_icon(screen, small_font, state, u, cx, cy):
    color = BROWN if u.role == "elephant" else BLUE if u.side == state.current_scenario.player_side else RED
    pygame.draw.circle(screen, color, (cx, cy), 19)
    pygame.draw.circle(screen, (20, 20, 20), (cx, cy), 19, 2)
    label = {"commander": "CM", "cavalry": "CV", "infantry": "IN", "elite infantry": "EI", "phalanx": "PH", "skirmisher": "SK", "guard": "GD", "artillery": "AR", "chariot": "CH", "elephant": "EL", "paratrooper": "PT", "armor": "TK", "naval": "NV", "bunker": "BK", "aircraft": "JF", "mechanized": "MC", "airdefense": "AD"}.get(u.role, u.name[:2].upper())
    draw_text(screen, small_font, label, 0, cy - 9, (255, 255, 255), center=True, center_x=cx)


def draw_units(screen, small_font, state):
    for u in state.units:
        if u.hp <= 0 or u.hidden:
            continue
        cx, cy = axial_to_pixel(u.q, u.r)
        img = UNIT_IMAGES.get(u.role)
        if img:
            border_color = BLUE if u.side == state.current_scenario.player_side else RED
            if u.role == "elephant":
                border_color = BROWN
            pygame.draw.circle(screen, border_color, (cx, cy), 23)
            pygame.draw.circle(screen, (20, 20, 20), (cx, cy), 23, 2)
            final_img = tint_image(img, border_color)
            screen.blit(final_img, final_img.get_rect(center=(cx, cy)))
        else:
            draw_fallback_unit_icon(screen, small_font, state, u, cx, cy)
        draw_text(screen, small_font, str(u.hp), 0, cy + 21, TEXT, center=True, center_x=cx)


def draw_scenario_select(screen, font, small_font, big_font, state):
    screen.fill(BG)
    center_x = WIDTH // 2
    draw_text(screen, big_font, "SUN TZU HEX TACTICS", 0, 35, TEXT, center=True, center_x=center_x)
    draw_text(screen, font, "Select a principle, then choose a scenario", 0, 72, MUTED, center=True, center_x=center_x)

    mx, my = pygame.mouse.get_pos()
    hover = PRINCIPLE_DROPDOWN_RECT.collidepoint(mx, my)
    pygame.draw.rect(screen, BUTTON_HOVER if hover else BUTTON, PRINCIPLE_DROPDOWN_RECT, border_radius=8)
    pygame.draw.rect(screen, GRID, PRINCIPLE_DROPDOWN_RECT, 2, border_radius=8)
    principle = state.principles[state.selected_principle_index]
    draw_text(screen, font, f"Principle: {principle.title}  v", 0, PRINCIPLE_DROPDOWN_RECT.y + 11, TEXT, center=True, center_x=PRINCIPLE_DROPDOWN_RECT.centerx)

    if state.dropdown_open:
        option_h = 42
        for i, principle_option in enumerate(state.principles):
            rect = pygame.Rect(PRINCIPLE_DROPDOWN_RECT.x, PRINCIPLE_DROPDOWN_RECT.y + PRINCIPLE_DROPDOWN_RECT.height + i * option_h, PRINCIPLE_DROPDOWN_RECT.width, option_h)
            pygame.draw.rect(screen, BUTTON_HOVER if rect.collidepoint(mx, my) else PANEL, rect)
            pygame.draw.rect(screen, GRID, rect, 1)
            draw_text(screen, font, principle_option.title, 0, rect.y + 11, TEXT if i != state.selected_principle_index else SELECT, center=True, center_x=rect.centerx)

    draw_wrapped_text(screen, small_font, principle.description, 180, 162, 95, MUTED, 18, max_lines=2, center=True, center_x=center_x)

    visible_scenarios = state.scenarios_for_selected_principle()
    card_w = 820
    card_h = 125
    x = (WIDTH - card_w) // 2
    start_y = 215
    gap = 140
    for i, scenario in enumerate(visible_scenarios):
        y = start_y + i * gap
        card_center = x + card_w // 2
        pygame.draw.rect(screen, PANEL, (x, y, card_w, card_h), border_radius=12)
        pygame.draw.rect(screen, GRID, (x, y, card_w, card_h), 2, border_radius=12)
        draw_text(screen, big_font, f"{i + 1}. {scenario.title}", 0, y + 18, TEXT, center=True, center_x=card_center)
        draw_text(screen, small_font, scenario.subtitle, 0, y + 53, MUTED, center=True, center_x=card_center)
        draw_wrapped_text(screen, small_font, scenario.description, x + 25, y + 78, 80, TEXT, 18, max_lines=2, center=True, center_x=card_center)

    draw_text(screen, font, "Press 1-9, click a scenario, or click the principle selector.", 0, 720, TEXT, center=True, center_x=center_x)


def draw_back_button(screen, small_font):
    mx, my = pygame.mouse.get_pos()
    hover = BACK_BUTTON_RECT.collidepoint(mx, my)
    pygame.draw.rect(screen, BUTTON_HOVER if hover else BUTTON, BACK_BUTTON_RECT, border_radius=8)
    pygame.draw.rect(screen, GRID, BACK_BUTTON_RECT, 2, border_radius=8)
    draw_text(screen, small_font, "Back to Scenarios  (M / ESC)", 0, BACK_BUTTON_RECT.y + 8, TEXT, center=True, center_x=BACK_BUTTON_RECT.centerx)


def draw_sidebar(screen, font, small_font, big_font, state):
    x = 750
    w = 430
    center_x = x + w // 2
    pygame.draw.rect(screen, PANEL, (740, 0, 460, HEIGHT))
    draw_text(screen, big_font, "SUN TZU HEX TACTICS", 0, 18, TEXT, center=True, center_x=center_x)
    y = 54
    principle = next(p for p in state.principles if p.key == state.current_scenario.principle_key)
    y = draw_wrapped_text(screen, small_font, principle.title, x, y, 38, SELECT, 18, max_lines=2, center=True, center_x=center_x)
    y = draw_wrapped_text(screen, font, state.current_scenario.title, x, y + 3, 38, TEXT, 21, max_lines=2, center=True, center_x=center_x)
    y += 10
    for line in [f"Turn: {state.turn_number if state.turn_number else 'Pre-Battle'}", f"Phase: {state.phase}"]:
        draw_text(screen, font, line, 0, y, TEXT, center=True, center_x=center_x)
        y += 23
    y += 7
    if state.phase == "DEPLOY":
        draw_text(screen, font, f"Deployment Points: {state.deployment_points}", 0, y, TEXT, center=True, center_x=center_x)
        y += 25
    else:
        for line in [f"Assessment Points: {state.assessment_points}", f"{state.current_scenario.player_side} Morale: {state.player_morale}", f"{state.current_scenario.enemy_side} Morale: {state.enemy_morale}", f"Logistics: {state.logistics}"]:
            draw_text(screen, font, line, 0, y, TEXT, center=True, center_x=center_x)
            y += 22
        y += 3
    draw_text(screen, big_font, "Controls", 0, y, TEXT, center=True, center_x=center_x)
    y += 38
    controls = ["Click player unit: select", "Click blue hex: redeploy", "S: scout selected unit area", "I: estimate enemy intent", "F: scenario special action", "B: begin battle"] if state.phase == "DEPLOY" else ["Click unit: select", "Click empty hex: move", "Click enemy: attack", "S: scout selected unit area", "I: estimate enemy intent", "F: scenario special action", "E: end turn"]
    for item in controls:
        y = draw_wrapped_text(screen, small_font, item, x, y, 39, TEXT, 18, max_lines=2, center=True, center_x=center_x)
    y += 12
    draw_text(screen, big_font, "Selected", 0, y, TEXT, center=True, center_x=center_x)
    y += 38
    if state.selected:
        selected_lines = [state.selected.name, f"Role: {state.selected.role}", f"HP: {state.selected.hp}", f"ATK: {state.selected.atk}", f"MOVE: {state.selected.move}", f"RANGE: {state.selected.range}"]
        for item in selected_lines:
            y = draw_wrapped_text(screen, small_font, item, x, y, 39, TEXT, 18, max_lines=2, center=True, center_x=center_x)
    else:
        draw_text(screen, small_font, "None", 0, y, TEXT, center=True, center_x=center_x)
    report_y = 638
    pygame.draw.rect(screen, (30, 28, 24), (750, report_y - 8, 430, 90), border_radius=8)
    pygame.draw.rect(screen, GRID, (750, report_y - 8, 430, 90), 1, border_radius=8)
    draw_text(screen, font, "Report", 0, report_y, TEXT, center=True, center_x=center_x)
    draw_wrapped_text(screen, small_font, state.message, x, report_y + 26, 41, TEXT, 18, max_lines=3, center=True, center_x=center_x)
    draw_back_button(screen, small_font)


def draw_legend(screen, small_font):
    pygame.draw.rect(screen, (25, 24, 21), (25, 732, 700, 42), border_radius=8)
    draw_wrapped_text(screen, small_font, "Terrain: green=plain/forest, tan=desert/prepared, gray=rough/bunker/airfield, blue=sea/river/supply, brown=heights/objective/bridge, city=urban, road=road", 35, 739, 80, TEXT, 18, max_lines=2, center=True, center_x=375)


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
    pygame.draw.rect(screen, (20, 20, 20), (210, 300, 760, 140))
    draw_wrapped_text(screen, big_font, state.game_over, 245, 335, 60, TEXT, 32, max_lines=2, center=True, center_x=590)
    draw_text(screen, font, "Use Back to Scenarios, M, or ESC.", 0, 405, TEXT, center=True, center_x=590)



