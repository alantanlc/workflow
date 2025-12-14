import logging

from src.framework.workflow import Workflow
from src.action.sample.happy_action import HappyAction
from src.action.sample.exception_action import ExceptionAction
from src.action.sample.not_executable_action import NotExecutableAction
from src.action.sample.happy_error_action import HappyErrorAction

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s"
)

def main():
    logging.info("Main start\n")

    # actions
    actions = [
        HappyAction(),
        ExceptionAction(),
        NotExecutableAction(),
        HappyErrorAction(),
    ]

    # workflow
    workflow = Workflow()
    workflow.actions = actions
    workflow.execute()
    
    logging.info("Main end")


if __name__ == "__main__":
    main()
