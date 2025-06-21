# main.py
# Entry point for the Vietnamese Text Readability Streamlit app.
# This script sets up the UI and handles user interaction.

import streamlit as st
import streamlit_authenticator as stauth
import bcrypt
from FE.components import render_title, render_input_area, render_submit_button, render_result, render_login, render_register, render_logout, render_history
from FE.api import analyze_text, login_user, register_user, get_history

def main():
    """
    Main function to run the Streamlit app.
    """
    st.set_page_config(page_title="Vietnamese Text Readability", page_icon="📚")
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
    if 'username' not in st.session_state:
        st.session_state['username'] = ''
    if not st.session_state['logged_in']:
        tab = st.sidebar.radio("Tài khoản", ["Đăng nhập", "Đăng ký"])
        if tab == "Đăng nhập":
            user, pwd = render_login()
            if st.button("Đăng nhập"):
                if login_user(user, pwd):
                    st.session_state['logged_in'] = True
                    st.session_state['username'] = user
                    st.success("Đăng nhập thành công!")
                else:
                    st.error("Sai tài khoản hoặc mật khẩu.")
        else:
            user, pwd = render_register()
            if st.button("Đăng ký"):
                if register_user(user, pwd):
                    st.success("Đăng ký thành công! Hãy đăng nhập.")
                else:
                    st.error("Tài khoản đã tồn tại hoặc lỗi đăng ký.")
        return
    else:
        render_logout()
        if st.button("Đăng xuất"):
            st.session_state['logged_in'] = False
            st.session_state['username'] = ''
            st.experimental_rerun()
        st.sidebar.write(f"Xin chào, {st.session_state['username']}")
        if st.sidebar.button("Lịch sử"):
            history = get_history(st.session_state['username'])
            render_history(history)
            st.stop()
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
