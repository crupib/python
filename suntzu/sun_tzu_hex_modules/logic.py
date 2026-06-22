# sun_tzu_hex_modular/logic.py
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

