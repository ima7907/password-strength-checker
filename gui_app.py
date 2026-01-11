import tkinter as tk
from tkinter import messagebox
import re
import random
import string

# ---------- FUNCTIONS ----------

def check_strength():
    password = entry.get()

    if not password:
        messagebox.showerror("Error", "Password cannot be empty")
        return

    score = 0
    if len(password) >= 8: score += 1
    if re.search("[A-Z]", password): score += 1
    if re.search("[a-z]", password): score += 1
    if re.search("[0-9]", password): score += 1
    if re.search("[!@#$%^&*()]", password): score += 1

    if score <= 2:
        strength = "WEAK"
        color = "red"
    elif score == 3:
        strength = "MEDIUM"
        color = "orange"
    else:
        strength = "STRONG"
        color = "green"

    result_label.config(text=f"Strength: {strength} ({score}/5)", fg=color)


def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = "".join(random.choice(chars) for _ in range(12))
    entry.delete(0, tk.END)
    entry.insert(0, password)
    result_label.config(text="Generated Secure Password", fg="blue")


# ---------- WINDOW ----------

window = tk.Tk()
window.title("Password Security Analyzer")
window.geometry("420x320")
window.resizable(False, False)

tk.Label(
    window,
    text="Password Security Analyzer",
    font=("Arial", 14, "bold")
).pack(pady=10)

tk.Label(window, text="Enter Password").pack()

entry = tk.Entry(window, width=30, show="*", font=("Arial", 11))
entry.pack(pady=5)

tk.Button(
    window,
    text="Check Strength",
    width=20,
    command=check_strength
).pack(pady=5)

tk.Button(
    window,
    text="Generate Password",
    width=20,
    command=generate_password
).pack(pady=5)

result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=15)

window.mainloop()