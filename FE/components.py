# FE/components.py
import streamlit as st

def render_title():
    st.title("Vietnamese Text Readability")
    st.caption("Phân loại độ khó văn bản tiếng Việt + tô đậm từ khó (demo)")

def render_input_area():
    return st.text_area("Nhập văn bản tiếng Việt cần đánh giá:", height=200)

def render_submit_button():
    return st.button("Phân tích độ khó")

def render_result(response):
    if "error" in response:
        st.error(response["error"])
        return

    st.subheader("📊 Kết quả phân tích")
    st.markdown(f"**Mức độ khó:** `{response['difficulty']}`")

def render_login():
    user = st.text_input("Tên đăng nhập")
    pwd = st.text_input("Mật khẩu", type="password")
    return user, pwd

def render_register():
    user = st.text_input("Tên đăng ký")
    full_name = st.text_input("Họ tên")
    pwd = st.text_input("Mật khẩu đăng ký", type="password")
    return user, full_name, pwd

def render_history(history):
    st.subheader("🕑 Lịch sử tra cứu")
    if not history:
        st.info("Chưa có lịch sử.")
    else:
        for i, item in enumerate(history[::-1]):
            msg = item.get("message", "")
            reply = item.get("reply", "")
            st.markdown(f"**{i+1}.** <b>Nhập:</b> {msg}<br><b>Kết quả:</b> {reply}", unsafe_allow_html=True)
    if st.button("⬅️ Quay lại", key="back_to_main"):
        st.session_state["show_history"] = False
        st.rerun()

def render_topbar(username, full_name, logged_in):
    """
    Topbar: 3 nút đồng nhất (user info, lịch sử, đăng xuất).
    Trả về tuple: (logout_clicked, history_clicked)
    """
    col_left, col_right = st.columns([7, 3])
    with col_left:
        st.markdown("")

    with col_right:
        if logged_in:
            col1, col2, col3 = st.columns([1, 1, 1])
            with col1:
                st.button(f"👤 {full_name or username}", key="topbar_user_btn", disabled=True)
            with col2:
                history_clicked = st.button("Lịch sử", key="topbar_history_btn")
            with col3:
                logout_clicked = st.button("Đăng xuất", key="topbar_logout_btn")
            return logout_clicked, history_clicked
        else:
            col1, col2, col3 = st.columns([1, 1, 1])
            with col1:
                st.button("🕶️ Chưa đăng nhập", key="topbar_user_btn_disabled", disabled=True)
            with col2:
                st.button("Lịch sử", key="topbar_history_btn_disabled", disabled=True)
            with col3:
                st.button("Đăng xuất", key="topbar_logout_btn_disabled", disabled=True)
            return False, False
