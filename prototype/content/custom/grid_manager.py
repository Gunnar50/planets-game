from prototype.content.custom.tile import Tile
from prototype.content.prefabs.tile_prefab import TilePrefab
from pyeng.components.game.builtin.grid import Grid


class GridManager(Grid):
  def __init__(self, width: int, height: int):
    Grid.__init__(self)
    self.width, self.height = width, height
    self.tile_prefab = TilePrefab

  def start(self) -> None:
    super().start()
    self.generate_grid()

  def generate_grid(self) -> None:
    for x in range(self.width):
      for y in range(self.height):
        tile = self.tile_prefab(
          cell_width=self.cell_width,
          cell_height=self.cell_height,
        ).create(
          name=f'Tile: {x}, {y}',
          position=self.cell_to_world(cell_coords=(x, y)),
        )
        tile_script = tile.get_component(Tile)
        tile_script.update_colour(is_offset=(x + y) % 2 == 0)
