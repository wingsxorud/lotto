import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="행님 로또 명당", page_icon="🎰", layout="centered")

# 간격 극최소화 및 모바일 최적화 CSS
st.markdown("""
    <style>
    /* 화면 좌우 여백 최적화 */
    .block-container {
        padding: 1rem 0.5rem !important;
        max-width: 450px;
    }
    .stButton>button {
        width: 100%;
        height: 3.2em;
        font-weight: bold !important;
        border-radius: 12px;
    }
    /* 세트 묶음 박스 */
    .lotto-bundle {
        background-color: #ffffff;
        border: 1px solid #dee2e6;
        border-radius: 15px;
        padding: 12px 8px;
        margin-bottom: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    /* 각 번호 줄 간격 밀착 */
    .lotto-row {
        display: flex;
        align-items: center;
        padding: 5px 0;
        border-bottom: 1px solid #f8f9fa;
    }
    .lotto-row:last-child { border-bottom: none; }
    
    .lotto-label {
        font-size: 0.75rem;
        font-weight: bold;
        color: #adb5bd;
        width: 35px;
        text-align: center;
    }
    .ball-container {
        display: flex;
        gap: 5px;
        margin-left: 5px;
    }
    .lotto-ball {
        width: 32px;
        height: 32px;
        line-height: 32px;
        border-radius: 50%;
        text-align: center;
        color: white;
        font-weight: bold;
        font-size: 14px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎰 행님 로또 명당")

# 로직 (최다 빈도수 가중치)
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

# 세션 상태 관리
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

# 로또 번호 출력
for b_idx, bundle in enumerate(st.session_state.lotto_bundles):
    # 각 세트 시작
    html_out = f'<div class="lotto-bundle">'
    html_out += f'<div style="font-size:0.7rem; color:#ced4da; margin-bottom:5px; font-weight:bold;">SET {b_idx + 1}</div>'
    
    for i, nums in enumerate(bundle):
        balls_html = "".join([
            f'<div class="lotto-ball" style="background-color:{get_ball_color(n)}">{n}</div>' 
            for n in nums
        ])
        # 한 줄씩 추가
        html_out += f'''
            <div class="lotto-row">
                <div class="lotto-label">#{i+1}</div>
                <div class="ball-container">{balls_html}</div>
            </div>
        '''
    
    html_out += '</div>' # 세트 닫기
    st.markdown(html_out, unsafe_allow_html=True)

st.divider()
st.caption("캡처 후 갤러리에 저장해서 사용하세요. 행님 대박 기원!")
