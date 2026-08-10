from Game.content.custom.tile import Tile
from PyEng.components.game.builtin.shape_render import SquareRenderer
from PyEng.components.game.prefab import Prefab


class TilePrefab(Prefab):
  def initialise_components(
    self,
    cell_width: int = 100,
    cell_height: int = 100,
    **kwargs,
  ) -> None:
    # Visual
    self.add_component(
      SquareRenderer(
        colour=(100, 0, 0),
        width=cell_width,
        height=cell_height,
      )
    )

    # Behaviour Scripts
    self.add_component(Tile())
