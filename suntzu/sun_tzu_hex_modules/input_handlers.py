# sun_tzu_hex_modular/input_handlers.py
import pygame

from constants import (
    WIDTH,
    BACK_BUTTON_RECT,
    PRINCIPLE_DROPDOWN_RECT,
    DROPDOWN_OPTION_HEIGHT,
    DROPDOWN_PANEL_PADDING,
    DROPDOWN_MAX_VISIBLE_OPTIONS,
)
from hex_utils import pixel_to_axial
from logic import (
    start_scenario,
    reveal_around,
    estimate_ai_intent,
    special_feint,
    begin_battle,
    end_player_turn,
    deploy_unit,
    move_unit,
    attack_unit,
    get_unit_at,
)


def handle_game_key(state, event):
    if event.key in [pygame.K_m, pygame.K_ESCAPE]:
        state.go_to_scenario_select()
        return

    if event.key == pygame.K_b and state.phase == "DEPLOY":
        begin_battle(state)
        return

    if event.key == pygame.K_e and state.turn == state.current_scenario.player_side:
        end_player_turn(state)
        return

    if event.key == pygame.K_s and state.selected and state.turn == state.current_scenario.player_side:
        if state.phase == "DEPLOY":
            if state.deployment_points > 0:
                reveal_around(state, state.selected.pos, radius=3)
                state.deployment_points -= 1
            else:
                state.message = "No deployment points left."
        else:
            if state.assessment_points > 0:
                reveal_around(state, state.selected.pos, radius=2)
                state.assessment_points -= 1
            else:
                state.message = "No assessment points left."
        return

    if event.key == pygame.K_i and state.turn == state.current_scenario.player_side:
        if state.phase == "DEPLOY":
            if state.deployment_points > 0:
                estimate_ai_intent(state)
                state.deployment_points -= 1
            else:
                state.message = "No deployment points left."
        else:
            if state.assessment_points > 0:
                estimate_ai_intent(state)
                state.assessment_points -= 1
            else:
                state.message = "No assessment points left."
        return

    if event.key == pygame.K_f and state.turn == state.current_scenario.player_side:
        special_feint(state)


def handle_game_click(state, mx, my):
    if BACK_BUTTON_RECT.collidepoint(mx, my):
        state.go_to_scenario_select()
        return

    if mx >= 730 or state.turn != state.current_scenario.player_side:
        return

    clicked = pixel_to_axial(mx, my)
    clicked_unit = get_unit_at(state, clicked)

    if clicked_unit and clicked_unit.side == state.current_scenario.player_side:
        state.selected = clicked_unit
        state.message = f"Selected {state.selected.name}."
        return

    if state.selected and state.phase == "DEPLOY" and not clicked_unit:
        deploy_unit(state, state.selected, clicked)
        return

    if state.selected and state.phase != "DEPLOY" and clicked_unit and clicked_unit.side != state.selected.side:
        attack_unit(state, state.selected, clicked_unit)
        return

    if state.selected and state.phase != "DEPLOY" and not clicked_unit:
        move_unit(state, state.selected, clicked)


def handle_scenario_click(state, mx, my):
    if PRINCIPLE_DROPDOWN_RECT.collidepoint(mx, my):
        state.dropdown_open = not state.dropdown_open
        return

    if state.dropdown_open:
        visible_count = min(len(state.principles), DROPDOWN_MAX_VISIBLE_OPTIONS)

        panel_rect = pygame.Rect(
            PRINCIPLE_DROPDOWN_RECT.x,
            PRINCIPLE_DROPDOWN_RECT.bottom + 6,
            PRINCIPLE_DROPDOWN_RECT.width,
            visible_count * DROPDOWN_OPTION_HEIGHT + DROPDOWN_PANEL_PADDING * 2,
        )

        for principle_index in range(visible_count):
            option_rect = pygame.Rect(
                panel_rect.x + DROPDOWN_PANEL_PADDING,
                panel_rect.y + DROPDOWN_PANEL_PADDING + principle_index * DROPDOWN_OPTION_HEIGHT,
                panel_rect.width - DROPDOWN_PANEL_PADDING * 2,
                DROPDOWN_OPTION_HEIGHT,
            )

            if option_rect.collidepoint(mx, my):
                state.selected_principle_index = principle_index
                state.dropdown_open = False
                return

        state.dropdown_open = False
        return

    visible_scenarios = state.scenarios_for_selected_principle()

    card_w = 820
    card_h = 125
    x = (WIDTH - card_w) // 2
    start_y = 215
    gap = 140

    for scenario_index, scenario in enumerate(visible_scenarios):
        y = start_y + scenario_index * gap

        if x <= mx <= x + card_w and y <= my <= y + card_h:
            start_scenario(state, scenario)
            return


def handle_scenario_key(state, event):
    if event.key == pygame.K_ESCAPE:
        state.dropdown_open = False
        return

    if event.key == pygame.K_UP:
        state.selected_principle_index = (state.selected_principle_index - 1) % len(state.principles)
        state.dropdown_open = False
        return

    if event.key == pygame.K_DOWN:
        state.selected_principle_index = (state.selected_principle_index + 1) % len(state.principles)
        state.dropdown_open = False
        return

    if event.key == pygame.K_SPACE:
        state.dropdown_open = not state.dropdown_open
        return

    if pygame.K_1 <= event.key <= pygame.K_9:
        idx = event.key - pygame.K_1
        visible_scenarios = state.scenarios_for_selected_principle()

        if idx < len(visible_scenarios):
            start_scenario(state, visible_scenarios[idx])
