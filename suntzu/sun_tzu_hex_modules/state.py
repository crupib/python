# sun_tzu_hex_modular/state.py

class GameState:
    def __init__(self):
        self.tiles = {}
        self.units = []
        self.principles = []
        self.scenarios = []
        self.selected = None
        self.current_scenario = None
        self.selected_principle_index = 0
        self.dropdown_open = False
        self.screen_mode = "SCENARIO_SELECT"
        self.turn = ""
        self.phase = ""
        self.message = ""
        self.assessment_points = 3
        self.deployment_points = 6
        self.player_morale = 100
        self.enemy_morale = 100
        self.logistics = 100
        self.turn_number = 0
        self.game_over = None

    def go_to_scenario_select(self):
        self.screen_mode = "SCENARIO_SELECT"
        self.selected = None
        self.current_scenario = None
        self.turn = ""
        self.phase = ""
        self.message = ""
        self.assessment_points = 3
        self.deployment_points = 6
        self.player_morale = 100
        self.enemy_morale = 100
        self.logistics = 100
        self.turn_number = 0
        self.game_over = None

    def scenarios_for_selected_principle(self):
        principle_key = self.principles[self.selected_principle_index].key
        return [s for s in self.scenarios if s.principle_key == principle_key]



