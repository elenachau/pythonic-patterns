from typing import Any, Protocol


class Task(Protocol):
    def run(self) -> None:
        """Runs the task."""


class TaskFactory(Protocol):
    def create(self, args: dict[str, Any]) -> Task:
        """Create a new task."""


class TaskRegistry:
    def __init__(self) -> None:
        self.registry: dict[str, TaskFactory] = {}

    def register(self, task_type: str, factory: TaskFactory) -> None:
        self.registry[task_type] = factory

    def unregister(self, task_type: str) -> None:
        self.registry.pop(task_type, None)

    def create(self, args: dict[str, Any]) -> Task:
        args_copy = args.copy()
        task_type = args_copy.pop("type")
        factory = self.registry[task_type]
        return factory.create(args_copy)
