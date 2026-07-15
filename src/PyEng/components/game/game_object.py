from typing import cast

import pygame

from src.PyEng.components.game.builtin.shape_render import Renderer
from src.PyEng.components.game.builtin.transform import Transform
from src.PyEng.components.game.game_component import BaseGameComponent
from src.PyEng.utils import exceptions
from src.PyEng.utils.logger import Logger
from src.PyEng.utils.types import TComponent


class GameObject:
  """
  The pure 'Container' box shown in the UGS diagram.
  A GameObject has *no* built-in data or behavior other than Transform,
  which is composition, not inheritance.
  """

  def __init__(self, name: str):
    self.name = name
    self.tag: str | None = None
    self.is_active = True  # GameObject active flag
    self.transform = Transform()  # MANDATORY composition.
    self.renderer: Renderer | None = None

    # A simple list/dict holding all attached components.
    self._components: dict[type[BaseGameComponent], BaseGameComponent] = {}

    # We always add the transform component as the base.
    self.add_component(self.transform)

  def add_component(self, component: BaseGameComponent) -> None:
    """
    Equivalent to Unity's gameObject.AddComponent<T>().
    Sets the self-reference back to this GameObject container.
    """
    if isinstance(component, Renderer):
      if self.renderer is None:
        self.renderer = component
      else:
        Logger.warning(
          f'[{self.name}] already has a Renderer! You must remove the first renderer before adding a new one! Skipping...'
        )
        return

    # Simplified key lookup based on class type
    comp_type = type(component)
    self._components[comp_type] = component
    component.game_object = self
    Logger.info(f'[{self.name}] Added component: {comp_type.__name__}')

  def try_get_component(
    self,
    component_type: type[TComponent],
  ) -> TComponent | None:
    """Equivalent to Unity's gameObject.GetComponent<T>()."""
    if self.is_active:
      component = self._components.get(component_type)
      if component and component.enabled:
        return cast(TComponent, component)

    return None

  def get_component(self, component_type: type[TComponent]) -> TComponent:
    if self.is_active:
      component = self._components.get(component_type)
      if component and component.enabled:
        return cast(TComponent, component)

    raise exceptions.ComponentNotFoundError('Component not found')

  def start(self) -> None:
    """
    Initializes the object. Starts all child components.
    Called once by SceneManager.
    """
    if self.is_active:
      for component in self._components.values():
        if component.enabled:
          Logger.info(
            f'[{self.name}] Started component: {type(component).__name__}'
          )
          component.start()

  def update(self, dt: float) -> None:
    """Updates all enabled components (excluding transform data update)."""
    if self.is_active:
      for component in self._components.values():
        if component.enabled:
          component.update(dt)

  def draw(self, display: pygame.Surface) -> None:
    """Render routine for visual components (like SpriteRenderer)."""
    if self.is_active and self.renderer:
      self.renderer.draw(display)

  def destroy(self) -> None:
    if self.is_active:
      self.is_active = False
      # Destroy all components of this game object
      for component in self._components.values():
        component.on_destroy()
      self._components.clear()
