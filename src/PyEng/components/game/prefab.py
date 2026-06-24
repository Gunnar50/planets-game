import pygame

from src.PyEng.components.game.game_object import GameObject


class Prefab:
  """
  A factory for creating pre-configured GameObjects.
  Mirrors Unity's Prefab concept.

  Subclass this and implement `create()` to define a reusable object template.

  can have a method

  Usage:
      prefab = PlayerPrefab()
      player = prefab.instantiate(x=100, y=200)
      scene.add_object(player)
  """

  # Should have method to create prefab from a json file
  def __init__(
    self,
    position: tuple[int, int] = (0, 0),
    rotation=None,
  ) -> None:
    self.position = pygame.Vector2(position[0], position[1])
    self.rotation = rotation

  def create(self, **kwargs) -> GameObject:
    """
    Override this method. Build and return a fully configured GameObject.
    kwargs can carry spawn position, overrides, variants, etc.
    """
    raise NotImplementedError
