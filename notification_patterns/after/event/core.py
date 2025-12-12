from typing import Callable
from lib.db import User

# define an event handler type
EventHandler = Callable[[User], None]  # make user dependent

# define the list of subscribers
subscribers: dict[str, list[EventHandler]] = {}

def subscribe(event_type: str, handler: EventHandler) -> None:
    if event_type not in subscribers:
        subscribers[event_type] = [] # no event type yet
    subscribers[event_type].append(handler)

def post_event(event_type: str, user: User) -> None:
    # sent event to all handler functions
    if event_type not in subscribers:
        return
    for handler in subscribers[event_type]:
        handler(user)