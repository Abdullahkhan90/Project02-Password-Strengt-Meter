import streamlit as st
import re

# Set up the Streamlit page
st.set_page_config(page_title="Password Strength Meter", page_icon="")
st.title("🔒Password Strength Meter")
st.markdown("""
## Welcome To Abdullah's Password Strength Meter!😊
Use this tool to assess your password strength and receive suggestions to enhance it.
We’ll provide multiple helpful tips to make your **Password More Secure** 🔒
""")

# Input the password
password = st.text_input("Enter Your Password", type="password")

feedback = []
score = 0

if password:
    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Check for uppercase and lowercase letters
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain both uppercase and lowercase letters.")

    # Check for digits
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one digit.")

    # Check for special characters
    if re.search(r'[!@#$%&*]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one special character (!@#$%&*).")

    # Provide overall feedback
    if score == 4:
        feedback.append("✔ Your password is strong!")
    elif score == 3:
        feedback.append("👁‍🗨 Your password is of medium strength. It could be stronger.")
    else:
        feedback.append("🔄 Your password is weak. Please make it stronger.")

else:
    st.info("Please enter your password to get started.")

# Show feedback
if feedback: 
    st.markdown("## Improvement Suggestions")
    for tip in feedback:
        st.write(tip)
