from typing import Any


class Logger:
  @staticmethod
  def info(message: Any = ''):
    print(f'INFO: {message}')

  @staticmethod
  def warning(message):
    print(f'WARNING: {message}')

  @staticmethod
  def error(message):
    print(f'ERROR: {message}')
