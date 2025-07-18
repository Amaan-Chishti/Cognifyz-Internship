import re

def evaluate_password_strength(password):
    strength_score = 0

    # Check length
    if len(password) >= 8:
        strength_score += 1
    else:
        print("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength_score += 1
    else:
        print("Password should include at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength_score += 1
    else:
        print("Password should include at least one lowercase letter.")

    # Check for digits
    if re.search(r'\d', password):
        strength_score += 1
    else:
        print("Password should include at least one digit.")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength_score += 1
    else:
        print("Password should include at least one special character.")

    # Determine strength level
    if strength_score == 5:
        print("Password strength: Strong")
    elif strength_score >= 3:
        print("Password strength: Moderate")
    else:
        print("Password strength: Weak")

# Example usage
user_password = input("Enter your password: ")
evaluate_password_strength(user_password)