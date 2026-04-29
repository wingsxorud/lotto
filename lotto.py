import streamlit as st
import random

# 1. 페이지 설정
st.set_page_config(page_title="1등 번호 추첨기", page_icon="🎰", layout="centered")

# 2. 디자인 설정 (프레임 축소 및 버튼 간격 밀착)
st.markdown("""
    <style>
    /* 전체 프레임 폭 조절 (400px로 컴팩트하게) */
    .main .block-container { 
        padding: 1.5rem 0.5rem !important; 
        max-width: 400px !important; 
    }
    
    /* 버튼 사이 간격 좁히기 (핵심!) */
    div[data-testid="stHorizontalBlock"] {
        gap: 2px !important;
    }
    
    .stButton>button { 
        width: 100%; 
        border-radius: 12px; 
        height: 3.5rem; 
        font-weight: bold !important; 
    }
    
    /* 로또 공 디자인 */
    .ball-style {
        display: inline-block;
        width: 38px; height: 38px; line-height: 38px;
        border-radius: 50%; text-align: center;
        color: white !important; font-weight: bold; font-size: 15px;
        margin: 2px;
        box-shadow: inset -2px -2px 4px rgba(0,0,0,0.2);
    }
    
    /* Expander 내부 여백 조절 */
    .streamlit-expanderContent { padding: 10px 5px !important; }
    </style>
    """, unsafe_allow_html=True)


st.title("🎰 나눔로또")

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
    if st.button("🔄 새로고침"):
        st.session_state.bundles = [[generate_lotto() for _ in range(5)]]
        st.rerun()
with col2:
    if st.button("➕ 5세트 추가"):
        st.session_state.bundles.append([generate_lotto() for _ in range(5)])

# 6. 결과 출력
for b_idx, bundle in enumerate(st.session_state.bundles):
    with st.expander(f"set {b_idx + 1}", expanded=True):
        for i, nums in enumerate(bundle):
            # 번호 라벨 비율을 살짝 줄여서 공간 확보
            cols = st.columns([0.15, 0.85])
            cols[0].markdown(f"<div style='padding-top:10px; font-weight:bold; color:#ccc;'>#{i+1}</div>", unsafe_allow_html=True)
            
            balls_html = "".join([
                f'<span class="ball-style" style="background-color:{get_color(n)}">{n}</span>' 
                for n in nums
            ])
            cols[1].markdown(balls_html, unsafe_allow_html=True)

st.divider()
st.info("행님, 이제 버튼도 딲! 붙어 있고 프레임도 아주 깔끔합니다! 🚀")
