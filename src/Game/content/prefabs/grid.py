from src.Game.content.custom.grid_manager import GridManager
from src.PyEng.components.game.prefab import Prefab


class GridPrefab(Prefab):
  def initialise_components(self, **kwargs) -> None:
    self.add_component(GridManager(2, 2))
