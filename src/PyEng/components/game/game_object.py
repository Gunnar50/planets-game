from src.PyEng.components.game.builtin.transform import Transform
from src.PyEng.components.game.game_component import BaseGameComponent


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

  def add_component(self, component: BaseGameComponent) -> BaseGameComponent:
    """
    Equivalent to Unity's gameObject.AddComponent<T>().
    Sets the self-reference back to this GameObject container.
    """
    # Simplified key lookup based on class type
    comp_type = type(component)
    self._components[comp_type] = component
    component.game_object = self
    print(f'[{self.name}] Added component: {comp_type.__name__}')
    return component

  def get_component(self, component_type: type[BaseGameComponent]):
    """Equivalent to Unity's gameObject.GetComponent<T>()."""
    return self._components.get(component_type)

  def start(self):
    """
    Initializes the object. Starts all child components.
    Called once by SceneManager.
    """
    for component in self._components.values():
      if component.enabled:
        component.start()

  def update(self, dt):
    """Updates all enabled components (excluding transform data update)."""
    if not self.is_active:
      return

    for component in self._components.values():
      if component.enabled:
        component.update(dt)

  def draw(self, screen):
    """Render routine for visual components (like SpriteRenderer)."""
    if not self.is_active:
      return

    for component in self._components.values():
      if component.enabled:
        component.draw(screen)
