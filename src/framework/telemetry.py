from datetime import datetime

class Telemetry:
    action_name: str = None
    is_error: bool = False
    time_taken: int = 0
    created: datetime = None
    updated: datetime = None

    def __init__(self, action_name: str) -> None:
        self.action_name = action_name

    def start(self) -> None:
        self.created = datetime.now()

    def end(self) -> None:
        self.updated = datetime.now()
        self.time_taken = (self.updated - self.created).total_seconds()
