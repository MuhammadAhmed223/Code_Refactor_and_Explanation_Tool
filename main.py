import streamlit as st
from refactor import refactor_code
from explain import explain_code

st.title("Code Refactor and Explanation Tool")

code_input = st.text_area("Enter Python code:", height=200)

if st.button("Process Code"):
    if code_input.strip():
        refactored_code = refactor_code(code_input)
        explanation = explain_code(code_input)

        st.subheader("Refactored Code")
        st.code(refactored_code, language="python")

        st.subheader("Code Explanation")
        st.write(explanation)
    else:
        st.warning("Please enter some code before processing.")
