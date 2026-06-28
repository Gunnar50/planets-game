from typing import TYPE_CHECKING

import pygame

from src.PyEng.components.system.system_manager import system_manager

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

  def start(self):
    """Called once when the object is initialized."""
    if self.game_object is None:
      # TODO
      raise Exception

    self.transform = self.game_object.transform

  def update(self, dt: float):
    """Called every frame. Handles Logic."""
    pass

  def draw(self, display: pygame.Surface):
    """Called by the rendering system. Handled in Python by components."""
    pass
