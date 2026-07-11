import pygame

from src.Game.content.prefabs.tile import TilePrefab
from src.PyEng.components.game.builtin.shape_render import SquareRenderer
from src.PyEng.components.game.game_component import BaseGameComponent


class GridManager(BaseGameComponent):
  def __init__(self, width: int, height: int):
    BaseGameComponent.__init__(self)
    self.width, self.height = width, height
    self.tile_prefab = TilePrefab

  def start(self) -> None:
    super().start()
    self.generate_grid()

  def generate_grid(self) -> None:
    for x in range(self.width):
      for y in range(self.height):
        tile = self.tile_prefab().create(
          name=f'Tile: {x}, {y}',
          position=pygame.Vector2(x, y),
        )
        renderer = tile.get_component(SquareRenderer)
        is_offset = (x + y) % 2 == 0
        if is_offset:
          renderer.colour = (200, 0, 0)
        else:
          renderer.colour = (100, 0, 0)
