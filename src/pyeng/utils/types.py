from collections.abc import Sequence
from typing import TypeVar

from pyeng.components.game.game_component import BaseGameComponent

Coordinate = tuple[float, float] | Sequence[float]
RGBAOutput = tuple[int, int, int, int]
Colour = tuple[int, int, int]
SortingKey = tuple[int, int, float]

TComponent = TypeVar('TComponent', bound=BaseGameComponent)
