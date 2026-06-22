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

  def create(self, **kwargs) -> GameObject:
    """
    Override this method. Build and return a fully configured GameObject.
    kwargs can carry spawn position, overrides, variants, etc.
    """
    raise NotImplementedError

  def instantiate(self, **kwargs) -> GameObject:
    """Public entry point. Calls create() and returns the GameObject."""
    return self.create(**kwargs)


class PlayerPrefab(Prefab):
  """
  Reusable Player template. Mirrors a Unity Prefab asset.
  Instantiate this anywhere to get a fully wired-up player.

  Usage:
      player = PlayerPrefab().instantiate(x=100, y=300)
      scene.add_object(player)
  """

  # Should have create method to create prefab from a json file

  def create(self, x=0, y=0, speed=200, health=100, **kwargs) -> GameObject:
    obj = GameObject('Player')
    obj.tag = 'Player'

    # Transform is already added in GameObject.__init__
    obj.transform.position = pygame.Vector2(x, y)

    # Visual — swap ShapeRenderer for SpriteRenderer when you have art
    obj.add_component(ShapeRenderer(color=(100, 180, 255), width=32, height=48))

    # Behaviour scripts
    obj.add_component(PlayerMovement(speed=speed))
    obj.add_component(Health(max_health=health))

    return obj
