from abc import ABC, abstractmethod
from datetime import datetime
from src.framework.context import Context
from src.framework.telemetry import Telemetry

class AbstractAction(ABC):
    is_error: bool = False

    def __init__(self) -> None:
        self.telemetry: Telemetry = Telemetry(self.__class__.__name__)

    def is_executable(self, context: Context) -> bool:
        """ check if action is executable """
        return True

    @abstractmethod
    def execute(self, context: Context) -> None:
        """ execute action """
        pass

    def handle_error(self, context: Context) -> None:
        """ handle error """
        pass

