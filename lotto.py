import streamlit as st
import random

# 1. 페이지 설정
st.set_page_config(page_title="행님 로또 명당", page_icon="🎰", layout="centered")

# 2. 모바일 최적화 및 밸런스 조정 CSS
st.markdown("""
    <style>
    /* 전체 배경색 및 여백 */
    .main .block-container {
        padding: 1.5rem 0.8rem !important;
        max-width: 480px !important;
    }
    
    /* 제목 스타일 */
    .stHeading h1 { font-size: 1.8rem !important; color: #333; margin-bottom: 20px !important; }

    /* 버튼 레이아웃 - 5:5 비율로 적당한 간격 */
    div[data-testid="stHorizontalBlock"] {
        gap: 12px !important;
        margin-bottom: 20px !important;
    }
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3.5rem;
        font-weight: bold !important;
        font-size: 1rem !important;
        background-color: #f8f9fa;
        border: 1px solid #ddd;
    }
    /* 새로고침 버튼 포인트 컬러 */
    div[data-testid="stHorizontalBlock"] div:nth-child(1) button {
        background-color: #4A90E2;
        color: white;
        border: none;
    }

    /* 번호 카드 - 시원한 폭과 깔끔한 테두리 */
    [data-testid="stVerticalBlockBorderWrapper"] {
        border: 1px solid #eee !important;
        border-radius: 20px !important;
        padding: 15px !important;
        background-color: #ffffff !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05) !important;
    }
    
    /* 로또 공 - 큼직하고 선명하게 */
    .ball {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 42px;
        height: 42px;
        border-radius: 50%;
        color: white !important;
        font-weight: 800;
        font-size: 15px;
        box-shadow: inset -3px -3px 5px rgba(0,0,0,0.2);
    }

    /* 번호 줄 간격 */
    .lotto-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 0;
        border-bottom: 1px solid #f1f1f1;
    }
    .lotto-row:last-child { border-bottom: none; }
    
    .row-num {
        font-size: 0.8rem;
        font-weight: bold;
        color: #bbb;
        width: 30px;
    }
    .ball-container {
        display: flex;
        gap: 6px;
        justify-content: flex-end;
        flex: 1;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎰 행님 로또 명당")

# 3. 로직
frequent = [1, 10, 12, 13, 14, 17, 18, 21, 24, 26, 27, 33, 34, 39, 40, 43, 45]
def pick():
    h = random.sample(frequent, 3)
    o = [n for n in range(1, 46) if n not in h]
    return sorted(h + random.sample(o, 3))

def get_c(n):
    if n <= 10: return "#fbc400"
    if n <= 20: return "#69c8f2"
    if n <= 30: return "#ff7272"
    if n <= 40: return "#aaaaaa"
    return "#b0d840"

# 4. 데이터 관리
if 'bundles' not in st.session_state:
    st.session_state.bundles = [[pick() for _ in range(5)]]

# 5. 버튼 레이아웃
c1, c2 = st.columns(2)
with c1:
    if st.button("🔄 번호 새로고침"):
        st.session_state.bundles = [[pick() for _ in range(5)]]
        st.rerun()
with c2:
    if st.button("➕ 5세트 추가"):
        st.session_state.bundles.append([pick() for _ in range(5)])

# 6. 결과 출력
for b_idx, bundle in enumerate(st.session_state.bundles):
    with st.container(border=True):
        st.caption(f"MY LUCKY SET {b_idx + 1}")
        for i, nums in enumerate(bundle):
            balls_html = "".join([f'<div class="ball" style="background-color:{get_c(n)}">{n}</div>' for n in nums])
            st.markdown(f'''
                <div class="lotto-row">
                    <div class="row-num">#{i+1}</div>
                    <div class="ball-container">{balls_html}</div>
                </div>
            ''', unsafe_allow_html=True)

st.divider()
st.info("행님, 이제 디자인 밸런스 딲! 맞췄습니다. 캡처하기 제일 좋으실 거예요!")
