import pygame

from prototype.main.configs.build_config import BuildConfig
from prototype.scene.game_scene import GameScene
from PyEng.components.system.game_manager import GameManager
from PyEng.main.engine import Engine
from PyEng.utils import key_mappings

if not pygame.IS_CE:
  raise Exception('Not running Pygame-CE')


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
    scene = GameScene()

    self.game_manager.load_scene(scene)

  def run(self) -> None:
    while True:
      delta_time = self.engine.window.delta_time

      # Events/Inputs
      if self.input.pressed(key_mappings.GameMapping.DOWN):
        print('DOWN')
      if self.input.pressed(key_mappings.GameMapping.MOUSE_LEFT):
        print('MOUSE_LEFT')
        print(self.input.mouse.position)

      # Updates
      self.engine.update()
      self.game_manager.update(delta_time)

      # Cleanup scene (end of update)
      self.game_manager.get_current_scene().cleanup()

      # Render
      self.engine.render()

    # self.game_manager.clean_up()


if __name__ == '__main__':
  # EngineTester().run()
  GameApp().run()
  # GameApp()
