import pygame

from src.PyEng.components.game.game_component import BaseGameComponent


class ShapeRender(BaseGameComponent):
  """Shaper rendering component."""

  def __init__(self, color, size=(32, 32)):
    BaseGameComponent.__init__(self)
    self.color = color
    self.size = size
    self.surface = pygame.Surface(size)
    self.surface.fill(color)

  def draw(self, display: pygame.Surface):
    if not self.game_object:
      raise Exception

    # Renders the surface relative to the GameObject's transform position
    display.blit(
      self.surface,
      (
        self.game_object.transform.position.x,
        self.game_object.transform.position.y,
      ),
    )
