from src.Game.content.custom.player_movement import PlayerMovement
from src.Game.main.game_state import RenderGroup
from src.PyEng.components.game.builtin.shape_render import SquareRenderer
from src.PyEng.components.game.game_object import GameObject
from src.PyEng.components.game.prefab import Prefab


class PlayerPrefab(Prefab):
  """
  Reusable Player template. Mirrors a Unity Prefab asset.
  Instantiate this anywhere to get a fully wired-up player.

  Usage:
      player = PlayerPrefab().instantiate(x=100, y=300)
      scene.add_object(player)
  """

  # Should have create method to create prefab from a json file

  def create(self, speed=200, health=100, **kwargs) -> GameObject:
    obj = GameObject('Player')
    obj.tag = 'Player'

    # Transform is already added in GameObject.__init__
    obj.transform.position = self.position
    # TODO: Add rotation

    # Visual — swap ShapeRenderer for SpriteRenderer when you have art
    obj.add_component(
      SquareRenderer(
        render_group=RenderGroup.GAME,
        colour=(100, 180, 255),
        width=32,
        height=32,
      )
    )

    # Behaviour scripts
    obj.add_component(PlayerMovement(speed=speed))
    # obj.add_component(Health(max_health=health))

    return obj
