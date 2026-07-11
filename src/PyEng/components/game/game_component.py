from typing import TYPE_CHECKING

import pygame

from src.PyEng.components.system.system_manager import system_manager
from src.PyEng.utils import exceptions

if TYPE_CHECKING:
  from src.PyEng.components.game.game_object import GameObject


class BaseGameComponent:
  """
  The analog to Unity's 'MonoBehaviour' or the generic 'Component' box.
  All logic (scripts) and data (built-ins) inherit from this.
  """

  def __init__(self):
    # The GameObject this component is currently attached to.
    # This is how components access data from sister components.
    self.game_object: GameObject | None = None
    self.enabled = True
    self.system_components = system_manager
    self.assets_manager = self.system_components.get_assets_manager()
    self.render_system = self.system_components.get_render()

  def start(self):
    """Called once when the object is initialized."""
    if self.game_object is None:
      raise exceptions.NoGameObjectException(
        f'Component {self.__class__.__name__!r} should have a GameObject attach to it'
      )

    self.transform = self.game_object.transform

  def get_game_obj(self) -> 'GameObject':
    if self.game_object is None:
      raise exceptions.NoGameObjectException(
        f'Prefab {self.__class__.__name__!r} should have a GameObject attach to it'
      )
    return self.game_object

  def update(self, dt: float) -> None:
    """Called every frame. Handles Logic."""
    pass

  def draw(self, display: pygame.Surface) -> None:
    """Called by the rendering system. Handled in Python by components."""
    pass

  def on_destroy(self) -> None:
    """Called by the Component when is being destroyed."""
    pass
