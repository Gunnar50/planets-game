from typing import TYPE_CHECKING

from src.PyEng.utils.logger import Logger

if TYPE_CHECKING:
  from src.PyEng.components.game.game_object import GameObject


class Scene:
  """A container for GameObjects representing a specific state/level."""

  def __init__(self, name='BaseScene'):
    self.name = name
    self.game_objects: list[GameObject] = []

  def load(self) -> None:
    pass

  def add_object(self, game_object: 'GameObject') -> None:
    self.game_objects.append(game_object)
    game_object.start()

  def update(self, delta_time: float) -> None:
    for game_object in self.game_objects:
      game_object.update(delta_time)


class GameManager:
  """Manages scene transitions and holds the currently active scene."""

  def __init__(self):
    self.current_scene: Scene | None = None

  def load_scene(self, scene: Scene) -> None:
    Logger.info(f'[GameManager] Loading Scene: {scene.name}')
    self.current_scene = scene
    self.current_scene.load()

  def update(self, dt: float) -> None:
    if self.current_scene:
      self.current_scene.update(dt)
