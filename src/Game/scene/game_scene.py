import pygame

from src.Game.content.prefabs.grid import GridPrefab
from src.Game.content.prefabs.player import PlayerPrefab
from src.PyEng.components.system.game_manager import Scene


class GameScene(Scene):
  """
  The main gameplay scene.
  Build the world here — spawn objects, load maps, configure camera.
  """

  def __init__(self):
    Scene.__init__(self, 'GameScene')

  def load(self):
    """Populate the scene with GameObjects."""

    # Spawn player via prefab
    GridPrefab().create()
    PlayerPrefab(speed=200).create(position=pygame.Vector2(100, 100))

    # Spawn some enemies
    # for i in range(3):
    #   enemy = EnemyPrefab().create(x=300 + i * 120, y=300)
    #   self.add_object(enemy)

    # TODO: load tilemap, background, UI, etc.
