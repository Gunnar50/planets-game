import pygame

from src.PyEng.components.game.game_component import BaseGameComponent
from src.shared.types import Colour


class Renderer(BaseGameComponent):
  """
  Base renderer component. Subclass for sprite, shape, or tilemap rendering.
  SpriteRenderer, ShapeRenderer, etc. all extend this.
  """

  def draw(self, display: pygame.Surface) -> None:
    """Override to draw this object to the screen."""
    raise NotImplementedError


class SquareRenderer(Renderer):
  """Shaper rendering component."""

  def __init__(self, colour: Colour, width: int = 0, height: int = 0):
    Renderer.__init__(self)
    self.colour = colour
    self.width = width
    self.height = height

  def draw(self, display: pygame.Surface) -> None:
    # Renders the surface relative to the GameObject's transform position
    pygame.draw.rect(
      display,
      self.colour,
      (
        self._transform.position.x,
        self._transform.position.y,
        self.width,
        self.height,
      ),
    )


class CircleRenderer(Renderer):
  """Circle rendering component."""

  def __init__(self, colour: Colour, radius: float = 0):
    Renderer.__init__(self)
    self.colour = colour
    self.radius = radius

  def draw(self, display: pygame.Surface) -> None:
    # Renders the surface relative to the GameObject's transform position
    pygame.draw.circle(
      display,
      self.colour,
      (
        self._transform.position.x,
        self._transform.position.y,
      ),
      self.radius,
    )
