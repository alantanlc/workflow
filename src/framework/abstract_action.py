from abc import ABC, abstractmethod
from datetime import datetime
from src.framework.context import Context
from src.framework.telemetry import Telemetry

class AbstractAction(ABC):
    telemetry: Telemetry = None
    is_error: bool = False

    def __init__(self, action_name: str) -> None:
        self.telemetry: Telemetry = Telemetry(action_name)

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

