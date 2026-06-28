from typing import Any

import pygame

from src.PyEng.components.system.system_component import SystemComponent


class Debugger(SystemComponent):
  def __init__(self, debug: bool = False) -> None:
    SystemComponent.__init__(self)
    self.debug: dict = {}
    self.debugging = debug
    self.font = pygame.font.SysFont('Consolas', 20)
    self.window = self.system_manager.get_window()

  def render_info(self) -> None:
    for i, key in enumerate(self.debug):
      text = self.font.render(
        f'{key}:{self.debug[key]}', True, (255, 255, 255), (0, 0, 0)
      )
      text_rect = text.get_rect()
      text_rect.x = 0
      text_rect.y = 20 * i
      self.window.debug_display.blit(text, text_rect)

  def add_info(self, key: str, info: Any) -> None:
    self.debug[key] = info

  def register_info(self) -> None:
    self.add_info('FPS', int(self.window.get_fps()))

  def update(self) -> None:
    self.register_info()
    self.render_info()
