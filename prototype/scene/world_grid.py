import pathlib

import pygame

from prototype.main.configs.build_config import BuildConfig
from PyEng.components.game.prefab import Prefab
from PyEng.utils import io


class WorldGrid(Prefab):
  def __init__(self, world_size: int) -> None:
    Prefab.__init__(self)
    self.world_size = world_size

  def save(self, file_path: pathlib.Path) -> None:
    output = io.export_data(self.export())
    io.write_json(file_path, output)

  def draw_grid(self, screen: pygame.Surface):
    for x in range(0, BuildConfig.window_width, BuildConfig.tile_width):
      pygame.draw.line(
        screen, (150, 150, 150), (x, 0), (x, BuildConfig.window_height)
      )

    for y in range(0, BuildConfig.window_height, BuildConfig.tile_height):
      pygame.draw.line(
        screen, (150, 150, 150), (0, y), (BuildConfig.window_width, y)
      )

  def render(self, screen: pygame.Surface) -> None:
    self.draw_grid(screen)

  def export(self) -> dict:
    return {}
