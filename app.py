import streamlit as st
import time
import base64

st.set_page_config(page_title="선택지 게임", layout="centered")

if "step" not in st.session_state:
    st.session_state.step = "screen_1"

# 화면 전체를 담을 단일 도화지(컨테이너)
placeholder = st.empty()

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def set_bg_color(color):
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

def render_centered_text(text):
    formatted_text = text.replace("\n", "<br>")
    return f"""
    <div style="display: flex; justify-content: center; align-items: center; height: 75vh; text-align: center;">
        <p style="color: white; font-size: 24px; font-weight: bold; line-height: 1.8; word-keep: keep-all;">
            {formatted_text}
        </p>
    </div>
    """

# 1. 첫 번째 화면
if st.session_state.step == "screen_1":
    set_bg_color("#FFFFFF")
    btn1_b64 = get_base64_image("선택지창_길소명을믿기.jpg")
    btn2_b64 = get_base64_image("선택지창_명소민을믿기.jpg")

    with placeholder.container():
        st.image("선택지창_명소민_길소명.jpg", use_container_width=True)
        st.markdown(
            f"""
            <style>
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

        col1, col2 = st.columns(2)
        with col1:
            if st.button("길소명을 믿기", key="btn_left", use_container_width=True):
                placeholder.empty()
                st.session_state.step = "screen_2_1_text"
                st.rerun()
        with col2:
            if st.button("명소민을 믿기", key="btn_right", use_container_width=True):
                placeholder.empty()
                st.session_state.step = "screen_2_2"
                st.rerun()

# 2-1. 두 번째 화면 (두 번째 이미지 클릭 시)
elif st.session_state.step == "screen_2_1_text":
    set_bg_color("#000000")
    placeholder.markdown(render_centered_text("나를 믿어줬구나... 정말 고마워."), unsafe_allow_html=True)
    time.sleep(2)
    placeholder.empty()
    st.session_state.step = "screen_2_1_choice"
    st.rerun()

elif st.session_state.step == "screen_2_1_choice":
    set_bg_color("#000000")
    with placeholder.container():
        st.markdown(
            """
            <style>
            div.stButton > button {
                background-color: #222222 !important;
                background-image: none !important;
                color: white !important;
                font-size: 20px !important;
                font-weight: bold !important;
                height: auto !important;
                padding: 18px 24px !important;
                border: 2px solid #888888 !important;
                border-radius: 10px !important;
                margin-bottom: 15px !important;
            }
            div.stButton > button:hover {
                background-color: #444444 !important;
                color: white !important;
                border-color: white !important;
            }
            </style>
            <div style="height: 30vh;"></div>
            """,
            unsafe_allow_html=True
        )

        if st.button("주스팩을 버리기", key="choice_throw", use_container_width=True):
            placeholder.empty()
            st.session_state.step = "screen_3_1"
            st.rerun()

        if st.button("주스팩을 경찰서에 가져가기", key="choice_police", use_container_width=True):
            placeholder.empty()
            st.session_state.step = "screen_3_2"
            st.rerun()

# 2-2. 두 번째 화면 (세 번째 이미지 클릭 시)
elif st.session_state.step == "screen_2_2":
    set_bg_color("#000000")
    placeholder.markdown(
        render_centered_text("그래, 소명이가 착각한거야.\n소명이가 트라우마에서 벗어날 수 있게 도와주겠니?"),
        unsafe_allow_html=True
    )
    time.sleep(3.5)
    placeholder.empty()
    st.session_state.step = "screen_3_1"
    st.rerun()

# 3-1. 세 번째 화면 (버리기 선택 or 2-2 종료 후)
elif st.session_state.step == "screen_3_1":
    set_bg_color("#000000")
    placeholder.markdown(
        render_centered_text(
            "나는 소민이에게 주스팩을 버리는 것이 좋을 거라고 조언했다.\n"
            "소민이는 잠시 고민하다가 주스팩을 복일천 공원에 던졌다.\n"
            "뒤돌아가는 소민이의 모습이 어쩐지 쓸쓸해 보였다."
        ),
        unsafe_allow_html=True
    )

# 3-2. 세 번째 화면 (경찰서에 가져가기 선택)
elif st.session_state.step == "screen_3_2":
    set_bg_color("#000000")
    placeholder.markdown(
        render_centered_text(
            "나는 소민이에게 주스팩을 경찰서에 다시 가져가라고 조언했다.\n"
            "소민이는 손을 떨고 있었지만 끝까지 진술을 해냈다.\n"
            "이후 명진이의 죽음에 대한 재수사가 시작되었다."
        ),
        unsafe_allow_html=True
    )
