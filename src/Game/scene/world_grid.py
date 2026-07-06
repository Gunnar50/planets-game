import pathlib

import pygame

from src.Game.main.configs.build_config import BuildConfig
from src.PyEng.main.engine import Engine
from src.PyEng.utils import io
from src.PyEng.utils import serialisers


class Scene:
  WORLD_SIZE = 10

  def __init__(self) -> None:
    self.window = Engine.get_instance().window
    self.world_grid = WorldGrid(self, Scene.WORLD_SIZE)

  def update(self):
    pass

  def render(self):
    self.world_grid.render(self.window.game_display)


class WorldGrid(serialisers.Serialiser):
  def __init__(self, scene: Scene, world_size: int) -> None:
    self.scene = scene
    self.world_size = world_size
    game_manager_component = self.components_manager.get_game_manager()

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

  def export(self):
    return {}
