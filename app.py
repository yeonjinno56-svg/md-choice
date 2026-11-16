import streamlit as st
import time
import base64

# 페이지 기본 설정
st.set_page_config(page_title="선택지 게임", layout="centered")

# 세션 상태 초기화
if "step" not in st.session_state:
    st.session_state.step = "screen_1"

def get_base64_image(image_path):
    """이미지를 Base64 문자열로 변환합니다."""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def set_bg_color(color):
    """전체 화면 배경색을 변경하는 CSS를 적용합니다."""
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {color};
        }}
        header, footer {{visibility: hidden;}}
        </style>
        """,
        unsafe_allow_html=True
    )

def show_centered_text(text):
    """검은 화면 정중앙에 흰색 대사를 출력합니다."""
    set_bg_color("#000000")
    formatted_text = text.replace("\n", "<br>")
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center; align-items: center; height: 75vh; text-align: center;">
            <p style="color: white; font-size: 24px; font-weight: bold; line-height: 1.8; word-keep: keep-all;">
                {formatted_text}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ==========================================
# 1. 첫 번째 화면
# ==========================================
if st.session_state.step == "screen_1":
    set_bg_color("#FFFFFF")

    # 첫 번째 이미지 출력
    st.image("선택지창_명소민_길소명.jpg", use_container_width=True)

    # 두 번째, 세 번째 이미지를 버튼처럼 스타일링
    btn1_b64 = get_base64_image("선택지창_길소명을믿기.jpg")
    btn2_b64 = get_base64_image("선택지창_명소민을믿기.jpg")

    st.markdown(
        f"""
        <style>
        /* 왼쪽 버튼에 두 번째 이미지 입히기 */
        div[data-testid="column"]:nth-of-type(1) button {{
            background-image: url("data:image/jpeg;base64,{btn1_b64}");
            background-size: contain;
            background-repeat: no-repeat;
            background-position: center;
            height: 80px;
            width: 100%;
            border: none;
            background-color: white;
            color: transparent !important;
        }}
        /* 오른쪽 버튼에 세 번째 이미지 입히기 */
        div[data-testid="column"]:nth-of-type(2) button {{
            background-image: url("data:image/jpeg;base64,{btn2_b64}");
            background-size: contain;
            background-repeat: no-repeat;
            background-position: center;
            height: 80px;
            width: 100%;
            border: none;
            background-color: white;
            color: transparent !important;
        }}
        div[data-testid="column"] button:hover {{
            opacity: 0.85;
            border: none;
        }}
        div[data-testid="column"] button:focus {{
            box-shadow: none !important;
            border: none !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # 하단 흰색 배경 영역에 인물 위치에 맞춰 2개의 컬럼 배치
    col1, col2 = st.columns(2)
    with col1:
        if st.button("길소명을 믿기", key="btn_left", use_container_width=True):
            st.session_state.step = "screen_2_1_text"
            st.rerun()
    with col2:
        if st.button("명소민을 믿기", key="btn_right", use_container_width=True):
            st.session_state.step = "screen_2_2"
            st.rerun()

# ==========================================
# 2-1. 두 번째 화면 (두 번째 이미지 클릭 시)
# ==========================================
elif st.session_state.step == "screen_2_1_text":
    show_centered_text("나를 믿어줬구나... 정말 고마워.")
    time.sleep(2)
    st.session_state.step = "screen_2_1_choice"
    st.rerun()

elif st.session_state.step == "screen_2_1_choice":
    set_bg_color("#000000")

    # 검은 화면 중앙에 선택지 버튼 스타일 지정
    st.markdown(
        """
        <style>
        div.stButton > button {
            background-color: #222222;
            color: white;
            font-size: 20px;
            font-weight: bold;
            padding: 18px 24px;
            border: 2px solid #888888;
            border-radius: 10px;
            margin-bottom: 15px;
        }
        div.stButton > button:hover {
            background-color: #444444;
            color: white;
            border-color: white;
        }
        </style>
        <div style="height: 30vh;"></div>
        """,
        unsafe_allow_html=True
    )

    if st.button("주스팩을 버리기", use_container_width=True):
        st.session_state.step = "screen_3_1"
        st.rerun()

    if st.button("주스팩을 경찰서에 가져가기", use_container_width=True):
        st.session_state.step = "screen_3_2"
        st.rerun()

# ==========================================
# 2-2. 두 번째 화면 (세 번째 이미지 클릭 시)
# ==========================================
elif st.session_state.step == "screen_2_2":
    show_centered_text("그래, 소명이가 착각한거야.\n소명이가 트라우마에서 벗어날 수 있게 도와주겠니?")
    time.sleep(3.5)
    st.session_state.step = "screen_3_1"
    st.rerun()

# ==========================================
# 3-1. 세 번째 화면 (버리기 선택 or 2-2 종료 후)
# ==========================================
elif st.session_state.step == "screen_3_1":
    show_centered_text(
        "나는 소민이에게 주스팩을 버리는 것이 좋을 거라고 조언했다.\n"
        "소민이는 잠시 고민하다가 주스팩을 복일천 공원에 던졌다.\n"
        "뒤돌아가는 소민이의 모습이 어쩐지 쓸쓸해 보였다."
    )

# ==========================================
# 3-2. 세 번째 화면 (경찰서에 가져가기 선택)
# ==========================================
elif st.session_state.step == "screen_3_2":
    show_centered_text(
        "나는 소민이에게 주스팩을 경찰서에 다시 가져가라고 조언했다.\n"
        "소민이는 손을 떨고 있었지만 끝까지 진술을 해냈다.\n"
        "이후 명진이의 죽음에 대한 재수사가 시작되었다."
    )
