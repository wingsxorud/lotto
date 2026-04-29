import streamlit as st
import random

# 1. 페이지 설정 및 초기화
st.set_page_config(page_title="행님 로또 명당", page_icon="🎰", layout="centered")

# 2. 아주 단순하고 강력한 공 디자인 (스타일 태그 최소화)
st.markdown("""
    <style>
    /* 전체 화면 여백 최적화 */
    .main .block-container {
        padding: 1.5rem 0.5rem !important;
        max-width: 450px !important;
    }
    /* 버튼 간격 및 디자인 */
    div[data-testid="stHorizontalBlock"] {
        gap: 10px !important;
    }
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3.5rem;
        font-weight: bold !important;
    }
    /* 로또 공 - 큼직하게 고정 */
    .ball {
        display: inline-block;
        width: 40px;
        height: 40px;
        line-height: 40px;
        border-radius: 50%;
        text-align: center;
        color: white !important;
        font-weight: bold;
        font-size: 15px;
        margin: 2px;
        box-shadow: inset -2px -2px 4px rgba(0,0,0,0.2);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎰 행님 로또 명당")

# 3. 로직 (통계 기반 추출)
frequent = [1, 10, 12, 13, 14, 17, 18, 21, 24, 26, 27, 33, 34, 39, 40, 43, 45]
def pick_lotto():
    h = random.sample(frequent, 3)
    others = [n for n in range(1, 46) if n not in h]
    return sorted(h + random.sample(others, 3))

def get_c(n):
    if n <= 10: return "#fbc400"
    if n <= 20: return "#69c8f2"
    if n <= 30: return "#ff7272"
    if n <= 40: return "#aaaaaa"
    return "#b0d840"

# 4. 세션 관리
if 'bundles' not in st.session_state:
    st.session_state.bundles = [[pick_lotto() for _ in range(5)]]

# 5. 상단 버튼 (1:1 비율)
c1, c2 = st.columns(2)
with c1:
    if st.button("🔄 번호 새로고침"):
        st.session_state.bundles = [[pick_lotto() for _ in range(5)]]
        st.rerun()
with c2:
    if st.button("➕ 5세트 추가"):
        st.session_state.bundles.append([pick_lotto() for _ in range(5)])

# 6. 결과 출력 (가장 안정적인 columns 방식)
for b_idx, bundle in enumerate(st.session_state.bundles):
    # Streamlit 공식 테두리 상자 사용 (절대 안 깨짐)
    with st.container(border=True):
        st.caption(f"SET {b_idx + 1}")
        for i, nums in enumerate(bundle):
            # 라벨과 공을 1:9 비율로 배치
            row_cols = st.columns([1, 9])
            with row_cols[0]:
                st.markdown(f"<div style='padding-top:10px; color:#ccc; font-weight:bold;'>#{i+1}</div>", unsafe_allow_html=True)
            with row_cols[1]:
                # 공 6개를 안전하게 한 줄로 출력
                balls_html = "".join([f'<div class="ball" style="background-color:{get_c(n)}">{n}</div>' for n in nums])
                st.markdown(balls_html, unsafe_allow_html=True)

st.divider()
st.info("행님, 이번 코드는 Streamlit의 정석대로 짰습니다. 이제는 진짜 반영될 겁니다!")
