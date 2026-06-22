import random
import pygame

from hex_utils import hex_distance, neighbors
from assets import load_unit_images_for_scenario


def get_unit_at(state, pos):
    for u in state.units:
        if u.hp > 0 and u.pos == pos:
            return u
    return None


def friendly_units(state, side):
    return [u for u in state.units if u.side == side and u.hp > 0]


def player_units(state):
    return friendly_units(state, state.current_scenario.player_side)


def ai_units(state):
    return friendly_units(state, state.current_scenario.enemy_side)


def reset_actions(state, side):
    for u in state.units:
        if u.side == side and u.hp > 0:
            u.acted = False


def start_scenario(state, scenario):
    state.dropdown_open = False
    state.current_scenario = scenario
    load_unit_images_for_scenario(scenario.key)
    scenario.setup_func(state)
    state.screen_mode = "GAME"


def reveal_around(state, pos, radius=2):
    revealed_count = 0
    for tile_pos, tile in state.tiles.items():
        if hex_distance(pos, tile_pos) <= radius:
            tile.revealed = True
    for unit in state.units:
        if unit.hidden and hex_distance(pos, unit.pos) <= radius:
            unit.hidden = False
            revealed_count += 1
    state.message = f"Scouting revealed {revealed_count} enemy formation(s)." if revealed_count else "Scouting improved terrain knowledge, but found no hidden formations."


def all_enemy_visible(state):
    return all(not u.hidden for u in ai_units(state))


def yorktown_escape_boats(state):
    return next((u for u in state.units if u.name == "Escape Boats" and u.hp > 0), None)


def yorktown_blockade_active(state):
    if state.current_scenario.key != "yorktown":
        return False
    fleets = [u for u in state.units if u.name.startswith("French Fleet") and u.hp > 0]
    active = any(state.tiles.get(u.pos) and state.tiles[u.pos].terrain == "blockade" for u in fleets)
    state.yorktown_blockade_active = active
    return active


def update_yorktown_blockade_status(state):
    if state.current_scenario.key != "yorktown":
        return ""
    if not hasattr(state, "yorktown_escape_progress"):
        state.yorktown_escape_progress = 0
    if yorktown_escape_boats(state) is None:
        state.yorktown_escape_progress = 0
        return "British escape boats destroyed. The naval escape route is closed."
    if yorktown_blockade_active(state):
        state.yorktown_escape_progress = max(0, state.yorktown_escape_progress - 1)
        return f"French blockade active. British escape pressure: {state.yorktown_escape_progress}/5."
    state.yorktown_escape_progress += 1
    return f"WARNING: French blockade broken. British escape pressure: {state.yorktown_escape_progress}/5."


def valid_deploy_preview(state, q, r):
    key = state.current_scenario.key
    if key == "normaninv":
        return q <= 3 or (4 <= q <= 5 and r in [2, 8])
    if key == "austerlitz":
        return q <= 5 and 3 <= r <= 9
    if key == "yorktown":
        return q <= 5 or (13 <= q <= 15 and 5 <= r <= 7)
    if key == "constantinople":
        return q <= 5 or (q == 12 and 4 <= r <= 6)
    return q <= 5


def valid_deploy_hex(state, pos):
    q, r = pos
    return pos in state.tiles and valid_deploy_preview(state, q, r) and not get_unit_at(state, pos)


def deploy_unit(state, unit, target):
    if state.deployment_points <= 0:
        state.message = "No deployment points left."
        return
    if unit.side != state.current_scenario.player_side:
        return
    if not valid_deploy_hex(state, target):
        state.message = "Invalid deployment hex."
        return
    unit.q, unit.r = target
    state.deployment_points -= 1
    state.message = f"{unit.name} redeployed. Deployment points left: {state.deployment_points}."


def move_unit(state, unit, target):
    if unit.acted:
        state.message = f"{unit.name} has already acted."
        return
    if target not in state.tiles:
        return
    if get_unit_at(state, target):
        state.message = "Tile occupied."
        return
    dist = hex_distance(unit.pos, target)
    if dist > unit.move:
        state.message = "Too far."
        return
    terrain = state.tiles[target].terrain
    extra_cost = 0
    if terrain in ["rough", "forest", "city", "bocage"] and unit.role in ["cavalry", "armor", "mechanized", "artillery"]:
        extra_cost += 1
    if terrain in ["river", "sea", "blockade"] and unit.role != "naval":
        state.message = "Only naval units can enter this water-control hex."
        return
    if dist + extra_cost > unit.move:
        state.message = "Terrain slows that unit."
        return
    unit.q, unit.r = target
    unit.acted = True
    state.logistics -= 2
    state.message = f"{unit.name} moved."


def attack_unit(state, attacker, defender):
    if attacker.acted:
        state.message = f"{attacker.name} has already acted."
        return
    if defender.hidden:
        state.message = "Cannot attack unrevealed enemy."
        return
    if hex_distance(attacker.pos, defender.pos) > attacker.range:
        state.message = "Target out of range."
        return

    key = state.current_scenario.key
    terrain = state.tiles[defender.pos].terrain
    terrain_bonus = 1 if terrain in ["rough", "heights", "village", "bocage", "bunker", "airfield", "objective", "forest", "city"] else 0
    bonus = 0

    if attacker.role == "artillery" and terrain in ["bunker", "city", "objective", "prepared"]:
        bonus += 2
    if attacker.role == "naval" and defender.role in ["naval", "bunker", "commander"]:
        bonus += 2
    if attacker.role == "aircraft" and defender.role in ["aircraft", "airdefense", "commander", "naval"]:
        bonus += 3
    if attacker.role == "cavalry" and defender.role in ["infantry", "skirmisher"]:
        bonus += 1
    if attacker.role == "skirmisher" and defender.role in ["artillery", "bunker", "elephant"]:
        bonus += 2
    if attacker.role == "guard" and terrain in ["city", "objective", "heights"]:
        bonus += 1

    scenario_bonus_roles = {
        "cannae": ["cavalry"],
        "kalka": ["cavalry", "skirmisher"],
        "cowpens": ["cavalry", "skirmisher"],
        "ulm": ["cavalry", "infantry"],
        "midway": ["aircraft"],
        "teutoburg": ["skirmisher", "infantry"],
        "redcliffs": ["naval"],
        "tenochitlan": ["naval", "skirmisher"],
    }
    if attacker.role in scenario_bonus_roles.get(key, []):
        bonus += 1
    if key == "yorktown" and attacker.role == "artillery" and yorktown_blockade_active(state):
        bonus += 2
    if key == "constantinople" and attacker.role == "artillery":
        bonus += 2
    if key == "redcliffs" and attacker.name.endswith("Fleet"):
        bonus += 2

    damage = max(1, attacker.atk + bonus + random.randint(-1, 2) - terrain_bonus)
    if all_enemy_visible(state) and attacker.side == state.current_scenario.player_side:
        damage += 1

    defender.hp -= damage
    attacker.acted = True

    if defender.hp <= 0:
        defender.hp = 0
        if defender.side == state.current_scenario.enemy_side:
            state.enemy_morale -= 15
        else:
            state.player_morale -= 15
        if key == "yorktown" and defender.name == "Escape Boats":
            state.enemy_morale -= 15
            state.yorktown_escape_progress = 0
        state.message = f"{attacker.name} destroyed {defender.name}!"
    else:
        state.message = f"{attacker.name} hit {defender.name} for {damage}."


def estimate_ai_intent(state):
    hints = {
        "gaugamela": "Persian cavalry pressures the wings. Reveal Darius, avoid chariots and elephants, then strike the center.",
        "normaninv": "German bunkers guard beach exits. Use naval fire, airborne disruption, and logistics before armor pushes inland.",
        "sixdaywar": "Speed is decisive. Use aircraft first, then armor and mechanized forces to seize objectives quickly.",
        "austerlitz": "Appear weak, let the Coalition overextend, then strike the Pratzen Heights with reserves.",
        "yorktown": "Keep French naval units on blockade hexes. If blockade breaks, British escape pressure rises to 5/5.",
        "constantinople": "Use bombards and sappers to weaken walls before committing Janissaries and fleet pressure.",
        "cannae": "The Roman mass is dangerous frontally. Hold center, destroy cavalry, then envelop.",
        "kalka": "Use feigned retreat and mobile fire to exhaust pursuit before the counterstroke.",
        "cowpens": "Let the enemy hit the screen, then counterattack with cavalry and regulars.",
        "ulm": "Seize roads and bridges. Trap the enemy commander through maneuver, not attrition.",
        "midway": "Find and strike carriers. Aircraft are decisive; preserve carrier screen.",
        "teutoburg": "Use forest and road disorder. Attack marching units before they form.",
        "thermopylae": "Hold chokepoints. Terrain is your force multiplier.",
        "stalingrad": "City fighting favors endurance. Encircle and destroy command cohesion.",
        "redcliffs": "Fire ships and naval shock are decisive against chained formations.",
        "tenochitlan": "Use allies, scouts, causeways, and naval control to isolate the city.",
    }
    state.message = hints.get(state.current_scenario.key, "Enemy intent unclear.")


def special_feint(state):
    if state.phase == "DEPLOY":
        if state.deployment_points <= 0:
            state.message = "No deployment points left."
            return
        state.deployment_points -= 1
    else:
        if state.assessment_points <= 0:
            state.message = "No assessment points left."
            return
        state.assessment_points -= 1

    key = state.current_scenario.key
    for enemy in ai_units(state):
        if random.random() < 0.65:
            enemy.hidden = False
            if key in ["sixdaywar", "constantinople", "redcliffs"]:
                enemy.hp = max(1, enemy.hp - 1)
    if key == "yorktown":
        report = update_yorktown_blockade_status(state)
        state.enemy_morale -= 5
        state.message = f"Seal the Bay executed. Naval control reveals British escape options. {report}"
    else:
        state.enemy_morale -= 4
        state.logistics = min(state.logistics + 3, 135)
        state.message = "Scenario stratagem executed. Enemy posture is disrupted and some formations are revealed."


def ai_turn(state):
    enemies = ai_units(state)
    players = player_units(state)
    key = state.current_scenario.key

    for enemy in enemies:
        if enemy.hidden and any(hex_distance(enemy.pos, p.pos) <= 2 for p in players):
            enemy.hidden = False
        if enemy.hp <= 0:
            continue

        targets = [p for p in players if p.hp > 0]
        if not targets:
            break

        if key in ["midway", "redcliffs", "tenochitlan", "yorktown", "constantinople"]:
            priority = [p for p in targets if p.role in ["naval", "aircraft", "artillery", "commander"]]
            target = min(priority or targets, key=lambda p: hex_distance(enemy.pos, p.pos))
        else:
            target = min(targets, key=lambda p: hex_distance(enemy.pos, p.pos))

        if hex_distance(enemy.pos, target.pos) <= enemy.range and not enemy.acted:
            attack_unit(state, enemy, target)
            continue

        candidates = [c for c in neighbors(enemy.q, enemy.r) if c in state.tiles and not get_unit_at(state, c)]
        if not candidates:
            continue

        if enemy.role == "naval":
            candidates.sort(key=lambda c: (0 if state.tiles[c].terrain in ["sea", "river", "blockade"] else 5, hex_distance(c, target.pos)))
        elif enemy.role in ["cavalry", "armor", "mechanized"]:
            candidates.sort(key=lambda c: (hex_distance(c, target.pos), 0 if state.tiles[c].terrain in ["plain", "desert", "road"] else 1))
        elif enemy.role == "commander":
            player_commander = next((p for p in targets if p.role == "commander"), None)
            candidates.sort(key=lambda c: -hex_distance(c, player_commander.pos) if player_commander else hex_distance(c, target.pos))
        else:
            candidates.sort(key=lambda c: hex_distance(c, target.pos))

        enemy.q, enemy.r = candidates[0]
        enemy.acted = True

    reset_actions(state, state.current_scenario.enemy_side)
    reset_actions(state, state.current_scenario.player_side)

    state.turn = state.current_scenario.player_side
    state.phase = "ASSESS"
    state.assessment_points = 3
    state.logistics -= 4
    state.turn_number += 1
    state.message = "New turn. Assess before committing."

    blockade_report = update_yorktown_blockade_status(state)
    if blockade_report:
        state.message = f"{state.message} {blockade_report}"


def begin_battle(state):
    state.phase = "ASSESS"
    state.turn_number = 1
    state.assessment_points = 3
    state.message = "Battle begins. Assess the field, then commit your attack."


def end_player_turn(state):
    if state.phase == "DEPLOY":
        state.message = "Press B to begin battle after deployment."
        return
    state.turn = state.current_scenario.enemy_side
    state.phase = "AI"
    state.message = "Enemy AI is moving..."
    pygame.time.set_timer(pygame.USEREVENT, 500)


def check_victory(state):
    commanders = [u for u in state.units if u.role == "commander"]
    player_commander = next((u for u in commanders if u.side == state.current_scenario.player_side), None)
    enemy_commander = next((u for u in commanders if u.side == state.current_scenario.enemy_side), None)

    if player_commander is None or player_commander.hp <= 0:
        return f"{state.current_scenario.enemy_side} wins. Your commander has fallen."
    if enemy_commander is None or enemy_commander.hp <= 0:
        return f"{state.current_scenario.player_side} wins. Enemy commander is routed."
    if state.enemy_morale <= 0:
        return f"{state.current_scenario.player_side} wins. Enemy morale collapses."
    if state.player_morale <= 0:
        return f"{state.current_scenario.enemy_side} wins. Your morale collapses."
    if state.logistics <= 0:
        return f"{state.current_scenario.enemy_side} wins. Your logistics are exhausted."

    key = state.current_scenario.key
    if key == "sixdaywar" and state.turn_number > 8:
        return f"{state.current_scenario.enemy_side} wins. The war dragged into attrition."
    if key == "yorktown":
        if getattr(state, "yorktown_escape_progress", 0) >= 5:
            return f"{state.current_scenario.enemy_side} wins. Cornwallis escapes because the French blockade failed."
        redoubts_alive = any(u.hp > 0 and u.name in ["Redoubt 9", "Redoubt 10"] for u in state.units)
        if yorktown_blockade_active(state) and yorktown_escape_boats(state) is None and not redoubts_alive:
            return f"{state.current_scenario.player_side} wins. Cornwallis is trapped by land siege and French naval blockade."
        if state.turn_number > 12:
            return f"{state.current_scenario.enemy_side} wins. Cornwallis escapes before the trap fully closes."
    if key == "constantinople" and state.turn_number > 10:
        return f"{state.current_scenario.enemy_side} wins. The siege stalls and the defenders hold the city."
    if key in ["cannae", "kalka", "cowpens", "ulm", "midway", "teutoburg", "thermopylae", "stalingrad", "redcliffs", "tenochitlan"] and state.turn_number > 12:
        return f"{state.current_scenario.enemy_side} wins. You failed to achieve the principle's decisive condition in time."

    return None


from constants import MAP_COLS, MAP_ROWS
from models import Tile, Unit, Principle, Scenario


def make_base_tiles(state):
    state.tiles = {}
    for q in range(MAP_COLS):
        for r in range(MAP_ROWS):
            state.tiles[(q, r)] = Tile(q, r, "plain")


def reveal_left(state, max_q=6):
    for (q, r), tile in state.tiles.items():
        if q <= max_q:
            tile.revealed = True


def finalize_setup(
    state,
    player_side,
    message,
    deployment_points=6,
    assessment_points=3,
    player_morale=100,
    enemy_morale=100,
    logistics=105,
):
    state.selected = None
    state.turn = player_side
    state.phase = "DEPLOY"
    state.message = message
    state.assessment_points = assessment_points
    state.deployment_points = deployment_points
    state.player_morale = player_morale
    state.enemy_morale = enemy_morale
    state.logistics = logistics
    state.turn_number = 0


def set_terrain_rect(state, terrain, q_min, q_max, r_min, r_max):
    for q in range(q_min, q_max + 1):
        for r in range(r_min, r_max + 1):
            if (q, r) in state.tiles:
                state.tiles[(q, r)].terrain = terrain


def set_terrain_points(state, terrain, points):
    for point in points:
        if point in state.tiles:
            state.tiles[point].terrain = terrain


def setup_gaugamela(state):
    make_base_tiles(state)
    set_terrain_rect(state, "prepared", 8, 13, 3, 8)
    set_terrain_rect(state, "rough", 12, 16, 0, 3)
    set_terrain_rect(state, "supply", 0, 2, 4, 7)
    reveal_left(state, 6)

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
    finalize_setup(state, "Macedon", "Gaugamela deployment. Scout, redeploy, feint right, then press B.", 6, logistics=100)


def setup_normaninv(state):
    make_base_tiles(state)
    set_terrain_rect(state, "sea", 0, 1, 0, MAP_ROWS - 1)
    set_terrain_rect(state, "beach", 2, 4, 0, MAP_ROWS - 1)
    set_terrain_rect(state, "supply", 5, 6, 3, 8)
    set_terrain_rect(state, "bocage", 7, 11, 2, 9)
    set_terrain_points(state, "bunker", [(12, 3), (12, 6), (12, 8), (13, 6)])
    set_terrain_rect(state, "village", 10, 16, 0, 2)
    set_terrain_rect(state, "rough", 10, 16, 9, 11)
    set_terrain_rect(state, "river", 6, 6, 3, 8)
    set_terrain_points(state, "bridge", [(6, 2), (7, 2), (6, 8), (7, 8)])
    set_terrain_points(state, "forest", [(8, 1), (9, 1), (8, 10), (9, 10)])
    set_terrain_points(state, "city", [(10, 2), (11, 2), (10, 5), (11, 5)])
    set_terrain_points(state, "road", [(6, 6), (7, 6), (8, 6)])
    reveal_left(state, 5)

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
    finalize_setup(state, "Allies", "Normandy deployment. Scout defenses, coordinate airborne drops, naval fire, armor, and beach logistics.", 8, logistics=125)


def setup_sixdaywar(state):
    make_base_tiles(state)
    set_terrain_rect(state, "desert", 4, 13, 2, 9)
    set_terrain_points(state, "airfield", [(10, 3), (10, 6), (10, 8), (13, 3), (13, 6), (13, 8)])
    set_terrain_points(state, "objective", [(12, 4), (12, 7), (13, 4), (13, 7)])
    set_terrain_rect(state, "supply", 0, 2, 4, 7)
    set_terrain_points(state, "road", [(6, 4), (7, 4), (8, 4), (6, 5), (7, 5), (8, 5), (6, 6), (7, 6), (8, 6)])
    set_terrain_points(state, "city", [(9, 4), (9, 7), (12, 4), (12, 7)])
    set_terrain_points(state, "rough", [(8, 2), (9, 2), (8, 9), (9, 9)])
    reveal_left(state, 5)

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
    finalize_setup(state, "Israel", "Six-Day War deployment. Use speed, air superiority, and economy of force to avoid attrition.", 7, logistics=120)


def setup_austerlitz(state):
    make_base_tiles(state)
    set_terrain_rect(state, "heights", 7, 11, 3, 6)
    set_terrain_rect(state, "frozen", 10, 16, 7, 11)
    set_terrain_rect(state, "village", 5, 6, 5, 7)
    set_terrain_rect(state, "supply", 0, 2, 4, 8)
    reveal_left(state, 6)

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
    finalize_setup(state, "France", "Austerlitz stratagem deployment. Appear weak, lure the Allies forward, then strike the Pratzen center.", 6, logistics=100)


def setup_yorktown(state):
    make_base_tiles(state)
    set_terrain_rect(state, "supply", 0, 3, 4, 7)
    set_terrain_points(state, "forest", [(4, 2), (5, 2), (4, 9), (5, 9)])
    set_terrain_rect(state, "prepared", 5, 7, 2, 9)
    set_terrain_rect(state, "city", 8, 9, 3, 8)
    set_terrain_rect(state, "river", 10, 12, 3, 8)
    set_terrain_rect(state, "sea", 13, 16, 0, 11)
    set_terrain_rect(state, "blockade", 13, 15, 5, 7)
    set_terrain_points(state, "bridge", [(10, 4), (11, 4), (10, 7), (11, 7)])
    set_terrain_points(state, "road", [(5, 6), (6, 6), (7, 6), (8, 6)])
    set_terrain_points(state, "bunker", [(8, 4), (9, 4), (8, 7), (9, 7)])
    set_terrain_points(state, "objective", [(9, 5), (10, 5)])
    reveal_left(state, 6)
    for tile in state.tiles.values():
        if tile.terrain == "blockade":
            tile.revealed = True

    state.units = [
        Unit("Washington", "Allies", 2, 5, 12, 3, 2, 1, "commander"),
        Unit("Rochambeau", "Allies", 2, 6, 11, 3, 2, 1, "commander"),
        Unit("Continental Infantry", "Allies", 3, 5, 12, 4, 2, 1, "infantry"),
        Unit("French Infantry", "Allies", 3, 6, 12, 4, 2, 1, "infantry"),
        Unit("Siege Artillery", "Allies", 4, 5, 9, 5, 1, 3, "artillery"),
        Unit("Light Infantry", "Allies", 4, 7, 9, 4, 3, 1, "skirmisher"),
        Unit("French Fleet Center", "Allies", 14, 6, 12, 5, 2, 4, "naval"),
        Unit("French Fleet North", "Allies", 14, 5, 10, 4, 2, 3, "naval"),
        Unit("French Fleet South", "Allies", 14, 7, 10, 4, 2, 3, "naval"),
        Unit("Cornwallis", "Britain", 9, 5, 10, 2, 2, 1, "commander", hidden=True),
        Unit("Yorktown Garrison", "Britain", 9, 6, 14, 3, 1, 1, "infantry", hidden=True),
        Unit("Redoubt 9", "Britain", 8, 4, 10, 4, 0, 3, "bunker", hidden=True),
        Unit("Redoubt 10", "Britain", 9, 7, 10, 4, 0, 3, "bunker", hidden=True),
        Unit("British Artillery", "Britain", 10, 5, 8, 4, 1, 3, "artillery", hidden=True),
        Unit("Cavalry Screen", "Britain", 8, 8, 8, 3, 4, 1, "cavalry", hidden=True),
        Unit("Escape Boats", "Britain", 12, 6, 8, 2, 2, 1, "naval", hidden=True),
    ]
    finalize_setup(state, "Allies", "Yorktown deployment. Keep French naval units on the blockade line, reduce the redoubts, and prevent British escape.", 7, logistics=115)
    state.yorktown_escape_progress = 0
    state.yorktown_blockade_active = True


def setup_constantinople(state):
    make_base_tiles(state)
    set_terrain_rect(state, "supply", 0, 2, 0, 11)
    set_terrain_rect(state, "prepared", 3, 5, 3, 8)
    set_terrain_rect(state, "bunker", 6, 7, 3, 8)
    set_terrain_rect(state, "city", 8, 10, 3, 8)
    set_terrain_rect(state, "sea", 12, 16, 0, 11)
    set_terrain_points(state, "forest", [(4, 2), (5, 2), (6, 2), (4, 9), (5, 9), (6, 9)])
    set_terrain_points(state, "road", [(5, 6), (6, 6), (7, 6), (8, 6)])
    set_terrain_points(state, "objective", [(7, 4), (8, 4), (7, 7), (8, 7)])
    set_terrain_points(state, "bridge", [(11, 4), (12, 4), (11, 7), (12, 7)])
    reveal_left(state, 6)

    state.units = [
        Unit("Mehmed II", "Ottomans", 2, 5, 12, 3, 2, 1, "commander"),
        Unit("Janissaries", "Ottomans", 3, 5, 13, 5, 2, 1, "guard"),
        Unit("Anatolian Infantry", "Ottomans", 3, 6, 12, 4, 2, 1, "infantry"),
        Unit("Rumelian Infantry", "Ottomans", 3, 4, 12, 4, 2, 1, "infantry"),
        Unit("Great Bombard", "Ottomans", 4, 5, 10, 6, 1, 4, "artillery"),
        Unit("Sappers", "Ottomans", 4, 7, 8, 3, 2, 1, "skirmisher"),
        Unit("Ottoman Fleet", "Ottomans", 12, 5, 10, 4, 2, 3, "naval"),
        Unit("Constantine XI", "Byzantines", 9, 5, 10, 3, 2, 1, "commander", hidden=True),
        Unit("Theodosian Walls", "Byzantines", 7, 5, 16, 4, 0, 3, "bunker", hidden=True),
        Unit("Gate Defenders", "Byzantines", 8, 6, 12, 4, 1, 1, "guard", hidden=True),
        Unit("Genoese Guard", "Byzantines", 8, 4, 11, 4, 1, 1, "infantry", hidden=True),
        Unit("Greek Fire Ships", "Byzantines", 12, 6, 9, 4, 2, 3, "naval", hidden=True),
        Unit("City Militia", "Byzantines", 9, 7, 10, 3, 1, 1, "infantry", hidden=True),
        Unit("Wall Artillery", "Byzantines", 7, 7, 8, 3, 0, 3, "artillery", hidden=True),
    ]
    finalize_setup(state, "Ottomans", "Constantinople deployment. Use bombardment, engineering, fleet pressure, and psychological shock to break the city.", 7, enemy_morale=110, logistics=120)


def setup_generic(state, key, player, enemy, message, theme):
    make_base_tiles(state)
    set_terrain_rect(state, "supply", 0, 2, 4, 7)
    reveal_left(state, 6)

    if theme == "open_envelopment":
        set_terrain_rect(state, "prepared", 6, 9, 3, 8)
        set_terrain_rect(state, "objective", 12, 14, 4, 7)
    elif theme == "river_maneuver":
        set_terrain_rect(state, "river", 7, 8, 2, 9)
        set_terrain_points(state, "bridge", [(7, 4), (8, 4), (7, 7), (8, 7)])
        set_terrain_points(state, "road", [(5, 6), (6, 6), (9, 6), (10, 6)])
    elif theme == "forest_ambush":
        set_terrain_rect(state, "forest", 4, 13, 2, 9)
        set_terrain_rect(state, "road", 5, 10, 6, 6)
        set_terrain_points(state, "rough", [(7, 4), (8, 5), (9, 6), (10, 7)])
    elif theme == "chokepoint":
        set_terrain_rect(state, "rough", 6, 8, 2, 9)
        set_terrain_points(state, "bridge", [(8, 4), (8, 5), (8, 6)])
        set_terrain_points(state, "heights", [(5, 3), (6, 3), (5, 8), (6, 8)])
    elif theme == "urban_encirclement":
        set_terrain_rect(state, "city", 5, 11, 2, 9)
        set_terrain_rect(state, "river", 4, 4, 3, 8)
        set_terrain_rect(state, "river", 12, 12, 3, 8)
    elif theme == "fire_naval":
        set_terrain_rect(state, "river", 4, 13, 3, 8)
        set_terrain_points(state, "objective", [(6, 4), (8, 5), (10, 6)])
    elif theme == "island_city":
        set_terrain_rect(state, "river", 6, 8, 2, 9)
        set_terrain_points(state, "bridge", [(6, 4), (7, 6), (8, 8)])
        set_terrain_rect(state, "city", 9, 12, 3, 8)
    elif theme == "carrier_battle":
        for tile in state.tiles.values():
            tile.terrain = "sea"
        set_terrain_rect(state, "airfield", 0, 2, 4, 7)
        set_terrain_points(state, "objective", [(6, 4), (6, 6), (6, 8)])
        reveal_left(state, 6)

    state.units = [
        Unit(f"{player} Commander", player, 2, 5, 12, 4, 2, 1, "commander"),
        Unit(f"{player} Infantry", player, 3, 5, 12, 4, 2, 1, "infantry"),
        Unit(f"{player} Cavalry", player, 3, 4, 10, 4, 4, 1, "cavalry"),
        Unit(f"{player} Skirmishers", player, 3, 7, 8, 3, 2, 2, "skirmisher"),
        Unit(f"{player} Artillery", player, 2, 6, 8, 4, 1, 3, "artillery"),
        Unit(f"{enemy} Commander", enemy, 14, 5, 10, 3, 2, 1, "commander", hidden=True),
        Unit(f"{enemy} Infantry", enemy, 12, 5, 13, 4, 2, 1, "infantry", hidden=True),
        Unit(f"{enemy} Reserve", enemy, 12, 7, 11, 4, 2, 1, "infantry", hidden=True),
        Unit(f"{enemy} Cavalry", enemy, 13, 4, 9, 3, 3, 1, "cavalry", hidden=True),
        Unit(f"{enemy} Artillery", enemy, 13, 6, 8, 3, 1, 3, "artillery", hidden=True),
    ]

    if theme in ["carrier_battle", "fire_naval", "island_city"]:
        state.units.extend([
            Unit(f"{player} Fleet", player, 2, 6, 10, 4, 3, 3, "naval"),
            Unit(f"{enemy} Fleet", enemy, 12, 6, 10, 4, 3, 3, "naval", hidden=True),
        ])

    if theme == "carrier_battle":
        state.units.extend([
            Unit(f"{player} Air Group", player, 2, 4, 9, 6, 5, 4, "aircraft"),
            Unit(f"{enemy} Air Group", enemy, 12, 4, 9, 6, 5, 4, "aircraft", hidden=True),
        ])

    finalize_setup(state, player, message, 7, logistics=110)


def setup_cannae(state):
    setup_generic(state, "cannae", "Carthage", "Rome", "Cannae deployment. Hold the center, preserve the wings, then envelop Rome.", "open_envelopment")


def setup_kalka(state):
    setup_generic(state, "kalka", "Mongols", "Rus Coalition", "Kalka River deployment. Use feigned retreat and sudden counterstroke.", "river_maneuver")


def setup_cowpens(state):
    setup_generic(state, "cowpens", "Patriots", "Britain", "Cowpens deployment. Draw the enemy forward through layered lines, then counterattack.", "open_envelopment")


def setup_ulm(state):
    setup_generic(state, "ulm", "France", "Austria", "Ulm deployment. Seize roads and crossings to trap the enemy through maneuver.", "river_maneuver")


def setup_midway(state):
    setup_generic(state, "midway", "US Navy", "Japan", "Midway deployment. Adapt rapidly and strike carriers at the decisive moment.", "carrier_battle")


def setup_teutoburg(state):
    setup_generic(state, "teutoburg", "Germanic Tribes", "Rome", "Teutoburg deployment. Strike an army on the march through forest and disorder.", "forest_ambush")


def setup_thermopylae(state):
    setup_generic(state, "thermopylae", "Greek Allies", "Persia", "Thermopylae deployment. Hold the narrow ground and make numbers irrelevant.", "chokepoint")


def setup_stalingrad(state):
    setup_generic(state, "stalingrad", "Soviets", "Germany", "Stalingrad deployment. Turn desperate ground into encirclement.", "urban_encirclement")


def setup_redcliffs(state):
    setup_generic(state, "redcliffs", "Wu-Shu Alliance", "Wei", "Red Cliffs deployment. Use fire, wind, and naval disruption to shatter a superior fleet.", "fire_naval")


def setup_tenochitlan(state):
    setup_generic(state, "tenochitlan", "Spanish Alliance", "Aztec Empire", "Tenochtitlan deployment. Use intelligence, allies, causeways, and naval control to isolate the city.", "island_city")


def register_content(state):
    state.principles = [
        Principle("principle1", "1. Laying Plans / Strategic Assessment", "Know terrain, enemy disposition, logistics, morale, timing, and likely enemy moves before committing."),
        Principle("principle2", "2. Waging War / Economy of Force", "Win quickly, avoid prolonged attrition, preserve resources, and use only the force required."),
        Principle("principle3", "3. Attack by Stratagem / Win Before Fighting", "Shape the battlefield before direct combat through deception, positioning, engineering, morale pressure, and blockade."),
        Principle("principle4", "4. Tactical Dispositions / Defensive Positioning", "Make defeat impossible first, then wait for the enemy to expose the opportunity for victory."),
        Principle("principle5", "5. Energy / Directed Force", "Use timing, momentum, reserves, and concentrated force to convert motion into decisive shock."),
        Principle("principle6", "6. Weak Points and Strong", "Avoid strength, strike weakness, and force the enemy to defend everywhere while you attack somewhere."),
        Principle("principle7", "7. Maneuvering", "Win through movement, speed, deception, and positional advantage before the enemy responds."),
        Principle("principle8", "8. Variation in Tactics", "Adapt to changing conditions and avoid repeating a stale plan."),
        Principle("principle9", "9. Army on the March", "Read movement, formation, terrain, and enemy behavior before battle is joined."),
        Principle("principle10", "10. Terrain", "Use ground, chokepoints, distance, and access routes as weapons."),
        Principle("principle11", "11. The Nine Situations", "Understand the army's psychological and strategic condition based on its situation."),
        Principle("principle12", "12. Attack by Fire", "Use fire, disruption, timing, and environmental shock to collapse enemy cohesion."),
        Principle("principle13", "13. Use of Spies / Intelligence", "Exploit intelligence, local knowledge, informants, deception, and reconnaissance."),
    ]

    state.scenarios = [
        Scenario("gaugamela", "principle1", "Gaugamela, 331 BC", "Alexander vs. Darius", "Scout prepared ground, read Persian cavalry, avoid chariots and elephants, then strike Darius.", "Macedon", "Persia", setup_gaugamela),
        Scenario("normaninv", "principle1", "Normandy Invasion, 1944", "Allied landings vs. German coastal defense", "Scout beach defenses, coordinate airborne drops, naval fire, armor, and supply.", "Allies", "Germany", setup_normaninv),
        Scenario("sixdaywar", "principle2", "Six-Day War, 1967", "Israel vs. Egyptian forces", "Achieve rapid objectives through air superiority, armor movement, and logistics preservation before attrition sets in.", "Israel", "Egypt", setup_sixdaywar),
        Scenario("austerlitz", "principle3", "Austerlitz, 1805", "Napoleon vs. Third Coalition", "Napoleon deliberately appeared weak to lure the Allies into a fatal attack against a prepared trap.", "France", "Coalition", setup_austerlitz),
        Scenario("yorktown", "principle3", "Yorktown, 1781", "Washington and Rochambeau vs. Cornwallis", "Keep the French blockade active, reduce redoubts with siege artillery, and prevent British escape.", "Allies", "Britain", setup_yorktown),
        Scenario("constantinople", "principle3", "Fall of Constantinople, 1453", "Mehmed II vs. Byzantine defenders", "Use bombards, sappers, fleet pressure, and morale shock to crack the city before the final assault.", "Ottomans", "Byzantines", setup_constantinople),
        Scenario("cannae", "principle4", "Cannae, 216 BC", "Hannibal vs. Rome", "Hold the center, preserve the wings, and envelop the Roman mass.", "Carthage", "Rome", setup_cannae),
        Scenario("kalka", "principle5", "Kalka River, 1223", "Subutai vs. Rus Coalition", "Directed energy through feigned retreat and sudden counterstroke.", "Mongols", "Rus Coalition", setup_kalka),
        Scenario("cowpens", "principle6", "Cowpens, 1781", "Daniel Morgan vs. Tarleton", "Layered defense exposes enemy weakness, then cavalry and regulars counterattack.", "Patriots", "Britain", setup_cowpens),
        Scenario("ulm", "principle7", "Ulm Campaign, 1805", "Napoleon vs. Mack", "Maneuver around the enemy, seize crossings, and force surrender through position.", "France", "Austria", setup_ulm),
        Scenario("midway", "principle8", "Midway, 1942", "US Navy vs. Imperial Japan", "Adapt to uncertainty, exploit timing, and strike carriers at the decisive moment.", "US Navy", "Japan", setup_midway),
        Scenario("teutoburg", "principle9", "Teutoburg Forest, AD 9", "Arminius vs. Varus", "Read an army on the march, use forest and disorder, and strike before it can form.", "Germanic Tribes", "Rome", setup_teutoburg),
        Scenario("thermopylae", "principle10", "Thermopylae, 480 BC", "Greek Allies vs. Persia", "Use terrain and narrow ground to neutralize overwhelming numbers.", "Greek Allies", "Persia", setup_thermopylae),
        Scenario("stalingrad", "principle11", "Stalingrad, 1942", "Soviets vs. Germany", "Turn desperate ground into encirclement and force the enemy into a fatal situation.", "Soviets", "Germany", setup_stalingrad),
        Scenario("redcliffs", "principle12", "Red Cliffs, 208", "Wu-Shu Alliance vs. Cao Cao", "Use fire ships, wind, and naval disruption to shatter a superior fleet.", "Wu-Shu Alliance", "Wei", setup_redcliffs),
        Scenario("tenochitlan", "principle13", "Siege of Tenochtitlan, 1521", "Spanish-Tlaxcalan Alliance vs. Aztec Empire", "Use intelligence, alliances, causeways, and naval control to isolate a powerful city.", "Spanish Alliance", "Aztec Empire", setup_tenochitlan),
    ]

