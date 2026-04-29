import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="행님 로또 명당", page_icon="🎰", layout="centered")

# 간격 극최소화 및 세트 박스 디자인
st.markdown("""
    <style>
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 1rem !important;
        max-width: 450px;
    }
    .stButton>button {
        width: 100%;
        height: 3em;
        font-weight: bold !important;
        border-radius: 10px;
    }
    /* 5개 조합을 묶는 세트 박스 */
    .lotto-bundle {
        background-color: #ffffff;
        border: 2px solid #e9ecef;
        border-radius: 15px;
        padding: 10px;
        margin-bottom: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    /* 조합 한 줄 레이아웃 */
    .lotto-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 4px 0;
        border-bottom: 1px solid #f8f9fa;
    }
    .lotto-row:last-child { border-bottom: none; }
    
    .lotto-label {
        font-size: 0.8rem;
        font-weight: bold;
        color: #666;
        width: 45px;
    }
    .ball-container {
        display: flex;
        gap: 4px;
    }
    .lotto-ball {
        width: 30px;
        height: 30px;
        line-height: 30px;
        border-radius: 50%;
        text-align: center;
        color: white;
        font-weight: bold;
        font-size: 13px;
        box-shadow: inset -2px -2px 4px rgba(0,0,0,0.2);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎰 행님 로또 명당")

# 데이터 로직
frequent_numbers = [1, 10, 12, 13, 14, 17, 18, 21, 24, 26, 27, 33, 34, 39, 40, 43, 45]

def get_lotto_numbers():
    high_pick = random.sample(frequent_numbers, 3)
    others = [n for n in range(1, 46) if n not in high_pick]
    low_pick = random.sample(others, 3)
    return sorted(high_pick + low_pick)

def get_ball_color(num):
    if 1 <= num <= 10: return "#fbc400"
    if 11 <= num <= 20: return "#69c8f2"
    if 21 <= num <= 30: return "#ff7272"
    if 31 <= num <= 40: return "#aaaaaa"
    return "#b0d840"

# 세션 상태 관리 (세트 단위로 저장)
if 'lotto_bundles' not in st.session_state:
    st.session_state.lotto_bundles = [[get_lotto_numbers() for _ in range(5)]]

col1, col2 = st.columns(2)
with col1:
    if st.button("🔄 전체 새로고침"):
        st.session_state.lotto_bundles = [[get_lotto_numbers() for _ in range(5)]]
        st.rerun()
with col2:
    if st.button("➕ 5조합 세트 추가"):
        st.session_state.lotto_bundles.append([get_lotto_numbers() for _ in range(5)])

# 로또 번호 출력 (세트 단위 묶음)
for b_idx, bundle in enumerate(st.session_state.lotto_bundles):
    bundle_html = f'<div class="lotto-bundle">'
    bundle_html += f'<div style="font-size:0.7rem; color:#999; margin-bottom:5px;">SET {b_idx + 1}</div>'
    
    for i, nums in enumerate(bundle):
        balls_html = "".join([
            f'<div class="lotto-ball" style="background-color:{get_ball_color(n)}">{n}</div>' 
            for n in nums
        ])
        bundle_html += f'''
            <div class="lotto-row">
                <div class="lotto-label">#{i+1}</div>
                <div class="ball-container">{balls_html}</div>
            </div>
        '''
    bundle_html += '</div>'
    st.markdown(bundle_html, unsafe_allow_html=True)

st.divider()
st.caption("행님, 이 세트 그대로 캡처해서 로또방 가시면 됩니다! 대박 나십쇼!")
