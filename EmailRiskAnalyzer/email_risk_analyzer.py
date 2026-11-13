import re

def analyze_email(email):

    score = 0
    warnings = []

    # Check urgent words
    urgent_words = [
        "urgent", "immediately", "act now",
        "verify now", "account blocked",
        "limited time", "suspended"
    ]

    for word in urgent_words:
        if word in email.lower():
            score += 1
            warnings.append("Urgent or threatening language detected.")
            break

    # Check suspicious links
    urls = re.findall(r'https?://\S+', email)

    if urls:
        score += 2
        warnings.append("Email contains links. Verify before clicking.")

    # Check sensitive information requests
    sensitive_words = [
        "password", "otp", "bank details",
        "credit card", "pin", "cvv",
        "social security"
    ]

    for word in sensitive_words:
        if word in email.lower():
            score += 3
            warnings.append("Sensitive information request detected.")
            break

    # Check phishing keywords
    phishing_words = [
        "claim your prize",
        "won a lottery",
        "free money",
        "click here",
        "verify your account",
        "congratulations"
    ]

    for word in phishing_words:
        if word in email.lower():
            score += 2
            warnings.append("Potential phishing language detected.")
            break

    # Display results
    print("\n========== EMAIL RISK REPORT ==========")

    if score == 0:
        print("Email Status: SAFE")
        print("Risk Level: LOW")

    elif score <= 3:
        print("Email Status: SUSPICIOUS")
        print("Risk Level: MEDIUM")

    else:
        print("Email Status: DANGEROUS")
        print("Risk Level: HIGH")

    print("\nRisk Score:", score)

    if warnings:
        print("\nSecurity Warnings:")
        for warning in warnings:
            print("-", warning)

    else:
        print("\nNo suspicious patterns detected.")

    print("=======================================")


# Main Program

print("===== EMAIL RISK ANALYZER =====")

print("Enter your email content.")
print("Type END on a new line to finish.")

email_lines = []

while True:
    line = input()

    if line.strip().upper() == "END":
        break

    email_lines.append(line)

email_content = " ".join(email_lines)

analyze_email(email_content)