from src.PyEng.components.game.builtin.shape_render import SquareRenderer
from src.PyEng.components.game.game_component import BaseGameComponent


class Tile(BaseGameComponent):
  base_colour = (200, 0, 0)
  offset_colour = (100, 0, 0)
  highlight_colour = (0, 100, 0)

  def start(self) -> None:
    super().start()
    self.renderer = self.get_component(SquareRenderer)

  def update(self, dt: float) -> None:
    pass

  def update_colour(self, is_offset: bool) -> None:
    if is_offset:
      self.renderer.colour = self.offset_colour
    else:
      self.renderer.colour = self.base_colour
    self.original_colour = self.renderer.colour

  def on_mouse_enter(self) -> None:
    # should change render colour
    self.renderer.colour = self.highlight_colour

  def on_mouse_exit(self) -> None:
    # should change render colour back to original
    self.renderer.colour = self.original_colour
