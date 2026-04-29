import streamlit as st
import random

# 페이지 설정 (모바일 최적화)
st.set_page_config(
    page_title="행님 로또 명당",
    page_icon="🎰",
    layout="centered"
)

# 모바일용 커스텀 CSS (버튼 크기 및 공 정렬)
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        height: 3em;
        font-size: 1.2rem !important;
        font-weight: bold !important;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    .lotto-container {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        margin-bottom: 15px;
        padding: 10px;
        background-color: #f8f9fa;
        border-radius: 15px;
    }
    .lotto-ball {
        width: 40px;
        height: 40px;
        line-height: 40px;
        border-radius: 50%;
        text-align: center;
        color: white;
        font-weight: bold;
        font-size: 16px;
        margin: 5px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
    }
    /* 스크린샷 찍을 때 배경색 하얗게 */
    @media print {
        .stButton, .stInfo { display: none; }
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎰 행님 전용 모바일 명당")
st.subheader("이번 주 1등 주인공은 바로 행님!")

# 데이터 시뮬레이션 (통계 기반)
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

# 세션 상태 초기화 (추천 더 받기 기능용)
if 'lotto_sets' not in st.session_state:
    st.session_state.lotto_sets = [get_lotto_numbers() for _ in range(5)]

# 버튼 레이아웃
col1, col2 = st.columns(2)

with col1:
    if st.button("🔄 번호 새로고침"):
        st.session_state.lotto_sets = [get_lotto_numbers() for _ in range(5)]
        st.rerun()

with col2:
    if st.button("➕ 5세트 추가하기"):
        new_sets = [get_lotto_numbers() for _ in range(5)]
        st.session_state.lotto_sets.extend(new_sets)

# 로또 번호 출력
for i, nums in enumerate(st.session_state.lotto_sets):
    balls_html = "".join([
        f'<div class="lotto-ball" style="background-color:{get_ball_color(n)}">{n}</div>' 
        for n in nums
    ])
    st.markdown(f"**조합 {i+1}**")
    st.markdown(f'<div class="lotto-container">{balls_html}</div>', unsafe_allow_html=True)

st.divider()

# 스크린샷 팁 안내
with st.expander("📸 스크린샷 저장 꿀팁"):
    st.write("1. 아이폰: 전원 버튼 + 볼륨 업")
    st.write("2. 갤럭시: 전원 버튼 + 볼륨 다운 (또는 손날 밀기)")
    st.info("현재 화면을 캡처해서 갤러리에 보관해두고 로또방에 가셔요!")

st.caption("통계 기반 가중치 조합 시스템 작동 중")
