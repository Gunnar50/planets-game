from src.Game.main.game_state import GameState
from src.PyEng.main.engine_config import EngineConfigs
from src.PyEng.utils.version import Version


class GameConfig(EngineConfigs):
  version = Version(0, 0, 0)
  game_speed = 1
  cheats = True
  show_debug = True
  auto_save = True
  session_creator = NotImplemented
  initial_state = GameState.INITIAL
  in_game_state = GameState.IN_GAME
  # Sorting by Y axis is used mostly for top down games
  sort_by_y_axis = False
