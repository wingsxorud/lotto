import streamlit as st
import random

# 1. 페이지 설정
st.set_page_config(page_title="행님 로또 명당", page_icon="🎰", layout="centered")

# 2. 필수 스타일 (공 디자인만 딱 잡았습니다)
st.markdown("""
    <style>
    .main .block-container { padding: 1rem 0.5rem !important; max-width: 500px !important; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3.5rem; font-weight: bold !important; }
    
    /* 공 디자인 - 절대 안 깨지게 클래스 간소화 */
    .lotto-ball {
        display: inline-block;
        width: 40px; height: 40px; line-height: 40px;
        border-radius: 50%; text-align: center;
        color: white !important; font-weight: bold; font-size: 16px;
        margin: 2px;
        box-shadow: inset -2px -2px 4px rgba(0,0,0,0.2);
    }
    /* 세트 박스 테두리 */
    .bundle-card {
        border: 1px solid #eee; border-radius: 15px;
        padding: 15px 5px; margin-bottom: 20px;
        background-color: white; box-shadow: 0 2px 10px rgba(0,0,0,0.05);
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

if 'bundles' not in st.session_state:
    st.session_state.bundles = [[pick() for _ in range(5)]]

# 4. 상단 버튼
c1, c2 = st.columns(2)
with c1:
    if st.button("🔄 새로고침"):
        st.session_state.bundles = [[pick() for _ in range(5)]]
        st.rerun()
with c2:
    if st.button("➕ 5세트 추가"):
        st.session_state.bundles.append([pick() for _ in range(5)])

# 5. 출력부 (안 깨지도록 개별 렌더링 방식 채택)
for b_idx, bundle in enumerate(st.session_state.bundles):
    with st.container():
        # 세트 박스 시작 (카드 형태로 감싸기)
        st.markdown(f'<div class="bundle-card">', unsafe_allow_html=True)
        st.caption(f"SET {b_idx + 1}")
        
        for i, nums in enumerate(bundle):
            # 번호 한 줄씩 출력
            cols = st.columns([1, 8])
            with cols[0]:
                st.markdown(f"<div style='padding-top:10px; color:#ccc; font-weight:bold;'>#{i+1}</div>", unsafe_allow_html=True)
            with cols[1]:
                # 공들을 하나의 문자열로 만들어 한 번에 출력
                balls_html = "".join([f'<div class="lotto-ball" style="background-color:{get_c(n)}">{n}</div>' for n in nums])
                st.markdown(balls_html, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

st.divider()
st.info("행님, 이제 절대 안 깨질 겁니다! 이번 주 주인공은 행님입니다! 🚀")
