import streamlit as st
import random

# 1. 페이지 설정
st.set_page_config(page_title="행님 로또 명당", page_icon="🎰", layout="centered")

# 2. 스타일 설정 (공 디자인 및 간격 최적화)
st.markdown("""
    <style>
    .main .block-container { padding: 1rem 0.5rem !important; max-width: 500px !important; }
    .stButton>button { width: 100%; border-radius: 12px; height: 3.5rem; font-weight: bold !important; }
    
    /* 세트 박스 디자인 */
    .set-container {
        border: 1px solid #eee;
        border-radius: 15px;
        padding: 15px 10px;
        margin-bottom: 20px;
        background-color: white;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    
    /* 세트 제목 스타일 */
    .set-title {
        font-size: 0.85rem;
        font-weight: bold;
        color: #bbb;
        margin-bottom: 10px;
        padding-left: 5px;
    }

    /* 로또 공 디자인 */
    .ball-style {
        display: inline-block;
        width: 38px; height: 38px; line-height: 38px;
        border-radius: 50%; text-align: center;
        color: white !important; font-weight: bold; font-size: 15px;
        margin: 2px;
        box-shadow: inset -2px -2px 4px rgba(0,0,0,0.15);
    }

    /* 번호 라벨 스타일 */
    .row-label {
        font-size: 0.9rem;
        font-weight: bold;
        color: #ccc;
        margin-right: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎰 행님 로또 명당")

# 3. 로직 (통계 기반 추출)
frequent_pool = [1, 10, 12, 13, 14, 17, 18, 21, 24, 26, 27, 33, 34, 39, 40, 43, 45]

def generate_lotto():
    high_part = random.sample(frequent_pool, 3)
    others = [n for n in range(1, 46) if n not in high_part]
    low_part = random.sample(others, 3)
    return sorted(high_part + low_part)

def get_color(n):
    if n <= 10: return "#fbc400"
    if n <= 20: return "#69c8f2"
    if n <= 30: return "#ff7272"
    if n <= 40: return "#aaaaaa"
    return "#b0d840"

# 4. 세션 관리
if 'bundles' not in st.session_state:
    st.session_state.bundles = [[generate_lotto() for _ in range(5)]]

# 5. 조작 버튼
col1, col2 = st.columns(2)
with col1:
    if st.button("🔄 전체 새로고침"):
        st.session_state.bundles = [[generate_lotto() for _ in range(5)]]
        st.rerun()
with col2:
    if st.button("➕ 5세트 추가"):
        st.session_state.bundles.append([generate_lotto() for _ in range(5)])

# 6. 결과 출력 (Expander 제거 버전)
for b_idx, bundle in enumerate(st.session_state.bundles):
    # 카드 전체를 감싸는 컨테이너 시작
    st.markdown(f'<div class="set-container">', unsafe_allow_html=True)
    st.markdown(f'<div class="set-title">SET {b_idx + 1}</div>', unsafe_allow_html=True)
    
    for i, nums in enumerate(bundle):
        # 번호 라벨과 공을 컬럼으로 분리 (라벨은 작게, 공은 넓게)
        c_idx, c_balls = st.columns([1, 8])
        with c_idx:
            st.markdown(f"<div style='padding-top:10px;' class='row-label'>#{i+1}</div>", unsafe_allow_html=True)
        with c_balls:
            balls_html = "".join([
                f'<span class="ball-style" style="background-color:{get_color(n)}">{n}</span>' 
                for n in nums
            ])
            st.markdown(balls_html, unsafe_allow_html=True)
            
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()
st.info("행님, 이제 거슬리는 거 없이 깔끔하게 나옵니다. 이번 주 대박 번호는 이 안에 있습니다! 🚀")
