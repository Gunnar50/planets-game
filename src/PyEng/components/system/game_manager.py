from typing import TYPE_CHECKING

from src.PyEng.utils.logger import Logger

if TYPE_CHECKING:
  from src.PyEng.components.game.game_object import GameObject


class Scene:
  """A container for GameObjects representing a specific state/level."""

  _active_scene: 'Scene | None' = None

  def __init__(self, name='BaseScene'):
    self.name = name
    self.game_objects: list[GameObject] = []
    self._pending_destroy: list[GameObject] = []

  def make_active(self) -> None:
    Scene._active_scene = self

  @classmethod
  def get_active_scene(cls) -> 'Scene':
    if active_scene := Scene._active_scene:
      return active_scene
    raise Exception('Failed to return active scene. No scene set.')

  def load(self) -> None:
    pass

  def add_object(self, game_object: 'GameObject') -> None:
    self.game_objects.append(game_object)
    game_object.start()

  def destroy(self, game_object: 'GameObject') -> None:
    self._pending_destroy.append(game_object)

  def update(self, delta_time: float) -> None:
    for game_object in self.game_objects:
      game_object.update(delta_time)

  def cleanup(self):
    for game_object in self._pending_destroy:
      game_object.destroy()
    self._pending_destroy.clear()


class GameManager:
  """Manages scene transitions and holds the currently active scene."""

  def __init__(self):
    self._current_scene: Scene | None = None

  def load_scene(self, scene: Scene) -> None:
    Logger.info(f'[GameManager] Loading Scene: {scene.name}')
    scene.make_active()
    self._current_scene = scene
    self._current_scene.load()

  def update(self, dt: float) -> None:
    if self._current_scene:
      self._current_scene.update(dt)

  def get_current_scene(self) -> Scene:
    if self._current_scene:
      return self._current_scene
    raise Exception('Failed to return current scene. No scene set.')
