from typing import TYPE_CHECKING

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

  def start(self):
    """Called once when the object is initialized."""
    pass

  def update(self, dt):
    """Called every frame. Handles Logic."""
    pass

  def draw(self, screen):
    """Called by the rendering system. Handled in Python by components."""
    pass
