# main.py
# Entry point for the Vietnamese Text Readability Streamlit app.
# This script sets up the UI and handles user interaction.

import streamlit as st
from FE.components import render_title, render_input_area, render_submit_button, render_result
from FE.api import analyze_text

def main():
    """
    Main function to run the Streamlit app.
    """
    st.set_page_config(page_title="Vietnamese Text Readability", page_icon="📚")

    render_title()

    text = render_input_area()

    if render_submit_button():
        if not text.strip():
            st.warning("Vui lòng nhập văn bản trước khi gửi.")
        else:
            with st.spinner("Đang phân tích..."):
                result = analyze_text(text)
                render_result(result)

if __name__ == "__main__":
    main()
