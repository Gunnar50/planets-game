import pygame

from pyeng.components.game.game_component import BaseGameComponent


class PlayerMovement(BaseGameComponent):
  """
  Custom component
  Reads keyboard input and moves the player each frame.

  Attach to any GameObject to make it player-controlled.
  """

  def __init__(self, speed: float = 200):
    BaseGameComponent.__init__(self)
    self.speed = speed

  def start(self) -> None:
    super().start()

  def update(self, dt: float) -> None:
    """Read WASD/arrow input and translate the object."""
    keys = pygame.key.get_pressed()
    dx, dy = 0, 0

    if keys[pygame.K_w] or keys[pygame.K_UP]:
      dy -= 1
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
      dy += 1
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
      dx -= 1
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
      dx += 1

    # Normalise diagonal movement
    vec = pygame.Vector2(dx, dy)
    if vec.length() > 0:
      vec = vec.normalize()

    self.transform.translate(vec.x * self.speed * dt, vec.y * self.speed * dt)
