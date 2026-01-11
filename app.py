from flask import Flask, render_template, request
import re
import random
import string

app = Flask(__name__)

def analyze_password(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters")

    if re.search("[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters")

    if re.search("[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters")

    if re.search("[0-9]", password):
        score += 1
    else:
        suggestions.append("Add numbers")

    if re.search("[!@#$%^&*()]", password):
        score += 1
    else:
        suggestions.append("Add special characters")

    if score <= 2:
        strength = "Weak"
    elif score == 3:
        strength = "Medium"
    else:
        strength = "Strong"

    return score, strength, suggestions


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    generated_password = None

    if request.method == "POST":
        if "check" in request.form:
            password = request.form.get("password", "")
            score, strength, suggestions = analyze_password(password)
            result = {
                "score": score,
                "strength": strength,
                "suggestions": suggestions
            }

        if "generate" in request.form:
            chars = string.ascii_letters + string.digits + "!@#$%^&*()"
            generated_password = "".join(random.choice(chars) for _ in range(12))

    return render_template(
        "index.html",
        result=result,
        generated_password=generated_password
    )


if __name__ == "__main__":
    app.run(debug=True)