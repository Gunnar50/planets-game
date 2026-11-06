import enum

import pydantic
import pygame

from pyeng.utils.types import Coordinate


class RenderObjects(pydantic.BaseModel):
  image: pygame.Surface
  position: Coordinate
  destination_surface: pygame.Surface
  layer: int

  # This is to allow pygame.Surface to be passed as a type
  model_config = pydantic.ConfigDict(arbitrary_types_allowed=True)


class InputMappings(pydantic.BaseModel):
  label: str
  input_id: int


class InputConfig(pydantic.BaseModel):
  config: list[InputMappings]


class TileType(enum.Enum):
  GRASS = 'grass'
  DIRT = 'dirt'
  BUSH = 'bush'
