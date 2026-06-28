import pygame

from src.Game.main.configs.game_config import GameConfig
from src.PyEng.components.game.game_component import BaseGameComponent
from src.shared.types import Colour
from src.shared.types import SortingKey


class Renderer(BaseGameComponent):
  """
  Base renderer component. Subclass for sprite, shape, or tilemap rendering.
  SpriteRenderer, ShapeRenderer, etc. all extend this.
  """

  def __init__(self, sorting_layer: int = 0, order_in_layer: int = 0):
    BaseGameComponent.__init__(self)
    self.position: pygame.Vector2
    self.sorting_layer = sorting_layer
    self.order_in_layer = order_in_layer

    # Sort by layer first, then order in layer, then y position for 2d top view
    if GameConfig.sort_by_y_axis:
      self.sorting_key = self._get_y_sort_key
    else:
      self.sorting_key = self._get_flat_sort_key

  def start(self) -> None:
    super().start()

    # Initialise position
    self.position = self.transform.position

    # Register to the RenderSystem
    self.system_components.get_render().register(self)

  def _get_y_sort_key(self) -> SortingKey:
    return (
      self.sorting_layer,
      self.order_in_layer,
      self.transform.position.y,
    )

  def _get_flat_sort_key(self) -> SortingKey:
    return (self.sorting_layer, self.order_in_layer, 0)

  def bounds(self) -> pygame.Rect:
    """Returns the bounding box of this renderer in world space."""
    raise NotImplementedError

  def draw(self, display: pygame.Surface) -> None:
    raise NotImplementedError


class SquareRenderer(Renderer):
  """Shaper rendering component."""

  def __init__(self, colour: Colour, width: int = 0, height: int = 0):
    Renderer.__init__(self)
    self.colour = colour
    self.width = width
    self.height = height

  def bounds(self) -> pygame.Rect:
    # Returns a Rect corresponding to the square's position and size
    return pygame.Rect(
      self.position.x,
      self.position.y,
      self.width,
      self.height,
    )

  def draw(self, display: pygame.Surface) -> None:
    # Renders the surface relative to the GameObject's transform position
    pygame.draw.rect(
      display,
      self.colour,
      self.bounds(),
    )


class CircleRenderer(Renderer):
  """Circle rendering component."""

  def __init__(self, colour: Colour, radius: float = 0):
    Renderer.__init__(self)
    self.colour = colour
    self.radius = radius
    self.diameter = radius * 2

  def bounds(self) -> pygame.Rect:
    # A circle's bounding box width and height is its diameter (radius * 2)
    # Bounding box top-left needs to be shifted back by the radius
    return pygame.Rect(
      self.position.x - self.radius,
      self.position.y - self.radius,
      self.diameter,
      self.diameter,
    )

  def draw(self, display: pygame.Surface) -> None:
    # Renders the surface relative to the GameObject's transform position
    pygame.draw.circle(
      display,
      self.colour,
      (self.position.x, self.position.y),
      self.radius,
    )


class RenderableSprite:
  # TODO
  def __init__(self, image, x, y, layer=0, order_in_layer=0):
    self.image = image
    self.rect = self.image.get_rect(topleft=(x, y))

    # Unity-like sorting properties
    self.layer = layer
    self.order_in_layer = order_in_layer

    # Cache the sorting key to avoid recalculating it constantly
    self.sorting_key = (self.layer, self.order_in_layer, self.rect.bottom)

  def update_position(self, dx, dy):
    self.rect.x += dx
    self.rect.y += dy
    # If Y-position matters for depth (like a top-down game), update the key
    self.sorting_key = (self.layer, self.order_in_layer, self.rect.bottom)
