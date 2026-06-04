# sun_tzu_hex_modular/logic.py
import random
import pygame

from constants import MAP_COLS, MAP_ROWS
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
    load_unit_images_for_scenario(state.current_scenario.key)
    state.current_scenario.setup_func(state)
    state.screen_mode = "GAME"


def reveal_around(state, pos, radius=2):
    revealed_count = 0

    for tile_pos, tile in state.tiles.items():
        if hex_distance(pos, tile_pos) <= radius:
            tile.revealed = True

    for u in state.units:
        if u.hidden and hex_distance(pos, u.pos) <= radius:
            u.hidden = False
            revealed_count += 1

    if revealed_count:
        state.message = f"Scouting revealed {revealed_count} enemy formation(s)."
    else:
        state.message = "Scouting improved terrain knowledge, but found no hidden formations."


def all_enemy_visible(state):
    return all(
        not u.hidden
        for u in state.units
        if u.side == state.current_scenario.enemy_side and u.hp > 0
    )



def yorktown_french_fleet(state):
    return next((u for u in state.units if u.name.startswith("French Fleet") and u.hp > 0), None)


def yorktown_escape_boats(state):
    return next((u for u in state.units if u.name == "Escape Boats" and u.hp > 0), None)


def yorktown_blockade_active(state):
    if state.current_scenario.key != "yorktown":
        return False

    fleet_units = [u for u in state.units if u.name.startswith("French Fleet") and u.hp > 0]
    active = any(state.tiles.get(u.pos) and state.tiles[u.pos].terrain == "blockade" for u in fleet_units)
    state.yorktown_blockade_active = active
    return active


def update_yorktown_blockade_status(state):
    if state.current_scenario.key != "yorktown":
        return ""

    if not hasattr(state, "yorktown_escape_progress"):
        state.yorktown_escape_progress = 0

    escape_boats = yorktown_escape_boats(state)

    if not escape_boats:
        state.yorktown_escape_progress = 0
        state.yorktown_blockade_active = True
        return "British escape boats destroyed. The naval escape route is closed."

    if yorktown_blockade_active(state):
        if state.yorktown_escape_progress > 0:
            state.yorktown_escape_progress -= 1
        return f"French blockade active. British escape pressure: {state.yorktown_escape_progress}/5."

    state.yorktown_escape_progress += 1
    return f"WARNING: French blockade broken. British escape pressure: {state.yorktown_escape_progress}/5."


def yorktown_siege_bonus_active(state):
    if state.current_scenario.key != "yorktown":
        return False

    return yorktown_blockade_active(state)

def valid_deploy_preview(state, q, r):
    if state.current_scenario.key == "gaugamela":
        return q <= 4

    if state.current_scenario.key == "austerlitz":
        return q <= 5 and 3 <= r <= 9

    if state.current_scenario.key == "normaninv":
        return q <= 3 or (4 <= q <= 5 and r in [2, 8])

    if state.current_scenario.key == "sixdaywar":
        return q <= 4

    if state.current_scenario.key == "yorktown":
        return q <= 5 or (13 <= q <= 15 and 5 <= r <= 7)

    if state.current_scenario.key == "constantinople":
        return q <= 5 or (q == 12 and 4 <= r <= 6)

    return False


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

    if terrain == "rough" and unit.role in ["cavalry", "chariot", "elephant", "armor", "mechanized"]:
        extra_cost += 1

    if terrain == "frozen" and unit.role in ["artillery", "infantry", "guard"]:
        extra_cost += 1

    if terrain == "bocage" and unit.role in ["armor", "infantry", "artillery"]:
        extra_cost += 1

    if terrain == "beach" and unit.role in ["armor", "artillery"]:
        extra_cost += 1

    if terrain == "desert" and unit.role in ["infantry", "artillery"]:
        extra_cost += 1

    if terrain == "forest" and unit.role in ["armor", "mechanized", "artillery"]:
        extra_cost += 1

    if terrain == "city" and unit.role in ["armor", "cavalry"]:
        extra_cost += 1

    if terrain == "river" and unit.role != "naval":
        state.message = "Use a bridge to cross river hexes."
        return

    if terrain == "sea" and unit.role != "naval":
        state.message = "Only naval units can enter sea hexes."
        return

    if unit.role == "elephant" and terrain == "rough":
        extra_cost += 1

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

    terrain_bonus = 0
    bonus = 0

    defender_tile = state.tiles[defender.pos]

    if defender_tile.terrain in [
        "rough", "heights", "village", "bocage", "bunker",
        "airfield", "objective", "forest", "city",
    ]:
        terrain_bonus += 1

    if attacker.role == "chariot" and defender.role == "phalanx":
        terrain_bonus += 2

    if attacker.role == "elephant" and defender.role == "cavalry":
        bonus += 2

    if attacker.role == "skirmisher" and defender.role == "elephant":
        bonus += 3

    if attacker.role == "phalanx" and defender.role == "elephant":
        bonus += 1

    if state.current_scenario.key == "austerlitz":
        if attacker.side == state.current_scenario.player_side and defender_tile.terrain == "heights":
            bonus += 1
        if attacker.role == "guard" and defender.role in ["infantry", "commander"]:
            bonus += 1

    if state.current_scenario.key == "normaninv":
        if attacker.role == "naval" and defender_tile.terrain in ["bunker", "beach"]:
            bonus += 2
        if attacker.role == "paratrooper" and defender.role in ["artillery", "bunker"]:
            bonus += 2
        if attacker.role == "armor" and defender_tile.terrain in ["bocage", "forest", "city"]:
            terrain_bonus += 1
        if attacker.role == "infantry" and defender_tile.terrain == "bunker":
            terrain_bonus += 1

    if state.current_scenario.key == "sixdaywar":
        if attacker.role == "aircraft" and defender.role in ["aircraft", "airdefense", "commander"]:
            bonus += 3
        if attacker.role == "armor" and defender_tile.terrain in ["desert", "objective"]:
            bonus += 1
        if attacker.role == "mechanized" and defender.role == "artillery":
            bonus += 2

    if state.current_scenario.key == "yorktown":
        if attacker.role == "artillery" and defender_tile.terrain in ["bunker", "prepared", "objective", "city"]:
            bonus += 2
            if state.current_scenario.key == "yorktown" and yorktown_siege_bonus_active(state):
                bonus += 2
        if attacker.role == "naval" and defender.role in ["naval", "commander"]:
            bonus += 2
        if attacker.role == "skirmisher" and defender.role in ["artillery", "bunker"]:
            bonus += 1
        if defender.role == "commander" and all_enemy_visible(state):
            bonus += 1

    if state.current_scenario.key == "constantinople":
        if attacker.role == "artillery" and defender_tile.terrain in ["bunker", "city", "objective"]:
            bonus += 3
        if attacker.role == "skirmisher" and defender.role in ["bunker", "artillery"]:
            bonus += 2
        if attacker.role == "naval" and defender.role == "naval":
            bonus += 2
        if attacker.role == "guard" and defender_tile.terrain in ["objective", "city"]:
            bonus += 1
        if defender.role == "bunker":
            terrain_bonus += 1

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

        state.message = f"{attacker.name} destroyed {defender.name}!"
    else:
        state.message = f"{attacker.name} hit {defender.name} for {damage}."


def estimate_ai_intent(state):
    hints = []

    if state.current_scenario.key == "gaugamela":
        if any(u.role == "chariot" and u.hp > 0 for u in ai_units(state)):
            hints.append("Chariots favor prepared plain. Pull them into poor ground or screen them.")
        if any(u.role == "elephant" and u.hp > 0 for u in ai_units(state)):
            hints.append("Elephants are slow shock units. Avoid cavalry contact; use skirmishers or phalanx.")
        if any(u.role == "cavalry" and u.hp > 0 for u in ai_units(state)):
            hints.append("Persian cavalry will pressure your wings.")

        darius = next((u for u in state.units if u.name == "Darius" and u.hp > 0), None)
        if darius and not darius.hidden:
            hints.append("Darius is visible. A center strike can collapse Persian morale.")

    elif state.current_scenario.key == "austerlitz":
        hints.append("The Coalition wants your right flank.")
        hints.append("Let them overextend, then strike the Pratzen Heights.")
        hints.append("Keep the Imperial Guard as a decisive reserve.")

    elif state.current_scenario.key == "normaninv":
        hints.append("German bunkers guard beach exits, towns, and bridges.")
        hints.append("Use naval fire and airborne disruption before pushing armor inland.")
        hints.append("Forests, bocage, and cities slow armor. Keep logistics near the beachhead.")

    elif state.current_scenario.key == "sixdaywar":
        hints.append("Speed is decisive. Destroy airfields and command nodes before prolonged attrition begins.")
        hints.append("Use aircraft first, then armor and mechanized forces to seize objectives quickly.")
        hints.append("Economy of force: avoid unnecessary attacks and keep logistics high.")

    elif state.current_scenario.key == "yorktown":
        hints.append("Yorktown is about blockade first: keep French naval units on blockade hexes.")
        hints.append("If the blockade breaks, British escape pressure rises each turn. At 5/5, Britain wins.")
        hints.append("With the blockade active, siege artillery gains extra power against redoubts and city defenses.")

    elif state.current_scenario.key == "constantinople":
        hints.append("The walls are strong, but morale is fragile.")
        hints.append("Use bombards and sappers to break defenses before committing Janissaries.")
        hints.append("Fleet pressure can reveal and disrupt Byzantine naval escape or relief options.")

    state.message = " ".join(hints) if hints else "Enemy intent unclear."


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

    if state.current_scenario.key == "gaugamela":
        alex = next((u for u in state.units if u.name == "Alexander" and u.hp > 0), None)
        cav = next((u for u in state.units if u.name == "Companion Cav" and u.hp > 0), None)

        for u in [alex, cav]:
            if u:
                target = (min(MAP_COLS - 1, u.q + 1), max(0, u.r - 1))
                if target in state.tiles and not get_unit_at(state, target):
                    u.q, u.r = target

        for p in ai_units(state):
            if p.role == "cavalry" and random.random() < 0.65:
                p.r = max(0, p.r - 1)
                p.hidden = False

        state.message = "Feint right executed. Persian cavalry shifts outward. Look for a center gap."

    elif state.current_scenario.key == "austerlitz":
        for enemy in ai_units(state):
            if enemy.role in ["infantry", "cavalry"] and random.random() < 0.7:
                enemy.q = max(0, enemy.q - 1)
                enemy.r = min(MAP_ROWS - 1, enemy.r + 1)
                enemy.hidden = False

        state.message = "False weakness shown on the right. Coalition forces overextend."

    elif state.current_scenario.key == "normaninv":
        for enemy in ai_units(state):
            if enemy.role in ["infantry", "armor"] and random.random() < 0.65:
                enemy.hidden = False
                enemy.q = min(MAP_COLS - 1, enemy.q + 1)

        state.message = "Deception and resistance reports confuse German reserves. Some enemy units reveal or delay."

    elif state.current_scenario.key == "sixdaywar":
        for enemy in ai_units(state):
            if enemy.role in ["aircraft", "commander", "airdefense"] and random.random() < 0.75:
                enemy.hidden = False
                enemy.hp -= 2
                state.enemy_morale -= 3

        state.logistics = min(state.logistics + 5, 140)
        state.message = "Preemptive air operation executed. Enemy air and command assets are disrupted."

    elif state.current_scenario.key == "yorktown":
        for enemy in ai_units(state):
            if enemy.role in ["commander", "naval", "artillery", "bunker"] and random.random() < 0.75:
                enemy.hidden = False

        state.enemy_morale -= 5
        state.logistics = min(state.logistics + 4, 130)
        blockade_report = update_yorktown_blockade_status(state)
        state.message = f"Stratagem executed. Siege lines tighten and French naval control reveals British escape options. {blockade_report}"

    elif state.current_scenario.key == "constantinople":
        for enemy in ai_units(state):
            if enemy.role in ["bunker", "commander", "artillery", "naval"] and random.random() < 0.75:
                enemy.hidden = False
                enemy.hp -= 1

        state.enemy_morale -= 7
        state.logistics = min(state.logistics + 3, 135)
        state.message = "Psychological and engineering pressure applied. Bombards, sappers, and fleet maneuvers shake the defense."


def ai_turn(state):
    enemies = ai_units(state)
    players = player_units(state)

    for e in enemies:
        if e.hidden:
            if any(hex_distance(e.pos, p.pos) <= 2 for p in players):
                e.hidden = False

        if e.hp <= 0:
            continue

        targets = [p for p in players if p.hp > 0]

        if not targets:
            break

        if state.current_scenario.key == "gaugamela" and e.role == "elephant":
            cavalry_targets = [p for p in targets if p.role == "cavalry"]
            target = min(cavalry_targets or targets, key=lambda p: hex_distance(e.pos, p.pos))

        elif state.current_scenario.key == "austerlitz" and e.role in ["infantry", "cavalry"]:
            right_flank = [p for p in targets if p.r >= 7]
            target = min(right_flank or targets, key=lambda p: hex_distance(e.pos, p.pos))

        elif state.current_scenario.key == "normaninv":
            beach_targets = [p for p in targets if state.tiles[p.pos].terrain in ["beach", "supply", "bridge"]]
            target = min(beach_targets or targets, key=lambda p: hex_distance(e.pos, p.pos))

        elif state.current_scenario.key == "sixdaywar":
            high_value = [p for p in targets if p.role in ["aircraft", "armor", "commander"]]
            target = min(high_value or targets, key=lambda p: hex_distance(e.pos, p.pos))

        elif state.current_scenario.key == "yorktown":
            siege_targets = [p for p in targets if p.role in ["artillery", "naval", "commander"]]
            target = min(siege_targets or targets, key=lambda p: hex_distance(e.pos, p.pos))

        elif state.current_scenario.key == "constantinople":
            high_value = [p for p in targets if p.role in ["artillery", "guard", "commander", "naval"]]
            target = min(high_value or targets, key=lambda p: hex_distance(e.pos, p.pos))

        else:
            target = min(targets, key=lambda p: hex_distance(e.pos, p.pos))

        if hex_distance(e.pos, target.pos) <= e.range and not e.acted:
            attack_unit(state, e, target)
            continue

        candidates = [c for c in neighbors(e.q, e.r) if c in state.tiles and not get_unit_at(state, c)]

        if not candidates:
            continue

        if e.role == "chariot":
            candidates.sort(key=lambda c: (hex_distance(c, target.pos), 0 if state.tiles[c].terrain == "prepared" else 1))
        elif e.role == "elephant":
            candidates.sort(key=lambda c: (10 if state.tiles[c].terrain == "rough" else 0, hex_distance(c, target.pos)))
        elif e.role in ["cavalry", "armor", "mechanized"]:
            candidates.sort(key=lambda c: (hex_distance(c, target.pos), 0 if state.tiles[c].terrain in ["plain", "desert", "road"] else 1))
        elif e.role == "naval":
            candidates.sort(key=lambda c: (0 if state.tiles[c].terrain in ["sea", "river", "blockade"] else 5, hex_distance(c, target.pos)))
        elif e.role == "commander":
            player_commander = next((p for p in players if p.role == "commander"), None)
            if player_commander:
                candidates.sort(key=lambda c: -hex_distance(c, player_commander.pos))
            else:
                candidates.sort(key=lambda c: hex_distance(c, target.pos))
        elif state.current_scenario.key == "normaninv" and e.role == "armor":
            candidates.sort(key=lambda c: (10 if state.tiles[c].terrain in ["bocage", "forest"] else 0, hex_distance(c, target.pos)))
        elif state.current_scenario.key == "yorktown":
            candidates.sort(key=lambda c: (
                0 if state.tiles[c].terrain in ["city", "bunker", "objective", "river"] else 1,
                hex_distance(c, target.pos),
            ))
        else:
            candidates.sort(key=lambda c: hex_distance(c, target.pos))

        e.q, e.r = candidates[0]
        e.acted = True

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

    if state.current_scenario.key == "sixdaywar" and state.turn_number > 8:
        return f"{state.current_scenario.enemy_side} wins. The war dragged into attrition."

    if state.current_scenario.key == "yorktown" and state.turn_number > 10:
        return f"{state.current_scenario.enemy_side} wins. Cornwallis escapes before the trap fully closes."

    return None

