import logging
from src.framework.abstract_action import AbstractAction
from src.framework.context import Context

class SampleExceptionAction(AbstractAction):
    
    def is_executable(self, context: Context) -> bool:
        return True

    def execute(self, context: Context) -> bool:
        logging.info("SampleExceptionAction execute")
        raise Exception("Generic exception")
