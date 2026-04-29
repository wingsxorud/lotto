import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="행님 로또 명당", page_icon="🎰", layout="centered")

# 간격 최적화 커스텀 CSS
st.markdown("""
    <style>
    /* 전체 배경 및 패딩 조절 */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 1rem !important;
    }
    /* 버튼 스타일 및 간격 */
    .stButton>button {
        width: 100%;
        height: 2.8em;
        font-weight: bold !important;
        border-radius: 8px;
        margin-bottom: 5px;
    }
    /* 조합 간격 최소화 */
    .lotto-row {
        margin-bottom: 2px !important;
        padding: 5px 0;
    }
    .lotto-container {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        margin: 0 auto 8px auto;
        padding: 5px;
        background-color: #f1f3f5;
        border-radius: 10px;
    }
    .lotto-ball {
        width: 32px;
        height: 32px;
        line-height: 32px;
        border-radius: 50%;
        text-align: center;
        color: white;
        font-weight: bold;
        font-size: 14px;
        margin: 3px;
        box-shadow: 1px 1px 3px rgba(0,0,0,0.1);
    }
    /* 조합 텍스트 간격 줄이기 */
    .stMarkdown p {
        margin-bottom: 2px !important;
        font-size: 0.9rem;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎰 행님 전용 모바일 명당")

# 데이터 시뮬레이션
frequent_numbers = [1, 10, 12, 13, 14, 17, 18, 21, 24, 26, 27, 33, 34, 39, 40, 43, 45]

def get_lotto_numbers():
    high_pick = random.sample(frequent_numbers, 3)
    others = [n for n in range(1, 46) if n not in high_pick]
    low_pick = random.sample(others, 3)
    return sorted(high_pick + low_pick)

def get_ball_color(num):
    if 1 <= num <= 10: return "#fbc400"
    if 11 <= num <= 20: return "#69c8f2"
    if 21 <= num <= 30: return "#ff7272"
    if 31 <= num <= 40: return "#aaaaaa"
    return "#b0d840"

if 'lotto_sets' not in st.session_state:
    st.session_state.lotto_sets = [get_lotto_numbers() for _ in range(5)]

col1, col2 = st.columns(2)
with col1:
    if st.button("🔄 새로고침"):
        st.session_state.lotto_sets = [get_lotto_numbers() for _ in range(5)]
        st.rerun()
with col2:
    if st.button("➕ 5세트 추가"):
        st.session_state.lotto_sets.extend([get_lotto_numbers() for _ in range(5)])

# 로또 번호 출력 (간격 축소 버전)
for i, nums in enumerate(st.session_state.lotto_sets):
    balls_html = "".join([
        f'<div class="lotto-ball" style="background-color:{get_ball_color(n)}">{n}</div>' 
        for n in nums
    ])
    # 조합 이름과 공 사이의 간격을 최소화하기 위해 하나의 div로 묶음
    st.markdown(f'''
        <div class="lotto-row">
            <div style="font-weight:bold; margin-left:10px;">조합 {i+1}</div>
            <div class="lotto-container">{balls_html}</div>
        </div>
    ''', unsafe_allow_html=True)

st.divider()
st.caption("화면을 캡처해서 사용하세요! 행님 대박 기원!")
