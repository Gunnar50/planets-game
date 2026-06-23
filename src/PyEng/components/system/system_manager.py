from typing import Any, TYPE_CHECKING

from src.shared import exceptions
from src.shared.debug import Logger

if TYPE_CHECKING:
  from src.Game.main.game_manager import GameManager
  from src.PyEng.components.system.input import Input
  from src.PyEng.components.system.system_component import SystemComponent
  from src.PyEng.components.system.window import Window


class SystemManager:
  """SystemManager

  This is a singleton component that handles all the system and game components
  """

  __instance: 'SystemManager | None' = None

  def __new__(cls, *args, **kwargs) -> 'SystemManager':
    if cls.__instance is None:
      cls.__instance = super().__new__(cls)
    return cls.__instance

  def __init__(self):
    self.system_components_by_name = {}

  def add_element(self, component: 'SystemComponent') -> None:
    # Prevent duplicates of the system elements
    if component.class_name not in self.system_components_by_name.keys():
      Logger.info(f'Adding component: {component!r}')
      self.system_components_by_name[component.class_name] = component
    else:
      raise exceptions.ComponentDuplicateError(
        f'Duplicate system component: {component.class_name!r}'
      )

  def update(self) -> None:
    for component in self.system_components_by_name.values():
      component.update()

  def get_system_components(self):
    return self.system_components_by_name.values()

  # TODO find a way to return correct type
  def get_by_class(self, class_name: str) -> Any:
    if class_name.lower() not in self.system_components_by_name.keys():
      raise exceptions.ComponentNotFoundError(
        f'Class name not found: {class_name}'
      )

    component = self.system_components_by_name[class_name.lower()]
    return component

  def get_game_manager(self) -> 'GameManager':
    name = 'GameManager'
    if name.lower() not in self.system_components_by_name.keys():
      raise exceptions.ComponentNotFoundError(f'Class name not found: {name!r}')

    component = self.system_components_by_name[name.lower()]
    return component

  def get_window(self) -> 'Window':
    name = 'Window'
    if name.lower() not in self.system_components_by_name.keys():
      raise exceptions.ComponentNotFoundError(f'Class name not found: {name!r}')

    component = self.system_components_by_name[name.lower()]
    return component

  def get_input(self) -> 'Input':
    name = 'Input'
    if name.lower() not in self.system_components_by_name.keys():
      raise exceptions.ComponentNotFoundError(f'Class name not found: {name!r}')

    component = self.system_components_by_name[name.lower()]
    return component


system_manager = SystemManager()
