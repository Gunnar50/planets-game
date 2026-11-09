from pyeng.utils import exceptions


def get_input_id(input_key: str) -> int:
  if input_id := input_map.get(input_key):
    return input_id

  raise exceptions.InvalidInputKey(f'Invalid Input Key {input_key!r}')


# TODO: make keys into enum for better parsing and validation?
input_map = {
  # Symbols
  '#': 35,
  "'": 39,
  ',': 44,
  '-': 45,
  '.': 46,
  '/': 47,
  ';': 59,
  '=': 61,
  '[': 91,
  ']': 93,
  # Numbers
  'num0': 48,
  'num1': 49,
  'num2': 50,
  'num3': 51,
  'num4': 52,
  'num5': 53,
  'num6': 54,
  'num7': 55,
  'num8': 56,
  'num9': 57,
  # Letters
  'a': 97,
  'b': 98,
  'c': 99,
  'd': 100,
  'e': 101,
  'f': 102,
  'g': 103,
  'h': 104,
  'i': 105,
  'j': 106,
  'k': 107,
  'l': 108,
  'm': 109,
  'n': 110,
  'o': 111,
  'p': 112,
  'q': 113,
  'r': 114,
  's': 115,
  't': 116,
  'u': 117,
  'v': 118,
  'w': 119,
  'x': 120,
  'y': 121,
  'z': 122,
  # Special
  'backspace': 8,
  'tab': 9,
  'return': 13,
  'space': 32,
  'left_shift': 1073742049,
  'left_control': 1073742048,
  'left_alt': 1073742050,
  'right_shift': 1073742053,
  'right_control': 1073742052,
  # NumPad
  'numpad0': 1073741922,
  'numpad1': 1073741913,
  'numpad2': 1073741914,
  'numpad3': 1073741915,
  'numpad4': 1073741916,
  'numpad5': 1073741917,
  'numpad6': 1073741918,
  'numpad7': 1073741919,
  'numpad8': 1073741920,
  'numpad9': 1073741921,
  # Arrows
  'up': 1073741906,
  'left': 1073741904,
  'down': 1073741905,
  'right': 1073741903,
  # Function keys
  'f1': 1073741882,
  'f2': 1073741883,
  'f3': 1073742051,
  'f4': 1073741885,
  'f5': 1073741886,
  'f6': 1073741887,
  'f7': 1073741888,
  'f8': 1073741889,
  'f9': 1073741890,
  'f10': 1073741891,
  'f11': 1073741892,
  'f12': 1073741893,
  # Mouse
  'mouse_left': 1,
  'mouse_middle': 2,
  'mouse_right': 3,
}
