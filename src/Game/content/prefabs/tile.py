from src.Game.content.custom.tile import Tile
from src.PyEng.components.game.builtin.shape_render import SquareRenderer
from src.PyEng.components.game.prefab import Prefab


class TilePrefab(Prefab):
  base_colour = (200, 0, 0)
  offset_colour = (100, 0, 0)

  def initialise_components(self, **kwargs) -> None:
    # Visual
    self.add_component(
      SquareRenderer(colour=(100, 0, 0), width=100, height=100)
    )

    # Behaviour Scripts
    self.add_component(Tile())
