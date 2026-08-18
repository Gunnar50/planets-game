from unittest import mock

import pygame
import pytest

from pyeng.components.system.system_manager import system_manager
from pyeng.main.engine import Engine
from pyeng.main.engine_config import EngineConfig
from pyeng.utils import exceptions


@pytest.fixture(autouse=True)
def mock_window():
  with mock.patch('pyeng.main.engine.Window', autospec=True) as mock_window:
    pygame.init()
    yield mock_window


@pytest.fixture(autouse=True)
def reset_engine_singleton():
  Engine._Engine__instance = None
  system_manager.system_components_by_name = {}
  yield


class TestEngine:
  configs = EngineConfig

  def test_singleton_behavior(self):
    engine = Engine.create()
    assert isinstance(engine, Engine)

    with pytest.raises(exceptions.IllegalStateException):
      Engine.create()

  def test_get_engine_instance(self):
    engine = Engine.create()
    engine_instance = Engine.get_instance()
    assert engine == engine_instance

  def test_get_instance_no_engine_created(self):
    engine_instance = Engine.get_instance()
    assert isinstance(engine_instance, Engine)

  @mock.patch.object(EngineConfig, 'data_folder', mock.Mock())
  def test_missing_assets_folder(self, mock_data_folder: mock.Mock):
    # Patch data_folder.exists to return False
    mock_data_folder.exists.return_value = False
    with pytest.raises(exceptions.IllegalStateException):
      Engine.create()
