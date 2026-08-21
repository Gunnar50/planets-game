import pathlib

from prototype.main.game_state import GameState
from pyeng.main.engine_config import EngineConfig
from pyeng.utils import key_mappings
from pyeng.utils.version import Version


class GameConfig(EngineConfig):
  version = Version(0, 0, 0)
  title = f'Planets Game - Version: {version}'
  window_width = 1280
  window_height = 720
  fullscreen = 0
  cheats = True
  is_editor = False

  game_speed = 1
  cheats = True
  show_debug = True
  auto_save = True
  session_creator = NotImplemented
  initial_state = GameState.INITIAL
  in_game_state = GameState.IN_GAME

  # Sorting by Y axis is used for top down games
  sort_by_y_axis = False

  # World settings
  map_width = 10
  map_height = 10
  tile_width = 16
  tile_height = 16
  scale_factor = 2

  project_root = pathlib.Path.cwd()
  data_folder = project_root / 'data'
  assets = data_folder
  error_logs = project_root / 'error_logs'
  game_mappings = data_folder / 'config/game_mappings.json'
  game_mappings_model = key_mappings.GameMapping

  items_folder = data_folder / 'items'
  entities_folder = data_folder / 'entities'
  tiles_folder = data_folder / 'tiles'
