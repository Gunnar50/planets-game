import pygame

from src.PyEng.components.game.builtin.shape_render import ShapeRenderer
from src.PyEng.components.game.builtin.transform import Transform
from src.PyEng.components.game.game_component import BaseGameComponent
from src.shared.debug import Logger


class GameObject:
  """
  The pure 'Container' box shown in the UGS diagram.
  A GameObject has *no* built-in data or behavior other than Transform,
  which is composition, not inheritance.
  """

  def __init__(self, name='New GameObject'):
    self.name = name
    self.tag: str | None = None
    self.is_active = True  # GameObject active flag
    self.transform = Transform()  # MANDATORY composition.

    # A simple list/dict holding all attached components.
    self._components: dict[type[BaseGameComponent], BaseGameComponent] = {}

    # We always add the transform component as the base.
    self.add_component(self.transform)

  def add_component(self, component: BaseGameComponent) -> None:
    """
    Equivalent to Unity's gameObject.AddComponent<T>().
    Sets the self-reference back to this GameObject container.
    """
    # Simplified key lookup based on class type
    comp_type = type(component)
    self._components[comp_type] = component
    component.game_object = self
    Logger.info(f'[{self.name}] Added component: {comp_type.__name__}')

  def get_component(
    self,
    component_type: type[BaseGameComponent],
  ) -> BaseGameComponent | None:
    """Equivalent to Unity's gameObject.GetComponent<T>()."""
    if self.is_active:
      component = self._components.get(component_type)
      if component and component.enabled:
        return component

    return None

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
    if self.is_active:
      # TODO: Check if the object has any Renderer component
      if renderer := self.get_component(ShapeRenderer):
        # Render using the object's transform location
        renderer.draw(display)
