import enum

import pydantic

from pyeng.utils import exceptions


class ActionType(str, enum.Enum):
  VECTOR2 = 'vector2'
  VECTOR1 = 'vector1'
  BUTTON = 'button'


class Vector2Mapping(pydantic.BaseModel):
  up: list[int] = pydantic.Field(default_factory=list)
  down: list[int] = pydantic.Field(default_factory=list)
  left: list[int] = pydantic.Field(default_factory=list)
  right: list[int] = pydantic.Field(default_factory=list)


class Vector1Mapping(pydantic.BaseModel):
  positive: list[int] = pydantic.Field(default_factory=list)
  negative: list[int] = pydantic.Field(default_factory=list)


class ActionConfig(pydantic.BaseModel):
  name: str
  vector2: Vector2Mapping | None = None
  vector1: Vector1Mapping | None = None
  button: list[int] | None = None
  action_type: ActionType | None = None

  @pydantic.model_validator(mode='after')
  def _post_validation(self) -> 'ActionConfig':
    types_present = [
      self.vector2 is not None,
      self.vector1 is not None,
      self.button is not None,
    ]
    count = sum(types_present)

    if count == 0:
      raise exceptions.InputSchemaException(
        f'Action {self.name!r} must define one type (vector2, vector1, or button).'
      )
    if count > 1:
      raise exceptions.InputSchemaException(
        f'Action {self.name!r} defines multiple types. Only one type is allowed per action.'
      )

    if self.vector2 is not None:
      self.action_type = ActionType.VECTOR2
    elif self.vector1 is not None:
      self.action_type = ActionType.VECTOR1
    elif self.button is not None:
      self.action_type = ActionType.BUTTON

    return self


class ActionMapConfig(pydantic.BaseModel):
  map_name: str
  actions: list[ActionConfig]
