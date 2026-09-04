# sun_tzu_hex_modular/models.py

from dataclasses import dataclass
from typing import Callable

@dataclass
class Tile:
    q: int
    r: int
    terrain: str = "plain"
    revealed: bool = False

@dataclass
class Unit:
    name: str
    side: str
    q: int
    r: int
    hp: int
    atk: int
    move: int
    range: int
    role: str
    hidden: bool = False
    acted: bool = False
    @property
    def pos(self):
        return self.q, self.r

@dataclass
class Principle:
    key: str
    title: str
    description: str

@dataclass
class Scenario:
    key: str
    principle_key: str
    title: str
    subtitle: str
    description: str
    player_side: str
    enemy_side: str
    setup_func: Callable



