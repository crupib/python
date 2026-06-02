# sun_tzu_hex_modular/scenarios.py

from constants import MAP_COLS, MAP_ROWS
from models import Tile, Unit, Principle, Scenario


def make_base_tiles(state):
    state.tiles = {(q, r): Tile(q, r, "plain") for q in range(MAP_COLS) for r in range(MAP_ROWS)}


def finalize_setup(state, turn, phase, message, deployment_points=6, logistics=100):
    state.selected = None
    state.turn = turn
    state.phase = phase
    state.message = message
    state.assessment_points = 3
    state.deployment_points = deployment_points
    state.player_morale = 100
    state.enemy_morale = 100
    state.logistics = logistics
    state.turn_number = 0


def setup_gaugamela(state):
    make_base_tiles(state)
    for (q, r), tile in state.tiles.items():
        if 8 <= q <= 13 and 3 <= r <= 8:
            tile.terrain = "prepared"
        if q >= 12 and r <= 3:
            tile.terrain = "rough"
        if q <= 2 and 4 <= r <= 7:
            tile.terrain = "supply"
        if q <= 6:
            tile.revealed = True

    state.units = [
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
    finalize_setup(state, "Macedon", "DEPLOY", "Gaugamela deployment. Scout, redeploy, feint right, then press B.")


def setup_austerlitz(state):
    make_base_tiles(state)
    for (q, r), tile in state.tiles.items():
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

    state.units = [
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
    finalize_setup(state, "France", "DEPLOY", "Austerlitz deployment. Look weak, lure the enemy, then strike the Pratzen Heights.")


def setup_normaninv(state):
    make_base_tiles(state)
    for (q, r), tile in state.tiles.items():
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
        if q == 6 and 3 <= r <= 8:
            tile.terrain = "river"
        if q in [6, 7] and r in [2, 8]:
            tile.terrain = "bridge"
        if q in [8, 9] and r in [1, 10]:
            tile.terrain = "forest"
        if q in [10, 11] and r in [2, 5]:
            tile.terrain = "city"
        if q in [6, 7, 8] and r == 6:
            tile.terrain = "road"
        if q <= 5:
            tile.revealed = True

    state.units = [
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
    finalize_setup(state, "Allies", "DEPLOY", "Normandy deployment. Scout defenses, coordinate airborne drops, naval fire, and beach logistics.", deployment_points=8, logistics=125)


def setup_sixdaywar(state):
    make_base_tiles(state)
    for (q, r), tile in state.tiles.items():
        if 4 <= q <= 13 and 2 <= r <= 9:
            tile.terrain = "desert"
        if q in [10, 13] and r in [3, 6, 8]:
            tile.terrain = "airfield"
        if q >= 12 and r in [4, 7]:
            tile.terrain = "objective"
        if q <= 2 and 4 <= r <= 7:
            tile.terrain = "supply"
        if q in [6, 7, 8] and r in [4, 5, 6]:
            tile.terrain = "road"
        if q in [9, 12] and r in [4, 7]:
            tile.terrain = "city"
        if q in [8, 9] and r in [2, 9]:
            tile.terrain = "rough"
        if q <= 5:
            tile.revealed = True

    state.units = [
        Unit("Israeli Command", "Israel", 1, 5, 12, 3, 2, 1, "commander"),
        Unit("Mirage Squadron", "Israel", 2, 4, 9, 6, 5, 4, "aircraft"),
        Unit("Vautour Squadron", "Israel", 2, 6, 9, 5, 5, 4, "aircraft"),
        Unit("7th Armored", "Israel", 3, 5, 13, 5, 4, 1, "armor"),
        Unit("Paratroop Brigade", "Israel", 3, 7, 10, 4, 3, 1, "paratrooper"),
        Unit("Mechanized Infantry", "Israel", 3, 4, 11, 4, 3, 1, "mechanized"),
        Unit("Mobile Artillery", "Israel", 2, 7, 8, 3, 2, 3, "artillery"),
        Unit("Egyptian Command", "Egypt", 14, 5, 10, 2, 2, 1, "commander", hidden=True),
        Unit("Egyptian Airfield", "Egypt", 12, 4, 12, 3, 0, 3, "aircraft", hidden=True),
        Unit("Forward Airbase", "Egypt", 10, 6, 10, 3, 0, 3, "aircraft", hidden=True),
        Unit("SAM Battery", "Egypt", 11, 5, 10, 4, 1, 3, "airdefense", hidden=True),
        Unit("Sinai Armor", "Egypt", 13, 7, 13, 5, 3, 1, "armor", hidden=True),
        Unit("Infantry Line", "Egypt", 11, 8, 11, 3, 1, 1, "infantry", hidden=True),
        Unit("Reserve Artillery", "Egypt", 13, 3, 8, 3, 1, 3, "artillery", hidden=True),
    ]
    finalize_setup(state, "Israel", "DEPLOY", "Six-Day War deployment. Use speed, air superiority, and economy of force to avoid attrition.", deployment_points=7, logistics=120)


def register_content(state):
    state.principles = [
        Principle("principle1", "1. Laying Plans / Strategic Assessment", "Know the terrain, enemy disposition, logistics, morale, timing, and likely enemy moves before committing."),
        Principle("principle2", "2. Waging War / Economy of Force", "Win quickly, avoid prolonged attrition, preserve resources, and use only the force required for decisive objectives."),
    ]
    state.scenarios = [
        Scenario("gaugamela", "principle1", "Gaugamela, 331 BC", "Alexander vs. Darius", "Scout prepared ground, read Persian cavalry, avoid chariots and elephants, then strike Darius.", "Macedon", "Persia", setup_gaugamela),
        Scenario("austerlitz", "principle1", "Austerlitz, 1805", "Napoleon vs. Third Coalition", "Appear weak on the right, lure the Coalition off the heights, then smash the exposed center.", "France", "Coalition", setup_austerlitz),
        Scenario("normaninv", "principle1", "Normandy Invasion, 1944", "Allied landings vs. German coastal defense", "Scout beach defenses, coordinate airborne drops, naval fire, armor, and supply.", "Allies", "Germany", setup_normaninv),
        Scenario("sixdaywar", "principle2", "Six-Day War, 1967", "Israel vs. Egyptian forces", "Achieve rapid objectives through air superiority, armor movement, and logistics preservation before attrition sets in.", "Israel", "Egypt", setup_sixdaywar),
    ]



