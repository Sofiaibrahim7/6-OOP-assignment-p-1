# 📝 Assignment: Logger Class with Constructor and Destructor in Streamlit

## 🎯 Objective:
Build a Streamlit app to demonstrate how constructors and destructors work in a Python class using UI buttons.

---

## ✅ Features:
- Create a `Logger` object with a button click.
- Delete the object manually with another button.
- Constructor message shown in the browser.
- Destructor message shown in the terminal.

---

## 💻 Python Code (app.py):

```python
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

▶️ How to Run:
Save this code as app.py in your project folder.

Open terminal in that folder.

Run the following command:

streamlit run app.py
Open the URL shown in the terminal (usually http://localhost:8501).

🔎 Notes:
The constructor message (__init__) is shown in the browser using Streamlit.

The destructor message (__del__) is shown in the terminal.

📷 Screenshot Example:

[Browser]
✅ Logger object has been created.
⚠️ Logger object deleted. Destructor will run (check terminal).

[Terminal]
Logger object is being destroyed.

