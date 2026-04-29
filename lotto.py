import streamlit as st
import random

# 1. 페이지 설정
st.set_page_config(page_title="행님 로또 명당", page_icon="🎰", layout="centered")

# 2. 시원시원한 UI를 위한 CSS
st.markdown("""
    <style>
    .main .block-container {
        padding: 1.5rem 1rem !important;
        max-width: 500px !important;
    }
    /* 버튼 시인성 강화 */
    .stButton>button {
        width: 100%;
        height: 3.5em;
        font-size: 1.1rem !important;
        font-weight: bold !important;
        border-radius: 12px;
        background-color: #2E7D32;
        color: white;
    }
    /* 세트 박스 - 크기 확장 */
    .bundle-box {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 15px;
        padding: 15px 10px;
        margin-bottom: 20px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.08);
    }
    /* 조합 한 줄 - 간격 및 높이 조절 */
    .lotto-line {
        display: flex;
        align-items: center;
        padding: 10px 0 !important;
        border-bottom: 1px solid #f5f5f5;
    }
    .lotto-line:last-child { border-bottom: none; }
    
    .label { 
        width: 45px; 
        font-size: 0.9rem; 
        color: #888; 
        font-weight: bold; 
        text-align: center;
    }
    .balls { 
        display: flex; 
        gap: 8px; /* 공 사이 간격 넓힘 */
        margin-left: 10px;
    }
    
    /* 공 크기 키움 (시원한 가시성) */
    .b {
        width: 42px;
        height: 42px;
        line-height: 42px;
        border-radius: 50%;
        text-align: center;
        color: white;
        font-weight: bold;
        font-size: 16px;
        box-shadow: 1px 2px 4px rgba(0,0,0,0.2);
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
    if n <= 10: return "#fbc400" # 노랑
    if n <= 20: return "#69c8f2" # 파랑
    if n <= 30: return "#ff7272" # 빨강
    if n <= 40: return "#aaaaaa" # 회색
    return "#b0d840" # 초록

# 4. 세션 관리
if 'bundles' not in st.session_state:
    st.session_state.bundles = [[pick() for _ in range(5)]]

col1, col2 = st.columns(2)
with col1:
    if st.button("🔄 새로고침"):
        st.session_state.bundles = [[pick() for _ in range(5)]]
        st.rerun()
with col2:
    if st.button("➕ 5세트 추가"):
        st.session_state.bundles.append([pick() for _ in range(5)])

# 5. 출력
for idx, bundle in enumerate(st.session_state.bundles):
    html = f'<div class="bundle-box"><div style="font-size:0.8rem; color:#aaa; margin-bottom:10px; font-weight:bold; padding-left:10px;">SET {idx+1}</div>'
    for i, nums in enumerate(bundle):
        balls = "".join([f'<div class="b" style="background-color:{get_c(n)}">{n}</div>' for n in nums])
        html += f'<div class="lotto-line"><div class="label">#{i+1}</div><div class="balls">{balls}</div></div>'
    html += '</div>'
    st.write(html, unsafe_allow_html=True)

st.divider()
st.info("행님, 이제 공이 큼직하니 보기 편하시죠? 좋은 소식 기대하겠습니다!")
