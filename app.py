import streamlit as st
import re
import random
import string

# Blacklist of common weak passwords
blacklist = ["password", "123456", "12345678", "qwerty", "password123", "admin", "letmein"]

def check_password_strength(password):
    score = 0
    feedback = []

    if password.lower() in blacklist:
        feedback.append("❌ Password is too common. Choose something more unique.")
        return 1, feedback

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    return score, feedback

def rate_strength(score):
    if score >= 4:
        return "✅ Strong Password!"
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features."
    else:
        return "❌ Weak Password - Improve it using the suggestions above."

def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(length))

# Streamlit UI
st.title("🔐 Password Strength Meter")
st.write("Check how secure your password is and get improvement tips!")

password_input = st.text_input("Enter your password", type="password")

if password_input:
    score, feedback = check_password_strength(password_input)
    st.markdown(f"**Strength Score:** {score}/4")
    st.markdown(f"**Assessment:** {rate_strength(score)}")

    if feedback:
        st.subheader("Suggestions to Improve:")
        for tip in feedback:
            st.write(tip)

    if score < 4:
        st.subheader("🔁 Suggestion")
        st.write("Try this strong password example:")
        st.code(generate_strong_password())

