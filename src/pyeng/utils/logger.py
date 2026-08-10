from typing import Any


class Logger:
  @staticmethod
  def info(message: Any) -> None:
    print(f'INFO: {message}')

  @staticmethod
  def warning(message: Any) -> None:
    print(f'WARNING: {message}')

  @staticmethod
  def error(message: Any) -> None:
    print(f'ERROR: {message}')

  @staticmethod
  def debug(message: Any) -> None:
    print(f'DEBUG: {message}')
