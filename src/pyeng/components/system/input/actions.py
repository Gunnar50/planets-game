import pygame


class InputActionMap:
  def __init__(self):
    self._enabled = True

  def enable(self) -> None:
    self._enabled = True

  def disable(self) -> None:
    self._enabled = False

  def is_enabled(self) -> bool:
    return self._enabled


class ButtonAction:
  def __init__(self, map_ref: InputActionMap, states: list):
    self._map = map_ref
    self._states = states

  def pressed(self) -> bool:
    return self._map.is_enabled() and any(
      state.pressed for state in self._states
    )

  def just_pressed(self) -> bool:
    return self._map.is_enabled() and any(
      state.just_pressed for state in self._states
    )

  def just_released(self) -> bool:
    return self._map.is_enabled() and any(
      state.just_released for state in self._states
    )


class Vector1Action:
  def __init__(
    self,
    map_ref: InputActionMap,
    positive_states: list,
    negative_states: list,
  ):
    self._map = map_ref
    self._positive_states = positive_states
    self._negative_states = negative_states

  def read_value(self) -> float:
    if not self._map.is_enabled():
      return 0.0
    val = 0.0
    if any(state.pressed for state in self._positive_states):
      val += 1.0
    if any(state.pressed for state in self._negative_states):
      val -= 1.0
    return val


class Vector2Action:
  def __init__(
    self,
    map_ref: InputActionMap,
    up_states: list,
    down_states: list,
    left_states: list,
    right_states: list,
  ):
    self._map = map_ref
    self._up = up_states
    self._down = down_states
    self._left = left_states
    self._right = right_states

  def read_value(self, normalize: bool = True) -> pygame.Vector2:
    if not self._map.is_enabled():
      return pygame.Vector2(0, 0)

    x, y = 0.0, 0.0
    if any(state.pressed for state in self._right):
      x += 1.0
    if any(state.pressed for state in self._left):
      x -= 1.0
    if any(state.pressed for state in self._up):
      y -= 1.0
    if any(state.pressed for state in self._down):
      y += 1.0

    vec = pygame.Vector2(x, y)
    if normalize and vec.length_squared() > 0:
      return vec.normalize()
    return vec
