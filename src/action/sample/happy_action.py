import logging
from src.framework.abstract_action import AbstractAction
from src.framework.context import Context

class HappyAction(AbstractAction):
    
    def is_executable(self, context: Context) -> bool:
        return True

    def execute(self, context: Context) -> bool:
        logging.info("HappyAction execute")
        return True
