import streamlit as st
import random

# 1. 페이지 설정
st.set_page_config(page_title="행님 로또 명당", page_icon="🎰", layout="centered")

# 2. 강력한 일체형 디자인 CSS
st.markdown("""
    <style>
    .main .block-container { padding: 1.5rem 0.5rem !important; max-width: 450px !important; }
    .stButton>button { width: 100%; border-radius: 12px; height: 3.5rem; font-weight: bold !important; }
    
    /* 세트 전체 카드 */
    .bundle-card {
        background: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 15px;
        padding: 15px 8px;
        margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }
    
    /* 한 줄 레이아웃 (Flex 사용으로 절대 안 깨짐) */
    .lotto-row {
        display: flex;
        align-items: center;
        padding: 8px 0;
        border-bottom: 1px solid #f8f9fa;
        min-height: 50px;
    }
    .lotto-row:last-child { border-bottom: none; }
    
    .label-box {
        width: 40px;
        font-size: 0.8rem;
        font-weight: bold;
        color: #ced4da;
        text-align: center;
        flex-shrink: 0;
    }
    
    .ball-box {
        display: flex;
        flex-grow: 1;
        justify-content: space-around;
        align-items: center;
    }
    
    /* 공 디자인 */
    .ball {
        width: 38px;
        height: 38px;
        line-height: 38px;
        border-radius: 50%;
        text-align: center;
        color: white !important;
        font-weight: bold;
        font-size: 15px;
        box-shadow: inset -2px -2px 4px rgba(0,0,0,0.2);
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

# 4. 버튼
c1, c2 = st.columns(2)
with c1:
    if st.button("🔄 새로고침"):
        st.session_state.bundles = [[pick() for _ in range(5)]]
        st.rerun()
with c2:
    if st.button("➕ 5세트 추가"):
        st.session_state.bundles.append([pick() for _ in range(5)])

# 5. 출력 (안 깨지게 문자열 완벽 조합 후 출력)
for b_idx, bundle in enumerate(st.session_state.bundles):
    # 각 세트 박스 내부의 모든 줄을 미리 생성
    rows_html = ""
    for i, nums in enumerate(bundle):
        balls_html = "".join([f'<div class="ball" style="background-color:{get_c(n)}">{n}</div>' for n in nums])
        rows_html += f'''
            <div class="lotto-row">
                <div class="label-box">#{i+1}</div>
                <div class="ball-box">{balls_html}</div>
            </div>
        '''
    
    # 세트 제목 + 모든 줄을 하나의 div(bundle-card)로 묶어서 단 한 번에 출력
    final_card_html = f'''
        <div class="bundle-card">
            <div style="font-size:0.75rem; color:#ced4da; margin-bottom:5px; font-weight:bold; padding-left:5px;">SET {b_idx + 1}</div>
            {rows_html}
        </div>
    '''
    st.markdown(final_card_html, unsafe_allow_html=True)

st.divider()
st.info("행님, 이제 위아래 뒤바뀌는 일 없이 프레임 안에 꽉 차게 나올 겁니다!")
