def send_email(
    smtp_server: str,
    smtp_port: int,
    smtp_username: str,
    smtp_password: str,
    to_address: str,
    subject: str = "",
    body: str = "",
) -> None:
    print(f"Connecting to {smtp_server}:{smtp_port} with username {smtp_username} and password {smtp_password}.")
    print(f"Sending email to {to_address} with subject '{subject}'")
    print(body)