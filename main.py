from src.Game.main.configs.build_config import BuildConfig
from src.Game.scene.game_scene import GameScene
from src.PyEng.components.system.game_manager import GameManager
from src.PyEng.main.engine import Engine
from src.shared import key_mappings


class EngineTester:
  def __init__(self) -> None:
    self.engine = Engine.create()

  def update(self) -> None:
    self.engine.update()

  def run(self) -> None:
    while True:
      self.update()


class GameApp:
  def __init__(self) -> None:
    self.engine = Engine.create(BuildConfig)
    self.input = self.engine.input
    self.window = self.engine.window

    self.game_manager = GameManager()
    scene = GameScene(self.window.display)

    self.game_manager.load_scene(scene)

  def run(self) -> None:
    while True:
      delta_time = self.engine.window.get_dt()
      self.engine.update()
      self.game_manager.update(delta_time)
      self.game_manager.render()

      if self.input.pressed(key_mappings.GameMapping.DOWN):
        print('DOWN')
      if self.input.pressed(key_mappings.GameMapping.MOUSE_LEFT):
        print('MOUSE_LEFT')
        print(self.input.mouse.position)

    # self.game_manager.clean_up()


if __name__ == '__main__':
  # EngineTester().run()
  GameApp().run()
  # GameApp()
