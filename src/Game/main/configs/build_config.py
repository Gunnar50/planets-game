from src.Game.main.configs.game_config import GameConfig


class BuildConfig(GameConfig):
  window_width = 1280
  window_height = 720
  title = f'Planets Game - Version: {GameConfig.version}'
  fullscreen = 0
  cheats = True
  is_editor = False

  # World settings
  map_width = 10
  map_height = 10
  tile_width = 16
  tile_height = 16
  scale_factor = 2
