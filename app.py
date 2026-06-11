import streamlit as st
import random

st.set_page_config(page_title="유명인 맞추기", page_icon="🎭")

people = {
    "메시": {
        "hard": [
            "왼발 사용으로 유명합니다.",
            "유소년 시절 성장호르몬 치료를 받았습니다.",
            "남미 출신 스포츠 스타입니다.",
            "등번호 10번의 상징적인 선수입니다."
        ],
        "medium": [
            "2022 월드컵 우승자입니다.",
            "오랜 기간 바르셀로나에서 뛰었습니다.",
            "발롱도르를 여러 차례 수상했습니다."
        ],
        "easy": [
            "아르헨티나 축구 선수입니다.",
            "현재 인터 마이애미 소속입니다."
        ]
    },

    "일론 머스크": {
        "hard": [
            "남아프리카공화국 출생입니다.",
            "온라인 결제 서비스 사업에 참여했습니다.",
            "재사용 로켓 기술로 유명합니다."
        ],
        "medium": [
            "전기차 산업의 대표 기업과 관련 있습니다.",
            "우주 산업 분야에서도 유명합니다."
        ],
        "easy": [
            "테슬라 CEO로 유명합니다.",
            "스페이스X 창립자입니다."
        ]
    },

    "테일러 스위프트": {
        "hard": [
            "컨트리 음악으로 데뷔했습니다.",
            "자신의 곡을 직접 작사하는 경우가 많습니다.",
            "그래미상을 다수 수상했습니다."
        ],
        "medium": [
            "세계적인 팝 가수입니다.",
            "대형 월드투어로 화제가 되었습니다."
        ],
        "easy": [
            "미국 가수입니다.",
            "Shake It Off를 불렀습니다."
        ]
    },

    "알베르트 아인슈타인": {
        "hard": [
            "스위스 특허청에서 근무한 적이 있습니다.",
            "1905년을 기적의 해라고 부릅니다.",
            "20세기 과학 발전에 큰 영향을 주었습니다."
        ],
        "medium": [
            "노벨 물리학상을 수상했습니다.",
            "독일 태생 과학자입니다."
        ],
        "easy": [
            "상대성 이론으로 유명합니다.",
            "E=mc²를 제시했습니다."
        ]
    }
}

# 게임 초기화
def new_game():
    answer = random.choice(list(people.keys()))

    st.session_state.answer = answer
    st.session_state.score = 100

    st.session_state.used_hard = 0
    st.session_state.used_medium = 0
    st.session_state.used_easy = 0

    st.session_state.hint_history = []

if "answer" not in st.session_state:
    new_game()

st.title("🎭 유명인 맞추기 게임")

st.write(f"## 현재 점수 : {st.session_state.score}점")

person = people[st.session_state.answer]

# 힌트 버튼
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🟢 어려움 (-10점)"):

        idx = st.session_state.used_hard

        if idx < len(person["hard"]):
            st.session_state.hint_history.append(
                person["hard"][idx]
            )
            st.session_state.used_hard += 1
            st.session_state.score = max(
                0,
                st.session_state.score - 10
            )

with col2:
    if st.button("🟡 보통 (-20점)"):

        idx = st.session_state.used_medium

        if idx < len(person["medium"]):
            st.session_state.hint_history.append(
                person["medium"][idx]
            )
            st.session_state.used_medium += 1
            st.session_state.score = max(
                0,
                st.session_state.score - 20
            )

with col3:
    if st.button("🔴 쉬움 (-30점)"):

        idx = st.session_state.used_easy

        if idx < len(person["easy"]):
            st.session_state.hint_history.append(
                person["easy"][idx]
            )
            st.session_state.used_easy += 1
            st.session_state.score = max(
                0,
                st.session_state.score - 30
            )

# 힌트 출력
st.subheader("📌 받은 힌트")

if len(st.session_state.hint_history) == 0:
    st.write("아직 받은 힌트가 없습니다.")
else:
    for i, hint in enumerate(
        st.session_state.hint_history,
        start=1
    ):
        st.write(f"{i}. {hint}")

# 정답 입력
guess = st.text_input("정답 입력")

if st.button("정답 제출"):

    if guess.strip().lower() == st.session_state.answer.lower():

        st.success(
            f"🎉 정답입니다! ({st.session_state.answer})"
        )

        st.write(
            f"최종 점수: {st.session_state.score}점"
        )

        st.balloons()

    else:
        st.error("❌ 틀렸습니다.")

# 새 게임
if st.button("새 게임 시작"):
    new_game()
    st.rerun()
