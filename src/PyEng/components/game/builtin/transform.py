import pygame

from src.PyEng.components.game.game_component import BaseGameComponent


class Transform(BaseGameComponent):
  """Transform Component. MANDATORY on every GameObject."""

  def __init__(self, x=0, y=0, angle=0):
    super().__init__()
    # Pygame uses vectors and Rects.
    # This component stores the essential STATE DATA (Position).
    self.position = pygame.Vector2(x, y)
    self.rotation = angle
    self.scale = pygame.Vector2(1, 1)

  def translate(self, dx: float, dy: float):
    """Move by an offset."""
    self.position += pygame.Vector2(dx, dy)

  def start(self):
    print(f'Transform initialized at: {self.position}')
