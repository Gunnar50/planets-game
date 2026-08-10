from prototype.content.custom.grid_manager import GridManager
from PyEng.components.game.prefab import Prefab


class GridPrefab(Prefab):
  def initialise_components(
    self,
    width: int = 100,
    height: int = 100,
    **kwargs,
  ) -> None:
    self.add_component(GridManager(width=width, height=height))
