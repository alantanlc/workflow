from typing import List
from dataclasses import dataclass, field
import logging
import traceback
from src.framework.context import Context
from src.framework.abstract_action import AbstractAction

@dataclass
class Workflow:
    context: Context = Context()
    actions: List[AbstractAction] = field(default_factory=list)

    def execute(self) -> None:
        """ execute workflow """
        for action in self.actions:
            # init
            action_name = action.__class__.__name__
            action.telemetry.start()

            # execute
            is_executable = action.is_executable(self.context)
            if is_executable:
                try:
                    logging.info(f"{action_name} start")
                    action.execute(self.context)
                    logging.info(f"{action_name} end")
                except Exception as exception:
                    traceback.print_exc() 
                    logging.error(f"Workflow exception {action_name=}, {exception=}, {self.context=}")
                    action.is_error = True
                    action.handle_error(self.context)
            else:
                logging.warn(f"Workflow action skipped {action_name=}, {is_executable=}, {self.context=}")

            # telemetry
            is_error = action.is_error
            action.telemetry.is_error = action.is_error
            action.telemetry.end()
            time_taken = action.telemetry.time_taken
            logging.info(f"Workflow {action_name=}, {is_executable=}, {is_error=}, {time_taken=}\n")
