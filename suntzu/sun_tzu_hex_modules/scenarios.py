# sun_tzu_hex_modular/scenarios.py
from constants import MAP_COLS, MAP_ROWS
from models import Tile, Unit, Principle, Scenario


def make_base_tiles(state):
    state.tiles = {}

    for q in range(MAP_COLS):
        for r in range(MAP_ROWS):
            state.tiles[(q, r)] = Tile(q, r, "plain")


def setup_gaugamela(state):
    make_base_tiles(state)

    for pos, tile in state.tiles.items():
        q, r = pos

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

    state.selected = None
    state.turn = "Macedon"
    state.phase = "DEPLOY"
    state.message = "Gaugamela deployment. Scout, redeploy, feint right, then press B."
    state.assessment_points = 3
    state.deployment_points = 6
    state.player_morale = 100
    state.enemy_morale = 100
    state.logistics = 100
    state.turn_number = 0


def setup_austerlitz(state):
    make_base_tiles(state)

    for pos, tile in state.tiles.items():
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

    state.selected = None
    state.turn = "France"
    state.phase = "DEPLOY"
    state.message = "Austerlitz deployment. Look weak, lure the enemy, then strike the Pratzen Heights."
    state.assessment_points = 3
    state.deployment_points = 6
    state.player_morale = 100
    state.enemy_morale = 100
    state.logistics = 100
    state.turn_number = 0


def setup_normaninv(state):
    make_base_tiles(state)

    for pos, tile in state.tiles.items():
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

    state.selected = None
    state.turn = "Allies"
    state.phase = "DEPLOY"
    state.message = "Normandy deployment. Scout defenses, coordinate airborne drops, naval fire, and beach logistics."
    state.assessment_points = 3
    state.deployment_points = 8
    state.player_morale = 100
    state.enemy_morale = 100
    state.logistics = 125
    state.turn_number = 0


def setup_sixdaywar(state):
    make_base_tiles(state)

    for pos, tile in state.tiles.items():
        q, r = pos

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

    state.selected = None
    state.turn = "Israel"
    state.phase = "DEPLOY"
    state.message = "Six-Day War deployment. Use speed, air superiority, and economy of force to avoid attrition."
    state.assessment_points = 3
    state.deployment_points = 7
    state.player_morale = 100
    state.enemy_morale = 100
    state.logistics = 120
    state.turn_number = 0


def setup_yorktown(state):
    make_base_tiles(state)

    for pos, tile in state.tiles.items():
        q, r = pos

        if q >= 13:
            tile.terrain = "sea"
        elif q in [10, 11, 12] and 3 <= r <= 8:
            tile.terrain = "river"
        elif q in [8, 9] and 3 <= r <= 8:
            tile.terrain = "city"
        elif q in [6, 7] and 2 <= r <= 9:
            tile.terrain = "prepared"
        elif q in [4, 5] and r in [2, 9]:
            tile.terrain = "forest"
        elif q <= 3 and 4 <= r <= 7:
            tile.terrain = "supply"

        if q in [10, 11] and r in [4, 7]:
            tile.terrain = "bridge"

        if q in [5, 6, 7, 8] and r == 6:
            tile.terrain = "road"

        if q in [8, 9] and r in [4, 7]:
            tile.terrain = "bunker"

        if q in [9, 10] and r == 5:
            tile.terrain = "objective"

        if q <= 6:
            tile.revealed = True

    state.units = [
        Unit("Washington", "Allies", 2, 5, 12, 3, 2, 1, "commander"),
        Unit("Rochambeau", "Allies", 2, 6, 11, 3, 2, 1, "commander"),
        Unit("Continental Infantry", "Allies", 3, 5, 12, 4, 2, 1, "infantry"),
        Unit("French Infantry", "Allies", 3, 6, 12, 4, 2, 1, "infantry"),
        Unit("Siege Artillery", "Allies", 4, 5, 9, 5, 1, 3, "artillery"),
        Unit("Light Infantry", "Allies", 4, 7, 9, 4, 3, 1, "skirmisher"),
        Unit("French Fleet", "Allies", 13, 6, 12, 5, 2, 4, "naval"),

        Unit("Cornwallis", "Britain", 9, 5, 10, 2, 2, 1, "commander", hidden=True),
        Unit("Yorktown Garrison", "Britain", 9, 6, 14, 3, 1, 1, "infantry", hidden=True),
        Unit("Redoubt 9", "Britain", 8, 4, 10, 4, 0, 3, "bunker", hidden=True),
        Unit("Redoubt 10", "Britain", 9, 7, 10, 4, 0, 3, "bunker", hidden=True),
        Unit("British Artillery", "Britain", 10, 5, 8, 4, 1, 3, "artillery", hidden=True),
        Unit("Cavalry Screen", "Britain", 8, 8, 8, 3, 4, 1, "cavalry", hidden=True),
        Unit("Escape Boats", "Britain", 12, 6, 8, 2, 2, 1, "naval", hidden=True),
    ]

    state.selected = None
    state.turn = "Allies"
    state.phase = "DEPLOY"
    state.message = "Yorktown deployment. Trap Cornwallis with siege lines, fleet control, and coordinated pressure."
    state.assessment_points = 3
    state.deployment_points = 7
    state.player_morale = 100
    state.enemy_morale = 100
    state.logistics = 115
    state.turn_number = 0


def register_content(state):
    state.principles = [
        Principle(
            key="principle1",
            title="1. Laying Plans / Strategic Assessment",
            description="Know the terrain, enemy disposition, logistics, morale, timing, and likely enemy moves before committing.",
        ),
        Principle(
            key="principle2",
            title="2. Waging War / Economy of Force",
            description="Win quickly, avoid prolonged attrition, preserve resources, and use only the force required for decisive objectives.",
        ),
        Principle(
            key="principle3",
            title="3. Attack by Stratagem / Win Before Fighting",
            description="Shape the battlefield before direct combat. Use positioning, deception, alliances, and blockade to make victory inevitable.",
        ),
    ]

    state.scenarios = [
        Scenario(
            key="gaugamela",
            principle_key="principle1",
            title="Gaugamela, 331 BC",
            subtitle="Alexander vs. Darius",
            description="Scout prepared ground, read Persian cavalry, avoid chariots and elephants, then strike Darius.",
            player_side="Macedon",
            enemy_side="Persia",
            setup_func=setup_gaugamela,
        ),
        Scenario(
            key="austerlitz",
            principle_key="principle1",
            title="Austerlitz, 1805",
            subtitle="Napoleon vs. Third Coalition",
            description="Appear weak on the right, lure the Coalition off the heights, then smash the exposed center.",
            player_side="France",
            enemy_side="Coalition",
            setup_func=setup_austerlitz,
        ),
        Scenario(
            key="normaninv",
            principle_key="principle1",
            title="Normandy Invasion, 1944",
            subtitle="Allied landings vs. German coastal defense",
            description="Scout beach defenses, coordinate airborne drops, naval fire, armor, and supply.",
            player_side="Allies",
            enemy_side="Germany",
            setup_func=setup_normaninv,
        ),
        Scenario(
            key="sixdaywar",
            principle_key="principle2",
            title="Six-Day War, 1967",
            subtitle="Israel vs. Egyptian forces",
            description="Achieve rapid objectives through air superiority, armor movement, and logistics preservation before attrition sets in.",
            player_side="Israel",
            enemy_side="Egypt",
            setup_func=setup_sixdaywar,
        ),
        Scenario(
            key="yorktown",
            principle_key="principle3",
            title="Yorktown, 1781",
            subtitle="Washington and Rochambeau vs. Cornwallis",
            description="Strategic positioning traps Cornwallis. Use siege lines, French naval control, and coordinated pressure to win before a costly assault.",
            player_side="Allies",
            enemy_side="Britain",
            setup_func=setup_yorktown,
        ),
    ]
