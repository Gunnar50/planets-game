import enum

import pygame

from pyeng.components.game.game_component import BaseGameComponent


class GridLayout(enum.Enum):
  RECTANGLE = 'rectangle'
  ISOMETRIC = 'isometric'
  HEXAGONPOINTY = 'hexagonpointy'
  HEXAGONFLAT = 'hexagonflat'


class Grid(BaseGameComponent):
  """
  Manages spatial layouts. Translates between continuous world space
  and discrete integer cell grid coordinate nodes.
  """

  def __init__(
    self,
    cell_size: tuple[int, int] = (16, 16),
    grid_layout: GridLayout = GridLayout.RECTANGLE,
  ):
    BaseGameComponent.__init__(self)
    self.cell_width, self.cell_height = cell_size
    self.grid_layout = grid_layout

  def world_to_cell(self, world_position: pygame.Vector2) -> tuple[int, int]:
    """Converts a continuous world pixel coordinate into an integer (X, Y) grid cell index."""
    # Calculate offset relative to the Grid's origin position
    origin = self.transform.position
    relative_x = world_position.x - origin.x
    relative_y = world_position.y - origin.y

    if self.grid_layout == GridLayout.RECTANGLE:
      cell_x = int(relative_x // self.cell_width)
      cell_y = int(relative_y // self.cell_height)
      return (cell_x, cell_y)

    return (0, 0)

  def cell_to_world(self, cell_coords: tuple[int, int]) -> pygame.Vector2:
    """Converts an integer (X, Y) grid cell index back into a continuous world pixel vector."""
    cell_x, cell_y = cell_coords
    origin = self.transform.position

    if self.grid_layout == GridLayout.RECTANGLE:
      world_x = origin.x + (cell_x * self.cell_width)
      world_y = origin.y + (cell_y * self.cell_height)
      return pygame.Vector2(world_x, world_y)

    return pygame.Vector2(origin.x, origin.y)
