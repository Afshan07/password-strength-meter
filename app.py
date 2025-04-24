import streamlit as st
from password_checker import check_password_strength  # agar use kar rahe ho

st.title("Password Strength Meter")
password = st.text_input("Enter your password", type="password")

if password:
    score, suggestions = check_password_strength(password)
    st.write(f"Password score: {score}/5")
    st.write("Suggestions:")
    for s in suggestions:
        st.write("-", s)
