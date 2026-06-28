import pygame

from src.PyEng.components.game.builtin.shape_render import Renderer
from src.PyEng.components.system.system_component import SystemComponent


class RenderSystem(SystemComponent):
  """Render all the elements in the Window in a Layer format"""

  def __init__(self) -> None:
    SystemComponent.__init__(self)
    self._renderers: list[Renderer] = []

  def register(self, renderer: Renderer) -> None:
    """Called automatically when a Renderer component starts."""
    self._renderers.append(renderer)

  def unregister(self, renderer: Renderer) -> None:
    """Called automatically if a GameObject/Component is destroyed."""
    if renderer in self._renderers:
      self._renderers.remove(renderer)

  def render(self, display: pygame.Surface) -> None:
    screen_rect = display.get_rect()

    render_queue = [
      (render.sorting_key(), render)
      for render in self._renderers
      if render.enabled
      and render.game_object
      and render.game_object.is_active
      and screen_rect.colliderect(render.bounds())
    ]
    render_queue.sort()

    for _, renderer in render_queue:
      renderer.draw(display)
