from typing import TYPE_CHECKING

import pygame

from src.Game.main.configs.game_config import GameConfig
from src.Game.main.game_state import GameState
from src.Game.repository.game_database import BlueprintDatabase
from src.PyEng.components.system.system_component import SystemComponent
from src.PyEng.main.engine import Engine
from src.shared.debug import Logger

if TYPE_CHECKING:
  from src.PyEng.components.game.game_object import GameObject


class OldGameManager(SystemComponent):
  configs: GameConfig
  engine: Engine
  blueprint_db: BlueprintDatabase
  # current_session: GameSession

  def __init__(self, engine: Engine, add=True):
    SystemComponent.__init__(self)
    self.engine = engine

    # Load blueprint for assets
    self.blueprint_db = BlueprintDatabase()
    # init game controls
    # init sounds
    # init session manager
    # self.current_session = GameSession()

    # for i in cls.blueprint_db.tiles:
    #   print(i.tile_type)

  def get_blueprint_database(self) -> BlueprintDatabase:
    return self.blueprint_db

  def update(self) -> None:
    # If there is a session (game is running),
    # and the state is not main_menu
    # render the scene
    if self.engine.state_manager.is_not_state(
      GameState.MAIN_MENU, GameState.INITIAL
    ):
      # self.engine.render
      # in the renderer
      pass

    # Update the current session which renders the world
    # self.engine.render()
    # self.current_session.update()


class Scene:
  """A container for GameObjects representing a specific state/level."""

  def __init__(self, name='BaseScene'):
    self.name = name
    self.game_objects: list[GameObject] = []

  def add_object(self, game_object: 'GameObject') -> None:
    self.game_objects.append(game_object)
    game_object.start()

  def update(self, delta_time: float) -> None:
    for game_object in self.game_objects:
      game_object.update(delta_time)

  def render(self, display: pygame.Surface) -> None:
    for game_object in self.game_objects:
      game_object.draw(display)


class GameManager:
  """Manages scene transitions and holds the currently active scene."""

  def __init__(self):
    self.current_scene: Scene | None = None

  def load_scene(self, scene: Scene) -> None:
    Logger.info(f'[GameManager] Loading Scene: {scene.name}')
    self.current_scene = scene

  def update(self, dt: float) -> None:
    if self.current_scene:
      self.current_scene.update(dt)

  def render(self, display: pygame.Surface) -> None:
    if self.current_scene:
      self.current_scene.render(display)
