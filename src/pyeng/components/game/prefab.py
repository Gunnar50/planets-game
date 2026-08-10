from typing import TYPE_CHECKING

import pygame

from pyeng.components.game.game_object import GameObject
from pyeng.components.system.game_manager import Scene
from pyeng.utils import exceptions

if TYPE_CHECKING:
  from pyeng.components.game.game_component import BaseGameComponent


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
    position: pygame.Vector2 = pygame.Vector2(0, 0),
    rotation=None,
    **kwargs,
  ) -> None:
    self.position = pygame.Vector2(position[0], position[1])
    self.rotation = rotation
    self.game_object: GameObject | None = None
    self._components_to_add: list[BaseGameComponent] = []
    self.initialise_components(**kwargs)

  def get_game_obj(self) -> 'GameObject':
    if self.game_object is None:
      raise exceptions.NoGameObjectException(
        f'Prefab {self.__class__.__name__!r} should have a GameObject attach to it'
      )
    return self.game_object

  def initialise_components(self, **kwargs) -> None:
    pass

  def add_component(self, component: 'BaseGameComponent') -> None:
    self._components_to_add.append(component)

  def create(
    self,
    *,
    name: str = 'New GameObject',
    position: pygame.Vector2 | None = None,
    rotation=None,
  ) -> GameObject:
    game_object = GameObject(name=name)
    game_object.transform.position = position or self.position
    # TODO: Add rotation
    self.game_object = game_object

    # Add all components
    for component in self._components_to_add:
      game_object.add_component(component)
    self._components_to_add.clear()

    # Add object to the scene
    Scene.get_active_scene().add_object(game_object)

    return game_object
