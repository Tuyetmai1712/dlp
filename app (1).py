
import streamlit as st
import time

def typewriter(text, delay=0.05, font_size=22):
    placeholder = st.empty()
    output = ""
    for char in text:
        output += char
        placeholder.markdown(
            f'<p style="font-family:Courier New; font-size:{font_size}px;">{output}</p>',
            unsafe_allow_html=True
        )
        time.sleep(delay)
    time.sleep(1)

def scene_1():
    messages = [
        "Chào mừng bạn đến với DAV Leadership Programme – Summer Course 2025",
        "Một hành trình mới sắp bắt đầu, chúc bạn chân cứng đá mềm",
        "Chị là Phạm Tuyết Mai",
        "Mai trong Hoa Mai",
        "Tuyết trong Bông Tuyết",
        "Phạm là họ bố..và cả ông nội… tất nhiên rồi",
        "Chị sẽ là Instructor đi cùng với em hết hành trình DLP4 này",
        "Cảm ơn vì đã đến"
    ]
    for msg in messages:
        typewriter(msg, delay=0.05)
        time.sleep(1)
        st.empty()
    if st.button("Tiếp tục"):
        st.session_state.scene = 2

def scene_2():
    st.header("Bạn đã sẵn sàng tiến vào hành trình này chưa?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Tôi rất sẵn sàng"):
            st.session_state.scene = 3
    with col2:
        if st.button("Tôi vẫn rất sẵn sàng"):
            st.session_state.scene = 3
    st.markdown("""
    <p style='font-size: 12px; color: gray; text-align: right;'>
    Không tìm thấy nút từ bỏ đâu, đừng cố tìm
    </p>
    """, unsafe_allow_html=True)

def scene_3():
    st.title("📘 Cẩm nang bắt đầu kết nối thế giới DLP4 dành cho Học viên mới")
    st.subheader("🔍 Gói tìm hiểu về các Staff")
    choice = st.radio("Chọn một nhóm để tìm hiểu:", ["Teaching Assistants", "Teaching Fellows", "Instructors"])
    if st.button("Xác nhận lựa chọn"):
        if choice == "Teaching Assistants":
            st.session_state.scene = 4
        elif choice == "Teaching Fellows":
            st.session_state.scene = 5
        elif choice == "Instructors":
            st.session_state.scene = 6

def main():
    if "scene" not in st.session_state:
        st.session_state.scene = 1

    scene_map = {
        1: scene_1,
        2: scene_2,
        3: scene_3
    }

    scene_func = scene_map.get(st.session_state.scene, scene_1)
    scene_func()

if __name__ == "__main__":
    main()
