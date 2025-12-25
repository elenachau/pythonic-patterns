from typing import Any, Callable

task_functions: dict[str, Callable[..., None]] = {} # takes in any number of arguments


def register(task_type: str, task_fn: Callable[..., None]) -> None:
    task_functions[task_type] = task_fn


def unregister(task_type: str) -> None:
    task_functions.pop(task_type, None)


def run(args: dict[str, Any]) -> None:  # directly run task instead of just create
    args_copy = args.copy()
    task_type = args_copy.pop("type")
    task_functions[task_type](**args_copy)
