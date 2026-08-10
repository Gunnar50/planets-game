from prototype.content.custom.player_movement import PlayerMovement
from prototype.main.game_state import RenderGroup
from pyeng.components.game.builtin.shape_render import SpriteRenderer
from pyeng.components.game.prefab import Prefab


class PlayerPrefab(Prefab):
  """
  Reusable Player template. Mirrors a Unity Prefab asset.
  Instantiate this anywhere to get a fully wired-up player.

  Usage:
      player = PlayerPrefab().create(x=100, y=300)
      scene.add_object(player)
  """

  # Should have create method to create prefab from a json file
  def initialise_components(
    self,
    speed: int = 200,
    health: int = 100,
    **kwargs,
  ) -> None:
    # Visual
    self.add_component(
      SpriteRenderer(
        image_name='player',
        render_group=RenderGroup.GAME,
      )
    )

    # Behaviour scripts
    self.add_component(PlayerMovement(speed=speed))
    # obj.add_component(Health(max_health=health))
