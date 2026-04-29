import streamlit as st
import random

# 1. 페이지 설정
st.set_page_config(page_title="행님 로또 명당", page_icon="🎰", layout="centered")

# 2. 공 모양을 위한 필수 스타일만 최소한으로 적용
st.markdown("""
    <style>
    .main .block-container { padding: 1rem 0.5rem !important; max-width: 450px !important; }
    .stButton>button { width: 100%; border-radius: 12px; height: 3.5rem; font-weight: bold !important; }
    
    /* 공 모양 스타일 - span 태그로 안전하게 사용 */
    .lotto-ball {
        display: inline-block;
        width: 38px; height: 38px; line-height: 38px;
        border-radius: 50%; text-align: center;
        color: white !important; font-weight: bold; font-size: 15px;
        margin: 2px;
        box-shadow: inset -2px -2px 4px rgba(0,0,0,0.15);
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

# 6. 결과 출력 (Streamlit 컨테이너 위젯으로 물리적 격리)
for b_idx, bundle in enumerate(st.session_state.bundles):
    # 테두리가 있는 상자(container)를 생성
    with st.container(border=True):
        st.caption(f"SET {b_idx + 1}")
        
        for i, nums in enumerate(bundle):
            # 라벨(1) : 번호(8) 비율로 컬럼 배치
            c_idx, c_balls = st.columns([1, 8])
            
            with c_idx:
                st.markdown(f"<div style='padding-top:8px; color:#ccc; font-weight:bold;'>#{i+1}</div>", unsafe_allow_html=True)
            
            with c_balls:
                # 공 6개를 하나의 문자열로 렌더링 (가장 안정적인 방식)
                balls_html = "".join([
                    f'<span class="lotto-ball" style="background-color:{get_color(n)}">{n}</span>' 
                    for n in nums
                ])
                st.write(balls_html, unsafe_allow_html=True)

st.divider()
st.info("행님, Streamlit 순정 테두리 기능을 써서 이제 절대로 밖으로 안 나갑니다! 🚀")
