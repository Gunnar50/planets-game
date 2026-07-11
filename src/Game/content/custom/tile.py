from src.PyEng.components.game.builtin.shape_render import SquareRenderer
from src.PyEng.components.game.game_component import BaseGameComponent


class Tile(BaseGameComponent):
  def start(self) -> None:
    super().start()
    print(f'Tile {self.transform.position.x}, {self.transform.position.y}')

  def update(self, dt: float) -> None:
    pass

  def init(self) -> None:
    renderer = self.get_game_obj().get_component(SquareRenderer)
    renderer.colour
