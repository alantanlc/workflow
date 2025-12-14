import logging
from src.framework.abstract_action import AbstractAction
from src.framework.context import Context

class HappyErrorAction(AbstractAction):
    
    def is_executable(self, context: Context) -> bool:
        return True

    def execute(self, context: Context) -> bool:
        logging.info("HappyErrorAction execute")
        self.is_error = True
        return True
