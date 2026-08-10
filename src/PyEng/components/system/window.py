import time

import pygame

from prototype.main.configs.build_config import BuildConfig
from prototype.main.game_state import RenderGroup
from PyEng.components.system.system_component import SystemComponent


class Window(SystemComponent):
  """
  Window class

  Create a pygame window and it has the windows methods such as get_dt, update,
  clear, swap_buffers, etc...
  """

  def __init__(
    self,
    window_width: int,
    window_height: int,
    fullscreen: int,
    caption: str,
    fps: int,
    vsync: bool,
    background_colour: tuple[int, int, int],
  ):
    SystemComponent.__init__(self)
    pygame.init()
    self.delta_time = 0.0
    self.fps_cap = fps
    self.frame_log: list[float] = []
    self.background_colour = background_colour
    self.window_width = window_width
    self.window_height = window_height
    self.start_time = time.time()

    # Main surface where all other surfaces gets blit to
    self.screen = pygame.display.set_mode(
      size=(window_width, window_height), flags=fullscreen, vsync=vsync
    )
    self.blit_func = self.screen.blit
    # Game display
    self.game_display = pygame.Surface(
      (
        window_width // BuildConfig.scale_factor,
        window_height // BuildConfig.scale_factor,
      )
    ).convert_alpha()

    # Debug display
    self.debug_display = pygame.Surface(
      (window_width, window_height)
    ).convert_alpha()
    self.display_map = {
      RenderGroup.GAME: self.game_display,
      RenderGroup.DEBUG: self.debug_display,
    }

    pygame.display.set_caption(caption)
    self.clock = pygame.time.Clock()

    self.previous_frame = time.time()

  def get_fps(self) -> float:
    return len(self.frame_log) / sum(self.frame_log)

  def get_width(self) -> int:
    return self.window_width

  def get_height(self) -> int:
    return self.window_height

  def update(self) -> None:
    self.clock.tick(self.fps_cap)

    # Calculate delta time
    self.delta_time = time.time() - self.previous_frame
    self.previous_frame = time.time()
    self.frame_log.append(self.delta_time)
    self.frame_log[-self.fps_cap :]

    self.swap_buffers()
    self.clear()

  def clear(self) -> None:
    self.game_display.fill(self.background_colour)
    self.debug_display.fill((0, 0, 0, 0))

  def swap_buffers(self) -> None:
    scaled_display = pygame.transform.scale(
      self.game_display, self.screen.get_size()
    )
    self.blit_func(scaled_display, (0, 0))
    self.blit_func(self.debug_display, (0, 0))
    pygame.display.flip()
