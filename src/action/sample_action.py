import logging
from src.framework.abstract_action import AbstractAction
from src.framework.context import Context

class SampleAction(AbstractAction):
    
    def is_executable(self, context: Context) -> bool:
        logging.info("SampleAction :: is_executable")
        return True

    def execute(self, context: Context) -> bool:
        logging.info("SampleAction :: execute :: start")
        logging.info("SampleAction :: execute :: end")
        return True
