import streamlit as st
import random

# 1. 페이지 설정
st.set_page_config(page_title="행님 로또 명당", page_icon="🎰", layout="centered")

# 2. 버튼 간격 및 프레임 크기 조절 CSS
st.markdown("""
    <style>
    /* 전체 여백 줄이기 */
    .main .block-container {
        padding: 1rem 0.5rem !important;
        max-width: 400px !important; /* 전체 폭을 좁혀서 컴팩트하게 */
    }
    
    /* 제목 및 아이콘 크기 조절 */
    h1 { font-size: 1.8rem !important; margin-bottom: 10px !important; }

    /* 버튼 레이아웃 - 간격 좁히기 */
    div[data-testid="stHorizontalBlock"] {
        gap: 10px !important; /* 버튼 사이 간격 최소화 */
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3rem;
        font-weight: bold !important;
        font-size: 0.9rem !important;
    }

    /* 프레임(컨테이너) 디자인 - 꽉 맞게 조절 */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        padding: 10px !important;
        margin-top: -10px !important;
    }
    
    /* 로또 공 디자인 (크기 및 간격 최적화) */
    .lotto-ball {
        display: inline-block;
        width: 38px;
        height: 38px;
        line-height: 38px;
        border-radius: 50%;
        text-align: center;
        color: white !important;
        font-weight: bold;
        font-size: 14px;
        margin: 2px;
        box-shadow: inset -2px -2px 4px rgba(0,0,0,0.15);
    }

    /* 번호 라벨 폭 조절 */
    .row-idx {
        color: #ccc;
        font-weight: bold;
        font-size: 12px;
        padding-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎰 행님 로또 명당")

# 3. 로직
frequent_pool = [1, 10, 12, 13, 14, 17, 18, 21, 24, 26, 27, 33, 34, 39, 40, 43, 45]
def pick():
    h = random.sample(frequent_pool, 3)
    o = [n for n in range(1, 46) if n not in h]
    return sorted(h + random.sample(o, 3))

def get_color(n):
    if n <= 10: return "#fbc400"
    if n <= 20: return "#69c8f2"
    if n <= 30: return "#ff7272"
    if n <= 40: return "#aaaaaa"
    return "#b0d840"

# 4. 세션 관리
if 'bundles' not in st.session_state:
    st.session_state.bundles = [[pick() for _ in range(5)]]

# 5. 조작 버튼 (간격을 좁히기 위해 columns 비율 조정)
c1, c2 = st.columns([1, 1])
with c1:
    if st.button("🔄 새로고침"):
        st.session_state.bundles = [[pick() for _ in range(5)]]
        st.rerun()
with c2:
    if st.button("➕ 세트 추가"):
        st.session_state.bundles.append([pick() for _ in range(5)])

# 6. 결과 출력 (컴팩트 프레임)
for b_idx, bundle in enumerate(st.session_state.bundles):
    with st.container(border=True):
        st.caption(f"SET {b_idx + 1}")
        for i, nums in enumerate(bundle):
            # 라벨과 공 사이의 간격도 더 밀착
            cols = st.columns([0.15, 0.85])
            with cols[0]:
                st.markdown(f"<div class='row-idx'>#{i+1}</div>", unsafe_allow_html=True)
            with cols[1]:
                balls_html = "".join([f'<span class="lotto-ball" style="background-color:{get_color(n)}">{n}</span>' for n in nums])
                # justify-content를 center로 바꿔서 공들이 너무 퍼지지 않게 함
                st.markdown(f'<div style="display:flex; justify-content:center; gap:5px;">{balls_html}</div>', unsafe_allow_html=True)

st.divider()
st.info("행님, 버튼 간격 좁히고 프레임도 딲! 맞게 줄였습니다. 이제 보기 훨씬 편하실 겁니다!")
