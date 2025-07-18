import re

def is_valid_email(email):
    """
    Validates if a given string is a valid email address.

    Args:
        email (str): The email address string to validate.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

email1 = "test@example.com"
email2 = "invalid-email"
email3 = "another.test@sub.example.co.uk"

print(f'"{email1}" is valid: {is_valid_email(email1)}')
print(f'"{email2}" is valid: {is_valid_email(email2)}')
print(f'"{email3}" is valid: {is_valid_email(email3)}')