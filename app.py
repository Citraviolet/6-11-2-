import streamlit as st
import random

st.set_page_config(page_title="Football Quiz", page_icon="⚽")

# 선수 데이터
players = {
    "메시": {
        "국적": "아르헨티나",
        "포지션": "공격수",
        "리그": "MLS",
        "나이": 38,
        "가치": 18000000
    },
    "호날두": {
        "국적": "포르투갈",
        "포지션": "공격수",
        "리그": "사우디",
        "나이": 41,
        "가치": 12000000
    },
    "음바페": {
        "국적": "프랑스",
        "포지션": "공격수",
        "리그": "라리가",
        "나이": 27,
        "가치": 180000000
    },
    "하알란드": {
        "국적": "노르웨이",
        "포지션": "공격수",
        "리그": "프리미어리그",
        "나이": 25,
        "가치": 180000000
    },
    "벨링엄": {
        "국적": "잉글랜드",
        "포지션": "미드필더",
        "리그": "라리가",
        "나이": 22,
        "가치": 180000000
    },
    "손흥민": {
        "국적": "대한민국",
        "포지션": "공격수",
        "리그": "프리미어리그",
        "나이": 34,
        "가치": 30000000
    }
}

page = st.sidebar.selectbox(
    "게임 선택",
    ["축구 Wordle", "시장가치 맞추기"]
)

# -----------------------
# 축구 Wordle
# -----------------------

if page == "축구 Wordle":

    st.title("⚽ 축구 Wordle")

    if "answer" not in st.session_state:
        st.session_state.answer = random.choice(list(players.keys()))
        st.session_state.attempts = 0

    guess = st.text_input("선수 이름 입력")

    if st.button("확인"):

        if guess not in players:
            st.error("등록된 선수만 입력하세요.")
        else:

            st.session_state.attempts += 1

            answer = st.session_state.answer

            if guess == answer:

                score = max(
                    100 - (st.session_state.attempts - 1) * 10,
                    10
                )

                st.success(
                    f"🎉 정답! {answer}"
                )

                st.write(
                    f"시도 횟수: {st.session_state.attempts}"
                )

                st.write(
                    f"점수: {score}점"
                )

                if st.button("새 게임"):
                    st.session_state.answer = random.choice(
                        list(players.keys())
                    )
                    st.session_state.attempts = 0
                    st.rerun()

            else:

                g = players[guess]
                a = players[answer]

                st.error("❌ 틀렸습니다!")

                st.write(
                    f"국적: {'✅' if g['국적']==a['국적'] else '❌'}"
                )

                st.write(
                    f"포지션: {'✅' if g['포지션']==a['포지션'] else '❌'}"
                )

                st.write(
                    f"리그: {'✅' if g['리그']==a['리그'] else '❌'}"
                )

                if g["나이"] < a["나이"]:
                    st.write("나이: ⬆️ (정답이 더 많음)")
                elif g["나이"] > a["나이"]:
                    st.write("나이: ⬇️ (정답이 더 적음)")
                else:
                    st.write("나이: ✅")

# -----------------------
# 시장가치 맞추기
# -----------------------

if page == "시장가치 맞추기":

    st.title("💰 시장가치 맞추기")

    if "market_player" not in st.session_state:
        st.session_state.market_player = random.choice(
            list(players.keys())
        )

    player = st.session_state.market_player

    st.subheader(player)

    value = st.number_input(
        "시장가치를 입력하세요 (€)",
        min_value=0,
        step=1000000
    )

    if st.button("제출"):

        actual = players[player]["가치"]

        diff = abs(actual - value)

        score = max(
            100 - int(diff / 5000000),
            0
        )

        st.write(
            f"실제 시장가치: €{actual:,}"
        )

        st.write(
            f"차이: €{diff:,}"
        )

        st.success(
            f"점수: {score}점"
        )

        if st.button("다음 선수"):
            st.session_state.market_player = random.choice(
                list(players.keys())
            )
            st.rerun()
