from pyeng.components.system.assets_manager import AssetsManager
from pyeng.components.system.input import Input
from pyeng.components.system.render import RenderSystem
from pyeng.components.system.state_manager import StateManager
from pyeng.components.system.system_manager import system_manager
from pyeng.components.system.window import Window
from pyeng.main.engine_config import EngineConfig
from pyeng.utils import exceptions
from pyeng.utils import key_mappings
from pyeng.utils.debugger import Debugger
from pyeng.utils.error_manager import ErrorManager


class Engine:
  __instance: 'Engine | None' = None

  def __init__(self, config: type[EngineConfig]):
    self.config = config
    self.window: Window
    self.input: Input
    self.render_system: RenderSystem
    self.system_manager = system_manager

    self.check_assets_folder()
    self.create_engine_components()
    self.create_global_components()

    self.close_flag = False

    Engine.__instance = self

  @classmethod
  def get_instance(cls) -> 'Engine':
    if cls.__instance is None:
      return cls.create()
    return cls.__instance

  def update(self) -> None:
    self.system_manager.update()

  def render(self) -> None:
    self.render_system.render(self.window.display_map)

  def check_assets_folder(self):
    if not self.config.data_folder.exists():
      raise exceptions.IllegalStateException(
        f"Can't create engine - assets folder not found in root directory: {self.config.project_root}."
      )

  def create_global_components(self) -> None:
    # Create global systems
    ErrorManager(self.config.error_logs)
    Debugger(self.config.debug)
    # BackgroundLoader()

  def create_engine_components(self) -> None:
    # Create engine components
    self.window = Window(
      window_width=self.config.window_width,
      window_height=self.config.window_height,
      fullscreen=self.config.fullscreen,
      caption=self.config.title,
      fps=self.config.fps,
      vsync=self.config.vsync,
      background_colour=self.config.background_colour,
      game_config=self.config,
    )

    # Create render system
    self.render_system = RenderSystem()
    self.assets_manager = AssetsManager(self.config)

    # Set up keyboard and mouse inputs
    self.input = Input(
      key_mappings.GameMapping,
      self.config,
    )
    self.state_manager = StateManager(
      self.config.default_state,
      self.config.initial_state,
    )
    # self.timer = FrameTimer(configs.fps)

    # Create UI
    # UserInterface(
    #     self.window,
    #     self.mouse,
    #     self.keyboard,
    #     configs.ui_configs,
    # )

  def get_delta(self) -> float:
    raise NotImplementedError
    # return self.timer.get_delta()

  def get_current_time(self) -> float:
    raise NotImplementedError
    # return self.timer.get_time()

  def close_engine(self) -> None:
    raise NotImplementedError
    # BackgroundLoader.clean_up()
    # Ui.clean_up()
    # self.window.destroy()

  @classmethod
  def create(cls, config: type[EngineConfig] = EngineConfig) -> 'Engine':
    if cls.__instance is not None:
      raise exceptions.IllegalStateException(
        'Engine has already been initialised!'
      )

    return cls(config)
