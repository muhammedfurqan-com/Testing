import streamlit as st

# Read from secrets
admin_user = st.secrets["admin"]["username"]
admin_pass = st.secrets["admin"]["password"]

st.title("🔑 Secrets Test")

# Simple login form
username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username == admin_user and password == admin_pass:
        st.success("✅ Logged in as admin")
    else:
        st.error("❌ Invalid username or password")
