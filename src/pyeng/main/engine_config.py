import pathlib

from pyeng.components.system.state_manager import State
from pyeng.utils.version import Version


class EngineConfig:
  version = Version(0, 0, 0)
  window_width = 1280
  window_height = 720
  ui_size = 1.0
  fullscreen = 0
  title = 'The Game'
  fps = 60
  vsync = False
  background_colour = (100, 100, 100)

  # ui_resources = UiResources()
  # ui_configs = ui_configs.UiConfigs()
  # resources = Resources()

  # # Using an empty state by default
  initial_state = State()
  default_state = State()

  debug = True
  is_editor = False

  # World settings
  map_width: int
  map_height: int
  tile_width: int
  tile_height: int
  scale_factor = 1

  # Sorting by Y axis is used for top down games
  sort_by_y_axis = False

  # Project folder paths. Override these in your game config to use
  # different names or locations for any of these folders.
  project_root = pathlib.Path.cwd()
  data_folder = project_root / 'data'
  assets = data_folder
  error_logs: pathlib.Path
  # Find better way to handle mappings
  game_mappings: pathlib.Path

  def __init_subclass__(cls, **kwargs) -> None:
    required = {
      k for k in EngineConfig.__annotations__ if k not in EngineConfig.__dict__
    }
    missing = required - set(cls.__dict__)
    if missing:
      raise TypeError(f'{cls.__name__} must define: {missing}')
