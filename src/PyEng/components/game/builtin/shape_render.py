import pygame

from src.PyEng.components.game.game_component import BaseGameComponent
from src.shared.types import Colour


class ShapeRenderer(BaseGameComponent):
  """Shaper rendering component."""

  def __init__(self, colour: Colour, width: int = 0, height: int = 0):
    BaseGameComponent.__init__(self)
    self.color = colour
    self.size = (width, height)
    self.surface = pygame.Surface(self.size)
    self.surface.fill(colour)

  def draw(self, display: pygame.Surface) -> None:
    if not self.game_object:
      # TODO: Create custom exception
      raise Exception

    # Renders the surface relative to the GameObject's transform position
    display.blit(
      self.surface,
      (
        self.game_object.transform.position.x,
        self.game_object.transform.position.y,
      ),
    )
