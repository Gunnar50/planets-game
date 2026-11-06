from data.config.input_actions import InputActions
from pyeng.components.game.game_component import BaseGameComponent


class PlayerMovement(BaseGameComponent):
  """
  Custom component
  Reads keyboard input and moves the player each frame.

  Attach to any GameObject to make it player-controlled.
  """

  def __init__(self, speed: float = 200):
    BaseGameComponent.__init__(self)
    self.speed = speed
    input_actions = InputActions()
    input_actions.player.enable()
    self.move = input_actions.player.move
    self.jump = input_actions.player.jump

  def jump_action(self) -> None:
    print('Jump!')

  def start(self) -> None:
    super().start()

  def update(self, dt: float) -> None:
    # Return pygame.Vector2
    direction = self.move.read_value()
    self.transform.translate(
      direction.x * self.speed * dt,
      direction.y * self.speed * dt,
    )

    # Button, check if was pressed this frame
    if self.jump.just_pressed():
      self.jump_action()
