from src.PyEng.components.system.system_manager import system_manager


class SystemComponent:
  """System components that are singletons.

  Render, Camera, Inputs, Assets, etc.
  """

  __instance = None

  def __new__(cls, *args, **kwargs):
    if cls.__instance is None:
      cls.__instance = super().__new__(cls)
    return cls.__instance

  def __init__(self, custom_id: int | None = None, add=True):
    self.custom_id = custom_id
    self.class_name = self.__class__.__name__.lower()
    self.system_manager = system_manager
    if add:
      system_manager.add_element(self)

  def update(self):
    pass

  def __repr__(self):
    return f'System Component: {self.__class__.__name__!r}'
