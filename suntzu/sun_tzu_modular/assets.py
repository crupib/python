# sun_tzu_hex_modular/assets.py

import pygame
from constants import UNIT_ASSET_ROOT, UNIT_IMAGE_SIZE

UNIT_IMAGES = {}

def candidate_filenames_for_role(role):
    files = {
        "commander": ["commander.png", "hq.png", "leader.png"],
        "cavalry": ["cavalry.png", "horse.png"],
        "infantry": ["infantry.png", "soldier.png"],
        "elite infantry": ["infantry.png", "elite_infantry.png"],
        "phalanx": ["phalanx.png"],
        "skirmisher": ["skirmisher.png"],
        "guard": ["guard.png"],
        "artillery": ["artillery.png", "gun.png"],
        "chariot": ["chariot.png"],
        "elephant": ["elephant.png"],
        "paratrooper": ["paratrooper.png", "paratroopers.png", "airborne.png", "airborne_infantry.png"],
        "armor": ["armor.png", "tank.png", "sherman.png"],
        "naval": ["naval.png", "ship.png", "battleship.png"],
        "bunker": ["bunker.png", "fortification.png"],
        "aircraft": ["aircraft.png", "jet.png", "fighter.png"],
        "mechanized": ["mechanized.png", "apc.png", "halftrack.png"],
        "airdefense": ["airdefense.png", "sam.png", "aa.png"],
    }
    return files.get(role, [f"{role}.png"])

def load_first_existing_image(paths):
    for path in paths:
        if not path.exists():
            continue
        try:
            img = pygame.image.load(str(path)).convert_alpha()
            return pygame.transform.smoothscale(img, (UNIT_IMAGE_SIZE, UNIT_IMAGE_SIZE))
        except pygame.error:
            continue
    return None

def load_unit_images_for_scenario(scenario_key):
    UNIT_IMAGES.clear()
    roles = ["commander", "cavalry", "infantry", "elite infantry", "phalanx", "skirmisher", "guard", "artillery", "chariot", "elephant", "paratrooper", "armor", "naval", "bunker", "aircraft", "mechanized", "airdefense"]
    for role in roles:
        filenames = candidate_filenames_for_role(role)
        paths = [UNIT_ASSET_ROOT / scenario_key / filename for filename in filenames]
        paths.extend(UNIT_ASSET_ROOT / "common" / filename for filename in filenames)
        UNIT_IMAGES[role] = load_first_existing_image(paths)



