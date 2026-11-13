import string

def check_password_strength(password):

    score = 0
    feedback = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    # Check uppercase letters
    if any(ch.isupper() for ch in password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Check lowercase letters
    if any(ch.islower() for ch in password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Check numbers
    if any(ch.isdigit() for ch in password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Check special characters
    if any(ch in string.punctuation for ch in password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    # Classify password strength
    print("\nPassword Strength:")

    if score <= 2:
        print("Weak Password")
    elif score <= 4:
        print("Medium Password")
    else:
        print("Strong Password")

    # Display feedback
    if feedback:
        print("\nSuggestions to improve your password:")
        for suggestion in feedback:
            print("-", suggestion)
    else:
        print("Excellent! Your password meets all requirements.")


# Main program
password = input("Enter your password: ")

check_password_strength(password)