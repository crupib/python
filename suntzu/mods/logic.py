
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


def supply_status(state):
    if state.logistics >= 100:
        return "Supply excellent. You can support active operations."
    if state.logistics >= 80:
        return "Supply strong. Keep pressure but avoid waste."
    if state.logistics >= 50:
        return "Supply steady. Roads, bridges, and supply hexes will keep the army moving."
    if state.logistics >= 30:
        return "Supply low. Move units onto blue supply hexes or reduce movement."
    if state.logistics >= 15:
        return "Supply critical. Stop overextending and resupply immediately."
    return "Supply collapsing. You may lose soon unless units reach supply hexes."


def resupply_units(state):
    restored = 0
    supplied_units = []

    for unit in player_units(state):
        tile = state.tiles.get(unit.pos)
        if not tile:
            continue
        if tile.terrain == "supply":
            restored += 8
            supplied_units.append(unit.name)
        elif tile.terrain in ["road", "bridge"]:
            restored += 2
            supplied_units.append(unit.name)

    if restored <= 0:
        state.message = "No units are on supply, road, or bridge hexes. Move back toward blue supply areas, roads, or bridges."
        return

    old = state.logistics
    state.logistics = min(state.logistics + restored, 140)
    gained = state.logistics - old
    listed = ", ".join(supplied_units[:3])
    if len(supplied_units) > 3:
        listed += f", +{len(supplied_units) - 3} more"
    state.message = f"Resupplied +{gained} logistics from {listed}. {supply_status(state)}"


def reveal_around(state, pos, radius=2):
    revealed_count = 0
    for tile_pos, tile in state.tiles.items():
        if hex_distance(pos, tile_pos) <= radius:
            tile.revealed = True
    for u in state.units:
        if u.hidden and hex_distance(pos, u.pos) <= radius:
            u.hidden = False
            revealed_count += 1
    state.message = f"Scouting revealed {revealed_count} enemy formation(s)." if revealed_count else "Scouting improved terrain knowledge, but found no hidden formations."


def all_enemy_visible(state):
    return all(not u.hidden for u in state.units if u.side == state.current_scenario.enemy_side and u.hp > 0)


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
    if yorktown_escape_boats(state) is None:
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
    return state.current_scenario.key == "yorktown" and yorktown_blockade_active(state)


def valid_deploy_preview(state, q, r):
    key = state.current_scenario.key
    if key == "gaugamela": return q <= 4
    if key == "normaninv": return q <= 3 or (4 <= q <= 5 and r in [2, 8])
    if key == "sixdaywar": return q <= 4
    if key == "austerlitz": return q <= 5 and 3 <= r <= 9
    if key == "yorktown": return q <= 5 or (13 <= q <= 20 and 5 <= r <= 9)
    if key == "constantinople": return q <= 6 or (q >= 16 and 6 <= r <= 9)
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
    if terrain == "rough" and unit.role in ["cavalry", "chariot", "elephant", "armor", "mechanized"]: extra_cost += 1
    if terrain == "frozen" and unit.role in ["artillery", "infantry", "guard"]: extra_cost += 1
    if terrain == "bocage" and unit.role in ["armor", "infantry", "artillery"]: extra_cost += 1
    if terrain == "beach" and unit.role in ["armor", "artillery"]: extra_cost += 1
    if terrain == "desert" and unit.role in ["infantry", "artillery"]: extra_cost += 1
    if terrain == "forest" and unit.role in ["armor", "mechanized", "artillery"]: extra_cost += 1
    if terrain == "city" and unit.role in ["armor", "cavalry"]: extra_cost += 1
    if terrain == "river" and unit.role != "naval":
        state.message = "Use a bridge to cross river hexes."
        return
    if terrain == "blockade" and unit.role != "naval":
        state.message = "Only naval units can occupy blockade hexes."
        return
    if terrain == "sea" and unit.role != "naval":
        state.message = "Only naval units can enter sea hexes."
        return
    if dist + extra_cost > unit.move:
        state.message = "Terrain slows that unit."
        return

    unit.q, unit.r = target
    unit.acted = True
    state.logistics -= 1 if terrain in ["road", "bridge", "supply"] else 2
    state.message = f"{unit.name} moved."
    if state.logistics <= 30:
        state.message += f" {supply_status(state)} Press L to check supply or R to resupply."


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
    key = state.current_scenario.key
    if defender_tile.terrain in ["rough", "heights", "village", "bocage", "bunker", "airfield", "objective", "forest", "city"]:
        terrain_bonus += 1

    if attacker.role == "chariot" and defender.role == "phalanx": terrain_bonus += 2
    if attacker.role == "elephant" and defender.role == "cavalry": bonus += 2
    if attacker.role == "skirmisher" and defender.role == "elephant": bonus += 3
    if attacker.role == "phalanx" and defender.role == "elephant": bonus += 1
    if key == "austerlitz" and defender_tile.terrain == "heights": bonus += 1
    if key == "normaninv" and attacker.role == "naval" and defender_tile.terrain in ["bunker", "beach"]: bonus += 2
    if key == "sixdaywar" and attacker.role == "aircraft": bonus += 2
    if key == "yorktown":
        if attacker.role == "artillery" and defender_tile.terrain in ["bunker", "prepared", "objective", "city"]:
            bonus += 2
            if yorktown_siege_bonus_active(state): bonus += 2
        if attacker.role == "naval" and defender.role in ["naval", "commander"]: bonus += 3
        if attacker.name.startswith("French Fleet") and defender.name == "Escape Boats": bonus += 3
    if key == "constantinople" and attacker.role == "artillery" and defender_tile.terrain in ["bunker", "city", "objective"]: bonus += 3
    if key == "redcliffs" and attacker.name == "Fire Ships": bonus += 4

    damage = max(1, attacker.atk + bonus + random.randint(-1, 2) - terrain_bonus)
    if all_enemy_visible(state) and attacker.side == state.current_scenario.player_side:
        damage += 1
    defender.hp -= damage
    attacker.acted = True
    state.logistics -= 1

    if defender.hp <= 0:
        defender.hp = 0
        if defender.side == state.current_scenario.enemy_side:
            state.enemy_morale -= 15
        else:
            state.player_morale -= 15
        if key == "yorktown" and defender.name == "Escape Boats":
            state.enemy_morale -= 15
            if hasattr(state, "yorktown_escape_progress"):
                state.yorktown_escape_progress = 0
        state.message = f"{attacker.name} destroyed {defender.name}!"
    else:
        state.message = f"{attacker.name} hit {defender.name} for {damage}."
    if state.logistics <= 30:
        state.message += f" {supply_status(state)}"


def estimate_ai_intent(state):
    hints = {
        "gaugamela": "Persian cavalry pressures the wings. Reveal Darius, avoid chariots and elephants, then strike the center.",
        "normaninv": "German bunkers guard beach exits. Use naval fire, airborne disruption, and logistics before armor pushes inland.",
        "sixdaywar": "Speed is decisive. Use aircraft first, then armor and mechanized forces to seize objectives quickly.",
        "austerlitz": "Appear weak, let the Coalition overextend, then strike the Pratzen Heights with reserves.",
        "yorktown": "Keep French naval units on blockade hexes. If the blockade breaks, British escape pressure rises to 5/5.",
        "constantinople": "Use bombards and sappers to weaken walls before committing Janissaries and fleet pressure.",
    }
    state.message = hints.get(state.current_scenario.key, "Use the principle: reveal, disrupt, preserve supply, and strike the enemy commander.")


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
    for enemy in ai_units(state):
        if random.random() < 0.6:
            enemy.hidden = False
    state.enemy_morale -= 4
    state.logistics = min(state.logistics + 3, 140)
    if state.current_scenario.key == "yorktown":
        state.message = f"Seal the Bay executed. {update_yorktown_blockade_status(state)}"
    else:
        state.message = "Scenario special action executed. Enemy posture disrupted, some units revealed, logistics slightly improved."


def ai_turn(state):
    enemies = ai_units(state)
    players = player_units(state)
    for e in enemies:
        if e.hidden and any(hex_distance(e.pos, p.pos) <= 2 for p in players):
            e.hidden = False
        if e.hp <= 0:
            continue
        targets = [p for p in players if p.hp > 0]
        if not targets:
            break
        target = min(targets, key=lambda p: hex_distance(e.pos, p.pos))
        if hex_distance(e.pos, target.pos) <= e.range and not e.acted:
            attack_unit(state, e, target)
            continue
        candidates = [c for c in neighbors(e.q, e.r) if c in state.tiles and not get_unit_at(state, c)]
        if not candidates:
            continue
        if e.role == "naval":
            candidates.sort(key=lambda c: (0 if state.tiles[c].terrain in ["sea", "river", "blockade"] else 5, hex_distance(c, target.pos)))
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
    state.message = f"New turn. Assess before committing. {supply_status(state)}"
    blockade_report = update_yorktown_blockade_status(state)
    if blockade_report:
        state.message = f"{state.message} {blockade_report}"


def begin_battle(state):
    state.phase = "ASSESS"
    state.turn_number = 1
    state.assessment_points = 3
    state.message = f"Battle begins. Assess the field, then commit your attack. {supply_status(state)}"


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
    if state.current_scenario.key == "yorktown" and getattr(state, "yorktown_escape_progress", 0) >= 5:
        return f"{state.current_scenario.enemy_side} wins. Cornwallis escapes because the French blockade failed."
    if state.current_scenario.key == "sixdaywar" and state.turn_number > 8:
        return f"{state.current_scenario.enemy_side} wins. The war dragged into attrition."
    if state.turn_number > 14:
        return f"{state.current_scenario.enemy_side} wins. You failed to achieve a decisive result in time."
    return None


