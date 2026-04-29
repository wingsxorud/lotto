import streamlit as st
import random

# 1. 페이지 설정
st.set_page_config(page_title="행님 로또 명당", page_icon="🎰", layout="centered")

# 2. 스타일 설정 (공 디자인 및 카드 프레임)
st.markdown("""
    <style>
    .main .block-container { padding: 1.5rem 0.5rem !important; max-width: 500px !important; }
    .stButton>button { width: 100%; border-radius: 12px; height: 3.5rem; font-weight: bold !important; }
    
    /* 카드 프레임 스타일 */
    .lotto-card {
        border: 1px solid #e0e0e0;
        border-radius: 15px;
        padding: 20px 10px;
        margin-bottom: 20px;
        background-color: #ffffff;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
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

    /* 세트 제목 */
    .set-header {
        font-size: 0.8rem;
        font-weight: bold;
        color: #bbb;
        margin-bottom: 15px;
        padding-left: 5px;
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

# 6. 결과 출력 (프레임 내부에 확실히 가두기)
for b_idx, bundle in enumerate(st.session_state.bundles):
    # div 태그를 직접 열고 닫아 프레임을 형성
    st.markdown(f'<div class="lotto-card">', unsafe_allow_html=True)
    st.markdown(f'<div class="set-header">SET {b_idx + 1}</div>', unsafe_allow_html=True)
    
    for i, nums in enumerate(bundle):
        # 한 줄씩 가로로 배치 (번호 라벨 1 : 공들 8)
        c_idx, c_balls = st.columns([1, 8])
        with c_idx:
            st.markdown(f"<div style='padding-top:8px; color:#ddd; font-weight:bold; font-size:13px;'>#{i+1}</div>", unsafe_allow_html=True)
        with c_balls:
            balls_html = "".join([
                f'<span class="ball-style" style="background-color:{get_color(n)}">{n}</span>' 
                for n in nums
            ])
            st.markdown(balls_html, unsafe_allow_html=True)
            
    st.markdown('</div>', unsafe_allow_html=True) # 프레임 확실히 닫기

st.divider()
st.info("행님, 이제 프레임 안으로 공들이 쏙 들어갔습니다! 확인 한번 부탁드려요! 🚀")
