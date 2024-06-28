from enum import Enum, auto

class SuperCoolEnum(Enum):
    FIRST = auto()
    SECOND = auto()
    OTHER = auto()


for e in list(SuperCoolEnum):
    print(e.name, e.value)
