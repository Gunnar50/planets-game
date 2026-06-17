import dataclasses

import pygame

from src.Game.main.configs.build_config import BuildConfig
from src.shared.hash_registry import Registrable


@dataclasses.dataclass
class Blueprint(Registrable):
  """
  Name: the unique name for this type of blueprint
  Group: the group this blueprint belongs (eg. tile, entities, crop)
  Layer: the layer that is rendered in (crops are rendered on top of tiles)
  Images: tuple containing the loaded images
  """

  name: str
  group: str
  layer: int
  images: list[pygame.Surface]

  def __post_init__(self):
    # Scale images to the correct tile size
    self.images = [
      pygame.transform.scale(
        image, (BuildConfig.tile_width, BuildConfig.tile_height)
      )
      for image in self.images
    ]

  def get_name(self) -> str:
    return self.name


@dataclasses.dataclass
class EntityBlueprint(Blueprint):
  def create_instance(self):
    raise NotImplementedError


@dataclasses.dataclass
class ItemBlueprint(Blueprint):
  def create_instance(self):
    raise NotImplementedError


@dataclasses.dataclass
class TileBlueprint(Blueprint):
  def create_instance(self):
    raise NotImplementedError
