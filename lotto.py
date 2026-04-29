import streamlit as st
import random

# 1. 페이지 설정
st.set_page_config(page_title="행님 로또 명당", page_icon="🎰", layout="centered")

# 2. 디자인 정밀 보정 CSS
st.markdown("""
    <style>
    .main .block-container { padding: 1rem 0.5rem !important; max-width: 450px !important; }
    .stButton>button { width: 100%; border-radius: 12px; height: 3.5rem; font-weight: bold !important; }
    
    /* 세트 카드 디자인 - 프레임 일체화 */
    .bundle-card {
        background: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 15px;
        padding: 15px 10px;
        margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }
    
    /* 테이블 레이아웃으로 간격 고정 */
    .lotto-table {
        width: 100%;
        border-collapse: collapse;
    }
    .lotto-row {
        height: 50px;
        border-bottom: 1px solid #f8f9fa;
    }
    .lotto-row:last-child { border-bottom: none; }
    
    .label-cell {
        width: 40px;
        font-size: 0.8rem;
        font-weight: bold;
        color: #bbb;
        text-align: center;
    }
    .ball-cell {
        display: flex;
        justify-content: space-around;
        align-items: center;
        padding: 5px 0;
    }
    
    /* 공 디자인 (반응형 크기) */
    .ball {
        width: 36px;
        height: 36px;
        line-height: 36px;
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

# 3. 번호 추출 로직
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

# 4. 버튼 영역
c1, c2 = st.columns(2)
with c1:
    if st.button("🔄 전체 새로고침"):
        st.session_state.bundles = [[pick() for _ in range(5)]]
        st.rerun()
with c2:
    if st.button("➕ 5조합 세트 추가"):
        st.session_state.bundles.append([pick() for _ in range(5)])

# 5. 출력 영역 (테이블 구조로 일체화)
for b_idx, bundle in enumerate(st.session_state.bundles):
    # 세트 카드 시작
    html_bundle = f'<div class="bundle-card">'
    html_bundle += f'<div style="font-size:0.75rem; color:#ced4da; margin-bottom:10px; font-weight:bold; padding-left:5px;">SET {b_idx + 1}</div>'
    html_bundle += '<table class="lotto-table">'
    
    for i, nums in enumerate(bundle):
        balls_html = "".join([f'<div class="ball" style="background-color:{get_c(n)}">{n}</div>' for n in nums])
        html_bundle += f'''
            <tr class="lotto-row">
                <td class="label-cell">#{i+1}</td>
                <td class="ball-cell">{balls_html}</td>
            </tr>
        '''
    
    html_bundle += '</table></div>'
    st.write(html_bundle, unsafe_allow_html=True)

st.divider()
st.info("행님, 이제 프레임이랑 번호가 한 몸처럼 딱 붙어 나올 겁니다!")
