import logging
from src.framework.abstract_action import AbstractAction
from src.framework.context import Context

class NotExecutableAction(AbstractAction):
    
    def is_executable(self, context: Context) -> bool:
        return False

    def execute(self, context: Context) -> bool:
        logging.info("NotExecutableAction execute")
        return True
