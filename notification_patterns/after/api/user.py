# import logging

from lib.db import create_user, find_user
# from lib.email import send_email
# from lib.slack import post_slack_message
from event.core import post_event

# ^ high coupling; dependency is problematic because every time notifications needs to change how it's handled, must update all other func

def register_new_user(name: str, password: str, email: str) -> None:
    # create an entry in the database
    user = create_user(name, password, email)

    # post an event
    post_event("user_registered", user)

    # # post a Slack message to sales department
    # post_slack_message(
    #     "sales",
    #     f"{user.name} has registered with email address {user.email}. Please spam this person incessantly.",
    # )

    # # send a welcome email
    # send_email(
    #     user.name,
    #     user.email,
    #     "Welcome",
    #     f"Thanks for registering, {user.name}!\nRegards, The DevNotes team",
    # )

    # # write server log
    # logging.debug(f"User registered with email address {user.email}")


def password_forgotten(email: str) -> None:
    # retrieve the user
    user = find_user(email)

    # generate a password reset code
    user.init_reset_password()

    # post an event
    post_event("user_password_forgotten", user)

    # # send a password reset message
    # send_email(
    #     user.name,
    #     user.email,
    #     "Reset your password",
    #     f"To reset your password, use this very secure code: {reset_code}.\nRegards, The DevNotes team",
    # )

    # # write server log
    # logging.debug(f"User with email address {user.email} requested a password reset")
