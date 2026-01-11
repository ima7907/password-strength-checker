import re
import random
import string
import sys
from datetime import datetime

# ---------------- UTILITY FUNCTIONS ---------------- #

def banner():
    print("=" * 50)
    print("      ADVANCED PASSWORD SECURITY ANALYZER")
    print("=" * 50)


def get_strength_level(score):
    if score <= 2:
        return "WEAK", "Seconds to Minutes"
    elif score == 3:
        return "MEDIUM", "Hours to Days"
    elif score == 4:
        return "STRONG", "Months to Years"
    else:
        return "VERY STRONG", "Many Years"


def validate_password(password):
    if not password:
        print("❌ Password cannot be empty.")
        sys.exit()

    if len(password) < 6:
        print("❌ Password too short. Minimum 6 characters required.")
        sys.exit()


# ---------------- PASSWORD ANALYSIS ---------------- #

def analyze_password(password):
    score = 0
    feedback = []

    rules = {
        "Length (>= 8)": len(password) >= 8,
        "Uppercase Letter": bool(re.search(r"[A-Z]", password)),
        "Lowercase Letter": bool(re.search(r"[a-z]", password)),
        "Number": bool(re.search(r"\d", password)),
        "Special Character": bool(re.search(r"[!@#$%^&*()]", password)),
    }

    for rule, passed in rules.items():
        if passed:
            score += 1
        else:
            feedback.append(f"Add {rule.lower()}")

    strength, crack_time = get_strength_level(score)

    return {
        "score": score,
        "strength": strength,
        "crack_time": crack_time,
        "feedback": feedback
    }


# ---------------- PASSWORD GENERATOR ---------------- #

def generate_password(length):
    if length < 6:
        print("❌ Password length must be at least 6.")
        sys.exit()

    charset = (
        string.ascii_uppercase +
        string.ascii_lowercase +
        string.digits +
        "!@#$%^&*()"
    )

    return "".join(random.choice(charset) for _ in range(length))


# ---------------- MAIN MENU ---------------- #

def main():
    banner()

    print("1. Analyze Password Strength")
    print("2. Generate Secure Password")
    print("3. Exit")

    choice = input("\nEnter your choice (1/2/3): ")

    if choice == "1":
        password = input("\nEnter password to analyze: ")
        validate_password(password)

        result = analyze_password(password)

        print("\n📊 PASSWORD ANALYSIS REPORT")
        print("-" * 30)
        print(f"Score           : {result['score']} / 5")
        print(f"Strength        : {result['strength']}")
        print(f"Crack Time Est. : {result['crack_time']}")

        if result["feedback"]:
            print("\n🔧 Improvement Suggestions:")
            for tip in result["feedback"]:
                print(" -", tip)
        else:
            print("\n✅ Excellent! Your password follows all security rules.")

    elif choice == "2":
        length = int(input("\nEnter desired password length: "))
        password = generate_password(length)

        print("\n🔑 GENERATED SECURE PASSWORD")
        print("-" * 30)
        print(password)

    elif choice == "3":
        print("\n👋 Exiting program. Stay secure!")
        sys.exit()

    else:
        print("\n❌ Invalid choice. Please restart the program.")


# ---------------- PROGRAM ENTRY ---------------- #

if __name__ == "__main__":
    main()