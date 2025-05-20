
import streamlit as st
import time

# Utility function for typewriter effect
def typewriter(text, delay=0.05, font_size=24):
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

# Scene 1
def scene_1():
    messages = [
        ("Chào mừng bạn đến với DAV Leadership Programme – Summer Course 2025", 7),
        ("Một hành trình mới sắp bắt đầu, chúc bạn chân cứng đá mềm", 5),
        ("Chị là Phạm Tuyết Mai", 3),
        ("Mai trong Hoa Mai", 3),
        ("Tuyết trong Bông Tuyết", 3),
        ("Phạm là họ bố..và cả ông nội… tất nhiên rồi", 3),
        ("Chị sẽ là Instructor đi cùng với em hết hành trình DLP4 này", 5),
        ("Cảm ơn vì đã đến", 3),
    ]
    for msg, delay in messages:
        st.empty()
        typewriter(msg, delay=0.05)
        time.sleep(delay)
        st.empty()
    if st.button("Tiếp tục"):
        st.session_state.scene = 2

# Scene 2
def scene_2():
    st.header("Bạn đã sẵn sàng tiến vào hành trình này chưa?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Tôi rất sẵn sàng"):
            st.session_state.scene = 3
    with col2:
        if st.button("Tôi vẫn rất sẵn sàng"):
            st.session_state.scene = 3
    st.markdown("<p style='font-size: 12px; color: gray; text-align: right;'>Không tìm thấy nút từ bỏ đâu, đừng cố tìm</p>", unsafe_allow_html=True)

# Scene 3
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

# Scene 4
def scene_4():
    st.header("👩‍🏫 Teaching Assistants")
    if st.button("Nguyễn Thị Thu Hà (Yoogi)"):
        st.session_state.scene = 7

# Scene 5
def scene_5():
    st.header("👩‍💼 Teaching Fellows")
    st.write("Tạm thời đang cập nhật...")

# Scene 6
def scene_6():
    st.header("👨‍🏫 Instructors")
    st.write("Tạm thời đang cập nhật...")

# Scene 7
def scene_7():
    st.markdown("### 👤 Nhân vật: Nguyễn Thị Thu Hà (Yoogi)", unsafe_allow_html=True)
    st.markdown("""
    - Ngày sinh: 19/11  
    - Cung hoàng đạo: Bọ Cạp  
    - Đặc điểm nhận dạng: Luôn bốc cháy, dâng hiến cả con tim  
    - [Link Facebook](https://www.facebook.com/ha.yoongie.7/)
    """, unsafe_allow_html=True)
    typewriter("Mình là Yoogie, mình thấy mình rất hài hước, mình thích được mang những câu joke vui vẻ đến với mọi người. Mình cung nước (Bọ Cạp) nên nhìn ngoài dữ nhưng bên trong mềm nhũn.", delay=0.02, font_size=20)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Quay lại trang chủ"):
            st.session_state.scene = 3
    with col2:
        if st.button("Nạp xong dữ liệu, tiếp tục hành trình"):
            st.session_state.scene = 40

# Scene 40
def scene_40():
    st.title("🚀 Hành trình DLP4 sắp bắt đầu")
    if st.button("Nhập vai Học viên, tiến vào DLP4"):
        st.session_state.scene = 41

# Scene 41
def scene_41():
    st.image("https://i.imgur.com/Z8NfYvP.png", caption="Chào mừng đến với DLP4!", use_column_width=True)

# Routing logic
def main():
    if "scene" not in st.session_state:
        st.session_state.scene = 1

    scene_map = {
        1: scene_1,
        2: scene_2,
        3: scene_3,
        4: scene_4,
        5: scene_5,
        6: scene_6,
        7: scene_7,
        40: scene_40,
        41: scene_41,
    }

    scene_func = scene_map.get(st.session_state.scene, scene_1)
    scene_func()

if __name__ == "__main__":
    main()
