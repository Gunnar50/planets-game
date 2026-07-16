from typing import TYPE_CHECKING

from src.PyEng.components.system.system_manager import system_manager
from src.PyEng.utils import exceptions

if TYPE_CHECKING:
  from src.PyEng.components.game.game_object import GameObject
  from src.PyEng.utils.types import TComponent


class BaseGameComponent:
  """
  The analog to Unity's 'MonoBehaviour' or the generic 'Component' box.
  All logic (scripts) and data (built-ins) inherit from this.
  """

  def __init__(self):
    # The GameObject this component is currently attached to.
    # This is how components access data from sister components.
    self.game_object: GameObject | None = None
    self.enabled = True
    self.system_components = system_manager
    self.assets_manager = self.system_components.get_assets_manager()
    self.render_system = self.system_components.get_render()
    self.input_mouse = self.system_components.get_input().mouse
    self.is_hovered = False

    # Check if child methods exists
    self.has_mouse_enter = self.has_method('on_mouse_enter')
    self.has_mouse_exit = self.has_method('on_mouse_exit')
    self.has_update = self.has_method('update')

  def has_method(self, method_name: str) -> bool:
    child_method = getattr(type(self), method_name)
    parent_method = getattr(BaseGameComponent, method_name)
    return child_method is not parent_method

  def start(self) -> None:
    """Called once when the object is initialized."""
    if self.game_object is None:
      raise exceptions.NoGameObjectException(
        f'Component {self.__class__.__name__!r} should have a GameObject attach to it'
      )

    self.transform = self.game_object.transform

    # If this subclass overrides the default empty hover methods, register it!
    if self.has_mouse_enter or self.has_mouse_exit:
      self.input_mouse.register_interactive(self)
    if self.has_update:
      self.get_game_object().register_update(self)

  def on_destroy(self) -> None:
    if self.has_mouse_enter or self.has_mouse_exit:
      self.input_mouse.unregister_interactive(self)

  def get_game_object(self) -> 'GameObject':
    if self.game_object is None:
      raise exceptions.NoGameObjectException(
        f'Prefab {self.__class__.__name__!r} should have a GameObject attach to it'
      )
    return self.game_object

  def get_component(self, component_type: type['TComponent']) -> 'TComponent':
    return self.get_game_object().get_component(component_type)

  def update(self, dt: float) -> None:
    """Called every frame. Handles Logic."""
    pass

  def on_mouse_enter(self) -> None:
    pass

  def on_mouse_exit(self) -> None:
    pass
