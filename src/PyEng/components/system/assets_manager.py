import pathlib

import pygame

from src.Game.repository.game_files import GameFiles
from src.PyEng.components.system.system_component import SystemComponent
from src.shared.debug import Logger


class AssetsManager(SystemComponent):
  def __init__(self) -> None:
    SystemComponent.__init__(self)

    # Maps a clean filename string to its pathlib.Path object
    self._path_registry: dict[str, pathlib.Path] = {}

    # Has the active Pygame Surfaces loaded into memory
    self._texture_cache: dict[str, pygame.Surface] = {}

    # Supported engine image formats
    self._valid_extensions = {'.png', '.jpg', '.jpeg', '.bmp', '.webp'}
    self._scan_assets(GameFiles.get_entities_folder())

  def _scan_assets(self, assets_folder: pathlib.Path) -> None:
    if not assets_folder.exists():
      Logger.error(f'[AssetManager] Asset directory not found: {assets_folder}')
      return

    self._load_folder(assets_folder)
    Logger.info(
      f'[AssetManager] Indexing complete. Registered {len(self._path_registry)} assets.'
    )

  def _load_folder(self, current_folder: pathlib.Path):
    for item in current_folder.iterdir():
      if item.is_dir():
        # Dig deeper into the subfolder
        self._load_folder(item)
      elif item.is_file() and item.suffix.lower() in self._valid_extensions:
        # Map its filename stem (name without extension) to its path
        asset_key = item.stem

        # Basic duplicate handling warning
        if asset_key in self._path_registry:
          Logger.warning(
            f"[AssetManager] Duplicate asset key detected: '{asset_key}'. Overwriting path mapping."
          )

        self._path_registry[asset_key] = item

  def load_image(self, key: str) -> pygame.Surface:
    # Check RAM Cache
    if key in self._texture_cache:
      return self._texture_cache[key]

    # Check Registry for the path
    file_path = self._path_registry.get(key)
    if not file_path:
      Logger.error(
        f"[AssetManager] No asset named '{key}' exists anywhere in project!"
      )
      raise KeyError(f'Asset not found: {key}')

    # Load the image
    Logger.info(f'[AssetManager] Lazy-loading asset to cache: {file_path}')
    raw_surface = pygame.image.load(file_path)
    optimized_surface = raw_surface.convert_alpha()
    # If is a tiled game we might want to scale the images with the tile size
    # optimized_surface = pygame.transform.scale(
    #   optimized_surface, (BuildConfig.tile_width, BuildConfig.tile_height)
    # )

    self._texture_cache[key] = optimized_surface
    return optimized_surface

  def clear_cache(self) -> None:
    self._texture_cache.clear()
    Logger.info('[AssetManager] RAM Texture cache cleared successfully.')
