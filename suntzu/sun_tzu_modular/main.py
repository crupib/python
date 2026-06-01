# sun_tzu_hex_modular/main.py
import pygame

from constants import WIDTH, HEIGHT, FPS, BACK_BUTTON_RECT
from state import GameState
from scenarios import register_content
from logic import ai_turn, check_victory
from render import draw_scenario_select, draw_game, draw_game_over
from input_handlers import handle_scenario_key, handle_scenario_click, handle_game_key, handle_game_click


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sun Tzu Hex Tactics")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("consolas", 18)
    small_font = pygame.font.SysFont("consolas", 15)
    big_font = pygame.font.SysFont("consolas", 28)
    state = GameState()
    register_content(state)
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if state.screen_mode == "SCENARIO_SELECT":
                if event.type == pygame.KEYDOWN:
                    handle_scenario_key(state, event)
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    handle_scenario_click(state, *pygame.mouse.get_pos())
            elif state.screen_mode == "GAME":
                if event.type == pygame.USEREVENT:
                    pygame.time.set_timer(pygame.USEREVENT, 0)
                    ai_turn(state)
                if event.type == pygame.KEYDOWN and not state.game_over:
                    handle_game_key(state, event)
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if state.game_over and BACK_BUTTON_RECT.collidepoint(*pygame.mouse.get_pos()):
                        state.go_to_scenario_select()
                    elif not state.game_over:
                        handle_game_click(state, *pygame.mouse.get_pos())
        if state.screen_mode == "SCENARIO_SELECT":
            state.game_over = None
            draw_scenario_select(screen, font, small_font, big_font, state)
        elif state.screen_mode == "GAME":
            state.game_over = check_victory(state)
            draw_game(screen, font, small_font, big_font, state)
            draw_game_over(screen, font, big_font, state)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()

