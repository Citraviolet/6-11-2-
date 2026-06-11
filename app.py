import streamlit as st
import random

st.set_page_config(page_title="유명인 맞추기", page_icon="🎭")

people = {
    "메시": {
        "hard": [
            "등번호 10번으로 유명합니다.",
            "남미 출신 스포츠 스타입니다."
        ],
        "medium": [
            "월드컵 우승 경력이 있습니다.",
            "오랜 기간 한 스페인 명문 구단에서 뛰었습니다."
        ],
        "easy": [
            "아르헨티나 축구 선수입니다.",
            "현재 인터 마이애미에서 뛰고 있습니다."
        ]
    },
    "일론 머스크": {
        "hard": [
            "재사용 가능한 로켓 개발에 큰 영향을 주었습니다.",
            "온라인 결제 서비스 사업에 참여한 적이 있습니다."
        ],
        "medium": [
            "전기차 산업을 대표하는 기업과 관련이 있습니다.",
            "우주 산업으로도 유명합니다."
        ],
        "easy": [
            "테슬라 CEO로 유명합니다.",
            "스페이스X를 이끌고 있습니다."
        ]
    },
    "테일러 스위프트": {
        "hard": [
            "컨트리 음악으로 경력을 시작했습니다.",
            "그래미상을 여러 차례 수상했습니다."
        ],
        "medium": [
            "세계적인 팝 가수입니다.",
            "대규모 월드투어로 화제가 되었습니다."
        ],
        "easy": [
            "미국의 가수입니다.",
            "Shake It Off로 유명합니다."
        ]
    },
    "알베르트 아인슈타인": {
        "hard": [
            "상대성 이론으로 유명합니다.",
            "20세기 과학 발전에 큰 영향을 주었습니다."
        ],
        "medium": [
            "노벨 물리학상을 수상했습니다.",
            "독일 태생 과학자입니다."
        ],
        "easy": [
            "E=mc²로 유명합니다.",
            "물리학자입니다."
        ]
    },
    "마이클 잭슨": {
        "hard": [
            "Moonwalk 춤으로 유명합니다.",
            "역사상 가장 영향력 있는 팝스타 중 한 명입니다."
        ],
        "medium": [
            "팝의 황제라는 별명을 가졌습니다.",
            "Thriller 앨범으로 유명합니다."
        ],
        "easy": [
            "미국 가수입니다.",
            "Beat It을 부른 가수입니다."
        ]
    }
}

# 게임 시작
if "answer" not in st.session_state:
    st.session_state.answer = random.choice(list(people.keys()))
    st.session_state.score = 100
    st.session_state.hints = []

st.title("🎭 유명인 맞추기 게임")

st.write(f"현재 점수: **{st.session_state.score}점**")

person = people[st.session_state.answer]

st.subheader("힌트 받기")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🟢 어려움 (-10점)"):
        hint = random.choice(person["hard"])
        st.session_state.hints.append(hint)
        st.session_state.score = max(0, st.session_state.score - 10)

with col2:
    if st.button("🟡 보통 (-20점)"):
        hint = random.choice(person["medium"])
        st.session_state.hints.append(hint)
        st.session_state.score = max(0, st.session_state.score - 20)

with col3:
    if st.button("🔴 쉬움 (-30점)"):
        hint = random.choice(person["easy"])
        st.session_state.hints.append(hint)
        st.session_state.score = max(0, st.session_state.score - 30)

if st.session_state.hints:
    st.subheader("지금까지 받은 힌트")
    for i, hint in enumerate(st.session_state.hints, start=1):
        st.write(f"{i}. {hint}")

guess = st.text_input("정답 입력")

if st.button("정답 제출"):
    if guess.strip().lower() == st.session_state.answer.lower():
        st.success(
            f"🎉 정답입니다! {st.session_state.answer}"
        )
        st.balloons()
        st.write(f"최종 점수: {st.session_state.score}점")
    else:
        st.error("❌ 틀렸습니다.")

if st.button("새 게임"):
    st.session_state.answer = random.choice(list(people.keys()))
    st.session_state.score = 100
    st.session_state.hints = []
    st.rerun()
