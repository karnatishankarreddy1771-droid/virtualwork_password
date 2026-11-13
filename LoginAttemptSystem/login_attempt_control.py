import time
import getpass
import hashlib
import hmac

# Login credentials
USERNAME = "admin"

# Store password as a SHA-256 hash (demo only)
PASSWORD_HASH = hashlib.sha256(
    "Admin@123".encode()
).hexdigest()

MAX_ATTEMPTS = 3
LOCK_TIME = 30


def login_system():

    attempts = 0

    while True:

        print("\n===== LOGIN SYSTEM =====")

        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")

        # Hash entered password
        entered_hash = hashlib.sha256(
            password.encode()
        ).hexdigest()

        # Check credentials
        if (username == USERNAME and
                hmac.compare_digest(entered_hash, PASSWORD_HASH)):

            print("\nLogin Successful!")
            print("Welcome,", username)

            attempts = 0
            break

        else:

            attempts += 1

            remaining = MAX_ATTEMPTS - attempts

            print("\nInvalid username or password!")

            if remaining > 0:

                print("Remaining attempts:", remaining)

            else:

                print("\nToo many failed attempts!")
                print("Account temporarily locked.")

                print("Please wait", LOCK_TIME, "seconds.")

                for i in range(LOCK_TIME, 0, -1):
                    print(f"Retry after {i} seconds...", end="\r")
                    time.sleep(1)

                print("\nAccount unlocked!")
                attempts = 0


# Main program
login_system()