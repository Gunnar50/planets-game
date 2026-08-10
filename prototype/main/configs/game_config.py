from prototype.main.game_state import GameState
from pyeng.main.engine_config import EngineConfigs
from pyeng.utils.version import Version


class GameConfig(EngineConfigs):
  version = Version(0, 0, 0)
  game_speed = 1
  cheats = True
  show_debug = True
  auto_save = True
  session_creator = NotImplemented
  initial_state = GameState.INITIAL
  in_game_state = GameState.IN_GAME
