import sys
import time

import pygame

from pyeng.components.game.game_component import BaseGameComponent
from pyeng.components.system.system_component import SystemComponent
from pyeng.main.engine_config import EngineConfig
from pyeng.utils import api
from pyeng.utils import io
from pyeng.utils import key_mappings


class InputState:
  def __init__(
    self,
    label: str,
    input_id: int,
  ):
    self.label = label
    self.input_id = input_id

    self.pressed = False
    self.just_pressed = False
    self.just_released = False
    self.held_since = 0.0

  def update(self):
    self.just_pressed = False
    self.just_released = False

  def press(self):
    self.pressed = True
    self.just_pressed = True
    self.held_since = time.time()

  def unpress(self):
    self.pressed = False
    self.just_released = True


class Input(SystemComponent):
  def __init__(
    self,
    mapping_type: type[key_mappings.MappingBase],
    game_config: type[EngineConfig],
  ):
    SystemComponent.__init__(self)
    self.game_config = game_config
    self.mapping_type = mapping_type
    self.input_config = io.load_model_from_json(
      self.game_config.game_mappings, api.InputConfig
    )
    self.input = {
      mapping_type(mapping.label): InputState(
        mapping.label,
        mapping.input_id,
      )
      for mapping in self.input_config.config
    }
    self.modifier_keys = []

    self.keyboard = Keyboard(self.input)
    self.mouse = Mouse(self.input, game_config)

  def pressed(
    self,
    key: key_mappings.MappingBase,
    modifier: key_mappings.MappingBase | None = None,
  ) -> bool:
    if modifier:
      if modifier in self.modifier_keys:
        return self.input[key].just_pressed if key in self.input else False
    else:
      if not self.modifier_keys:
        return self.input[key].just_pressed if key in self.input else False

    return False

  def holding(self, key: key_mappings.MappingBase) -> bool:
    return self.input[key].pressed if key in self.input else False

  def released(self, key: key_mappings.MappingBase) -> bool:
    return self.input[key].just_released if key in self.input else False

  def update(self):
    for state in self.input.values():
      state.update()

    self.modifier_keys = [
      self.mapping_type(state.label)
      for state in self.input.values()
      if state.pressed
    ]

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

      self.keyboard.update(event)
      self.mouse.update(event)


class Keyboard:
  def __init__(
    self,
    input_config: dict[key_mappings.MappingBase, InputState],
  ):
    self.input = input_config

  def update(self, event: pygame.event.Event) -> None:
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        pygame.quit()
        sys.exit()

      for state in self.input.values():
        if event.key == state.input_id:
          state.press()

    elif event.type == pygame.KEYUP:
      for state in self.input.values():
        if event.key == state.input_id:
          state.unpress()


class Mouse:
  def __init__(
    self,
    input_config: dict[key_mappings.MappingBase, InputState],
    game_config: type[EngineConfig],
  ):
    self.game_config = game_config
    self.input = input_config
    self.position = api.Position(0, 0)
    self.ui_position = api.Position(0, 0)
    self.movement = api.Position(0, 0)
    self._interactive_components: list[BaseGameComponent] = []

  def update(self, event: pygame.event.Event) -> None:
    mx, my = pygame.mouse.get_pos()
    self.position = api.Position(
      mx // self.game_config.scale_factor, my // self.game_config.scale_factor
    )
    self.ui_x, self.ui_y = self.position.x // 2, self.position.y // 2

    if event.type == pygame.MOUSEMOTION:
      self._process_mouse_hovers()

    if event.type == pygame.MOUSEBUTTONDOWN:
      for state in self.input.values():
        if event.button == state.input_id:
          state.press()

    elif event.type == pygame.MOUSEBUTTONUP:
      for state in self.input.values():
        if event.button == state.input_id:
          state.unpress()

  def register_interactive(self, component: BaseGameComponent) -> None:
    if component not in self._interactive_components:
      self._interactive_components.append(component)

  def unregister_interactive(self, component: BaseGameComponent) -> None:
    if component in self._interactive_components:
      self._interactive_components.remove(component)

  def _process_mouse_hovers(self) -> None:
    """Checks bounds and dispatches enter/exit events to subscribers."""
    mouse_point = (self.position.x, self.position.y)

    for component in self._interactive_components:
      game_object = component.get_game_object()
      # Skip if component or parent GameObject is inactive
      if component.enabled and game_object.is_active:
        # Ensure the object actually has a renderer to check bounds against
        if renderer := game_object.renderer:
          # Check collision
          is_mouse_over = renderer.bounds().collidepoint(mouse_point)
          if is_mouse_over and not component.is_hovered:
            component.is_hovered = True
            component.on_mouse_enter()
          elif not is_mouse_over and component.is_hovered:
            component.is_hovered = False
            component.on_mouse_exit()
