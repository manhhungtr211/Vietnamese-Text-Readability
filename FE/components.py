# FE/components.py
# Contains UI rendering functions for the Streamlit frontend.

import streamlit as st

def render_title():
    """
    Render the main title and caption for the app.
    """
    st.title("Vietnamese Text Readability")
    st.caption("Phân loại độ khó văn bản tiếng Việt + tô đậm từ khó (demo)")

def render_input_area():
    """
    Render a text area for user to input Vietnamese text.
    Returns:
        str: The input text from the user.
    """
    return st.text_area("Nhập văn bản tiếng Việt cần đánh giá:", height=200)

def render_submit_button():
    """
    Render the submit button for analyzing text.
    Returns:
        bool: True if the button is clicked, else False.
    """
    return st.button("Phân tích độ khó")

def render_result(response):
    """
    Render the analysis result or error message.
    Args:
        response (dict): The response from the backend API.
    """
    if "error" in response:
        st.error(response["error"])
        return

    st.subheader("📊 Kết quả phân tích")
    st.markdown(f"**Mức độ khó:** `{response['difficulty']}`")

    if "highlighted_text" in response:
        st.markdown("**🔍 Văn bản với từ khó được tô đậm:**")
        st.markdown(response["highlighted_text"], unsafe_allow_html=True)
