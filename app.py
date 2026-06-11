import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="Football Wordle", page_icon="⚽")

players = {
    "메시": {"국적":"아르헨티나","팀":"인터 마이애미","리그":"MLS","포지션":"RW","나이":38,"키":170,"주발":"왼발"},
    "호날두": {"국적":"포르투갈","팀":"알 나스르","리그":"사우디","포지션":"ST","나이":41,"키":187,"주발":"오른발"},
    "음바페": {"국적":"프랑스","팀":"레알 마드리드","리그":"라리가","포지션":"ST","나이":27,"키":178,"주발":"오른발"},
    "하알란드": {"국적":"노르웨이","팀":"맨체스터 시티","리그":"프리미어리그","포지션":"ST","나이":25,"키":195,"주발":"왼발"},
    "벨링엄": {"국적":"잉글랜드","팀":"레알 마드리드","리그":"라리가","포지션":"CM","나이":22,"키":186,"주발":"오른발"},
    "손흥민": {"국적":"대한민국","팀":"토트넘","리그":"프리미어리그","포지션":"LW","나이":34,"키":183,"주발":"오른발"},
    "살라": {"국적":"이집트","팀":"리버풀","리그":"프리미어리그","포지션":"RW","나이":34,"키":175,"주발":"왼발"},
    "비니시우스": {"국적":"브라질","팀":"레알 마드리드","리그":"라리가","포지션":"LW","나이":26,"키":176,"주발":"오른발"},
    "야말": {"국적":"스페인","팀":"바르셀로나","리그":"라리가","포지션":"RW","나이":19,"키":180,"주발":"왼발"},
    "케인": {"국적":"잉글랜드","팀":"바이에른 뮌헨","리그":"분데스리가","포지션":"ST","나이":33,"키":188,"주발":"오른발"}
}

st.title("⚽ Football Wordle")

if "answer" not in st.session_state:
    st.session_state.answer = random.choice(list(players.keys()))
    st.session_state.score = 100
    st.session_state.history = []

answer = st.session_state.answer

st.write("선수 이름을 입력해 정답을 맞혀보세요!")

guess = st.selectbox(
    "선수 선택",
    [""] + list(players.keys())
)

if st.button("확인") and guess:

    if guess == answer:
        st.success(f"🎉 정답! 정답은 {answer}입니다.")
        st.write(f"최종 점수: {st.session_state.score}점")

    else:
        g = players[guess]
        a = players[answer]

        def compare_text(value1, value2):
            return "✅" if value1 == value2 else "❌"

        def compare_number(value1, value2):
            if value1 == value2:
                return "✅"
            elif value1 < value2:
                return "⬆️"
            else:
                return "⬇️"

        row = {
            "선수": guess,
            "국적": compare_text(g["국적"], a["국적"]),
            "팀": compare_text(g["팀"], a["팀"]),
            "리그": compare_text(g["리그"], a["리그"]),
            "포지션": compare_text(g["포지션"], a["포지션"]),
            "나이": compare_number(g["나이"], a["나이"]),
            "키": compare_number(g["키"], a["키"]),
            "주발": compare_text(g["주발"], a["주발"])
        }

        st.session_state.history.append(row)
        st.session_state.score = max(10, st.session_state.score - 10)

        st.error("❌ 틀렸습니다!")

if st.session_state.history:
    st.subheader("추측 기록")
    df = pd.DataFrame(st.session_state.history)
    st.dataframe(df, use_container_width=True)

st.write(f"현재 점수: {st.session_state.score}점")

if st.button("새 게임 시작"):
    st.session_state.answer = random.choice(list(players.keys()))
    st.session_state.score = 100
    st.session_state.history = []
    st.rerun()
