import streamlit as st
import random

# 1. 페이지 설정 및 모바일 최적화 (가로 폭 꽉 채우기)
st.set_page_config(page_title="행님 로또 명당", page_icon="🎰", layout="centered")

# 2. 강력한 스타일 보정 (여백 제거 및 프레임 확장)
st.markdown("""
    <style>
    /* 1. 기본 Streamlit 여백 제거 */
    .main .block-container {
        padding: 1rem 0.5rem !important;
        max-width: 100% !important;
    }
    
    /* 2. 세트 박스 - 가로 폭 확장 및 정렬 */
    .stElementContainer div[data-testid="stVerticalBlockBorderWrapper"] {
        padding: 0 !important;
    }
    
    /* 3. 로또 공 디자인 (크기 최적화) */
    .lotto-ball {
        display: inline-block;
        width: 13vw; /* 화면 폭에 맞춘 반응형 크기 */
        height: 13vw;
        max-width: 42px;
        max-height: 42px;
        line-height: 13vw;
        border-radius: 50%;
        text-align: center;
        color: white !important;
        font-weight: bold;
        font-size: 1rem;
        margin: 1px;
        box-shadow: inset -2px -2px 4px rgba(0,0,0,0.15);
    }
    /* 큰 화면 대비 보정 */
    @media (min-width: 450px) {
        .lotto-ball { line-height: 42px; font-size: 1.1rem; }
    }

    /* 4. 버튼 스타일 */
    .stButton>button { width: 100%; border-radius: 12px; height: 3.5rem; font-weight: bold !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎰 행님 로또 명당")

# 3. 로직 (통계 기반)
frequent_pool = [1, 10, 12, 13, 14, 17, 18, 21, 24, 26, 27, 33, 34, 39, 40, 43, 45]
def generate_lotto():
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
    st.session_state.bundles = [[generate_lotto() for _ in range(5)]]

# 5. 버튼
c1, c2 = st.columns(2)
with c1:
    if st.button("🔄 새로고침"):
        st.session_state.bundles = [[generate_lotto() for _ in range(5)]]
        st.rerun()
with c2:
    if st.button("➕ 5세트 추가"):
        st.session_state.bundles.append([generate_lotto() for _ in range(5)])

# 6. 결과 출력 (프레임 꽉 채우기)
for b_idx, bundle in enumerate(st.session_state.bundles):
    # border=True로 생성되는 프레임 내부 여백을 최소화
    with st.container(border=True):
        st.caption(f"SET {b_idx + 1}")
        for i, nums in enumerate(bundle):
            # 라벨 비율을 줄여서 공들이 넓게 퍼지게 함
            c_idx, c_balls = st.columns([0.8, 9])
            with c_idx:
                st.markdown(f"<div style='padding-top:10px; color:#ccc; font-weight:bold; font-size:12px;'>#{i+1}</div>", unsafe_allow_html=True)
            with c_balls:
                # flex를 사용해 공 간격을 균등하게 벌림
                balls_html = "".join([f'<span class="lotto-ball" style="background-color:{get_color(n)}">{n}</span>' for n in nums])
                st.markdown(f'<div style="display:flex; justify-content:space-between; width:100%;">{balls_html}</div>', unsafe_allow_html=True)

st.divider()
st.info("행님, 이제 프레임이 화면 끝까지 닿고 공들도 시원시원하게 보일 겁니다! 🚀")
