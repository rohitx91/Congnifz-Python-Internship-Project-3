# Level 1 - Task 3

def validate_email(email):
    """
    Validates an email address based on basic rules.

    Args:
        email (str): The email address to validate.

    Returns:
        str: A message indicating if the email is valid or the reason it's invalid.
    """
    # Remove leading and trailing whitespace
    email = email.strip()

    # Check for the presence of '@' symbol
    if "@" not in email:
        return "Invalid email: Missing '@' symbol."

    # Split the email into username and domain parts
    parts = email.split("@")

    # Ensure there is exactly one '@' symbol
    if len(parts) != 2:
        return "Invalid email: More than one '@' symbol."

    username, domain = parts

    # Validate the username part: must not be empty
    if not username:
        return "Invalid email: Nothing before '@'."

    # Validate the domain part: must contain a dot and be at least 3 characters long
    if len(domain) < 3:
        return "Invalid email: Domain name is too short."

    if "." not in domain:
        return "Invalid email: Domain must contain a dot."

    # Additional check: ensure the dot is not at the start or end of the domain
    if domain.startswith(".") or domain.endswith("."):
        return "Invalid email: Domain cannot start or end with a dot."

    # If all checks pass, the email is valid
    return "Valid email address!"

# Main program execution
if __name__ == "__main__":
    # Prompt the user for input
    user_email = input("Enter your email: ")
    # Validate and display the result
    result = validate_email(user_email)
    print(result)
