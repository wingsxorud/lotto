import streamlit as st
import random

# 1. 페이지 설정
st.set_page_config(page_title="행님 로또 명당", page_icon="🎰", layout="centered")

# 2. 모바일 밀착형 스타일
st.markdown("""
    <style>
    /* 전체 여백 조절 */
    .main .block-container {
        padding: 1.5rem 0.7rem !important;
        max-width: 500px !important;
    }
    
    /* 버튼 스타일 및 적당한 간격 */
    div[data-testid="stHorizontalBlock"] {
        gap: 15px !important;
        margin-bottom: 20px !important;
    }
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3.5rem;
        font-weight: bold !important;
        font-size: 1rem !important;
    }

    /* 로또 공 - 모바일 화면에 맞춰 큼직하게 */
    .ball-item {
        display: inline-block;
        width: 42px;
        height: 42px;
        line-height: 42px;
        border-radius: 50%;
        text-align: center;
        color: white !important;
        font-weight: 800;
        font-size: 16px;
        margin: 3px;
        box-shadow: inset -2px -2px 4px rgba(0,0,0,0.2);
    }

    /* 프레임 내부 정렬 */
    .row-container {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 8px 0;
        border-bottom: 1px solid #f8f9fa;
    }
    .row-container:last-child { border-bottom: none; }
    
    .row-idx {
        font-size: 0.8rem;
        font-weight: bold;
        color: #bbb;
        width: 35px;
        flex-shrink: 0;
    }
    .ball-area {
        flex-grow: 1;
        display: flex;
        justify-content: flex-end; /* 공들을 오른쪽으로 정렬해서 가득 차 보이게 */
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎰 행님 로또 명당")

# 3. 로직
frequent = [1, 10, 12, 13, 14, 17, 18, 21, 24, 26, 27, 33, 34, 39, 40, 43, 45]
def pick_nums():
    h = random.sample(frequent, 3)
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
    st.session_state.bundles = [[pick_nums() for _ in range(5)]]

# 5. 상단 버튼 (비율 1:1로 딲 맞춤)
c1, c2 = st.columns(2)
with c1:
    if st.button("🔄 번호 새로고침"):
        st.session_state.bundles = [[pick_nums() for _ in range(5)]]
        st.rerun()
with c2:
    if st.button("➕ 5세트 추가"):
        st.session_state.bundles.append([pick_nums() for _ in range(5)])

# 6. 결과 출력
for b_idx, bundle in enumerate(st.session_state.bundles):
    with st.container(border=True):
        st.caption(f"MY LUCKY SET {b_idx + 1}")
        for i, nums in enumerate(bundle):
            balls_html = "".join([f'<div class="ball-item" style="background-color:{get_color(n)}">{n}</div>' for n in nums])
            st.markdown(f'''
                <div class="row-container">
                    <div class="row-idx">#{i+1}</div>
                    <div class="ball-area">{balls_html}</div>
                </div>
            ''', unsafe_allow_html=True)

st.divider()
st.info("행님, 이제 공도 큼직하고 버튼도 딲! 보기 좋으실 겁니다. 1등 가즈아! 🚀")
