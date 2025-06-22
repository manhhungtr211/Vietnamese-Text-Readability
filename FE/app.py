# FE/app.py
import streamlit as st
import time
from components import (
    render_title, render_input_area, render_submit_button,
    render_result, render_login, render_register,
    render_history, render_topbar
)
from api import (
    analyze_text, login_user, register_user,
    get_history
)

def main():
    st.set_page_config(
        page_title="Vietnamese Text Readability", 
        page_icon="📚",
        layout="wide"
    )

    st.markdown("""
    <style>
        div.stButton > button {
            min-width: 120px;
            padding: 0.5rem 1rem;
            margin: 0.2rem;
        }
        .stAlert {
            z-index: 1000;
        }
    </style>
    """, unsafe_allow_html=True)

    # Khởi tạo session_state
    for key, default in {
        'logged_in': False,
        'username': '',
        'session_id': None,
        'conversation_id': None,
        'full_name': '',
        'show_login_success': False,
        'show_history': False,
        'confirming_logout': False
    }.items():
        if key not in st.session_state:
            st.session_state[key] = default

    # ======== Hiển thị thông báo đăng nhập thành công ========
    if st.session_state.get('show_login_success', False):
        st.success("Đăng nhập thành công! Đang chuyển hướng...")
        time.sleep(3)
        st.session_state['show_login_success'] = False
        st.rerun()

    # ======== TOPBAR ========
    logout_clicked, history_clicked = render_topbar(
        st.session_state['username'],
        st.session_state['full_name'],
        st.session_state['logged_in']
    )

    # ======== Lịch sử ========
    if history_clicked:
        st.session_state["show_history"] = True

    if st.session_state["show_history"]:
        history = get_history(st.session_state["session_id"])
        render_history(history)
        st.stop()

    # ======== Xác nhận đăng xuất ========
    if st.session_state['logged_in'] and logout_clicked:
        st.session_state['confirming_logout'] = True

    if st.session_state['confirming_logout']:
        st.warning("Bạn có muốn đăng xuất?")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Có", key="confirm_logout"):
                for key in ['logged_in', 'username', 'session_id', 'conversation_id', 'full_name']:
                    st.session_state[key] = '' if isinstance(st.session_state[key], str) else None
                st.session_state['logged_in'] = False
                st.session_state['confirming_logout'] = False
                st.success("Đang chuyển hướng về màn hình đăng nhập...")
                time.sleep(2)
                st.rerun()
        with col2:
            if st.button("Không", key="cancel_logout"):
                st.session_state['confirming_logout'] = False
                st.rerun()

    # ======== Đăng nhập / Đăng ký ========
    if not st.session_state['logged_in']:
        tab = st.radio("Tài khoản", ["Đăng nhập", "Đăng ký"], horizontal=True)
        if tab == "Đăng nhập":
            user, pwd = render_login()
            if st.button("Đăng nhập", key="login_btn"):
                resp = login_user(user, pwd)
                if resp.get("success"):
                    st.session_state['logged_in'] = True
                    st.session_state['username'] = user
                    st.session_state['session_id'] = resp.get("session_id")
                    st.session_state['full_name'] = resp.get("full_name", "")
                    st.session_state['show_login_success'] = True
                    st.rerun()
                else:
                    st.error(resp.get("message", "Sai tài khoản hoặc mật khẩu."))
        else:
            user, full_name, pwd = render_register()
            if st.button("Đăng ký", key="register_btn"):
                resp = register_user(user, full_name, pwd)
                if resp.get("success"):
                    st.success("Đăng ký thành công! Hãy đăng nhập.")
                    time.sleep(2)
                    st.rerun()
                else:
                    st.error(resp.get("message", "Tài khoản đã tồn tại hoặc lỗi đăng ký."))
        return

    # ======== Giao diện chính ========
    render_title()
    text = render_input_area()
    if render_submit_button():
        if not text.strip():
            st.warning("Vui lòng nhập văn bản trước khi gửi.")
        else:
            with st.spinner("Đang phân tích..."):
                result = analyze_text(
                    text,
                    session_id=st.session_state['session_id'],
                    conversation_id=st.session_state['conversation_id']
                )
                if isinstance(result, dict) and result.get("conversation_id"):
                    st.session_state['conversation_id'] = result["conversation_id"]
                render_result(result)

if __name__ == "__main__":
    main()
