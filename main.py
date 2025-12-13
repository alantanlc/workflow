import logging

from src.framework.workflow import Workflow
from src.action.sample_action import SampleAction
from src.action.sample_exception_action import SampleExceptionAction
from src.action.sample_not_executable_action import SampleNotExecutableAction

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s"
)

def main():
    logging.info("Main start\n")

    # actions
    actions = [
        SampleAction(),
        SampleExceptionAction(),
        SampleNotExecutableAction(),
        SampleAction(),
    ]

    # workflow
    workflow = Workflow()
    workflow.actions = actions
    workflow.execute()
    
    logging.info("Main end")


if __name__ == "__main__":
    main()
