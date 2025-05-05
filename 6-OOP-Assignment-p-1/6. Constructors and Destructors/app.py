import streamlit as st

st.set_page_config(page_title="Logger Constructor & Destructor", layout="centered")

st.title("🔧 Logger Constructor and Destructor Demo")

class Logger:
    def __init__(self):
        st.success("✅ Logger object has been created.")

    def __del__(self):
        print("Logger object is being destroyed (check terminal).")

# Use session state to hold the object
if 'logger' not in st.session_state:
    st.session_state.logger = None

# Button to create Logger
if st.button("Create Logger Object"):
    st.session_state.logger = Logger()

# Button to delete Logger
if st.button("Delete Logger Object"):
    st.session_state.logger = None
    st.warning("⚠️ Logger object deleted. Destructor will run (check terminal).")
