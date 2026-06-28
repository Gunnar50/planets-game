from collections import defaultdict

import pygame

from src.Game.main.game_state import RenderGroup
from src.PyEng.components.game.builtin.shape_render import Renderer
from src.PyEng.components.system.system_component import SystemComponent


class RenderSystem(SystemComponent):
  """Render all the elements in the Window in a Layer format"""

  def __init__(self) -> None:
    SystemComponent.__init__(self)
    self._renderers: dict[RenderGroup, list[Renderer]] = defaultdict(list)

  def register(self, group: RenderGroup, renderer: Renderer) -> None:
    """Called automatically when a Renderer component starts."""
    self._renderers[group].append(renderer)

  def unregister(self, group: RenderGroup, renderer: Renderer) -> None:
    """Called automatically if a GameObject/Component is destroyed."""
    if renderer in self._renderers[group]:
      self._renderers[group].remove(renderer)

  def render(self, display_map: dict[RenderGroup, pygame.Surface]) -> None:
    for group_name, renderers in self._renderers.items():
      target_surface = display_map[group_name]
      screen_rect = target_surface.get_rect()

      render_queue = [
        (render.sorting_key(), render)
        for render in renderers
        if render.enabled
        and render.game_object
        and render.game_object.is_active
        and screen_rect.colliderect(render.bounds())
      ]
      render_queue.sort()

      for _, renderer in render_queue:
        renderer.draw(target_surface)
