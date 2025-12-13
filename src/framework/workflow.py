from typing import List
from dataclasses import dataclass, field
import logging
import traceback
from context import Context
from abstract_action import AbstractAction

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s"
)

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
            is_error = None

            # execute
            is_executable = action.is_executable(self.context)
            if is_executable:
                try:
                    is_error = action.execute(self.context)
                except Exception as e:
                    traceback.print_exc() 
                    logging.error(f"Workflow :: execute :: exception :: {action=}, {exception=}, {context=}")
                    is_error = True
                    action.handle_error(self.context)
            else:
                logging.warn(f"Workflow :: execute :: skipped :: {action_name} is skipped, {is_executable=}, {context=}")

            # telemetry
            action.telemetry.is_error = is_error
            action.telemetry.end()
            time_taken = action.telemetry.time_taken
            logging.info(f"Workflow :: execute :: end :: {action_name=}, {is_executable=}, {is_error=}, {time_taken=}\n")
            
