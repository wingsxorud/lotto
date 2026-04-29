import streamlit as st
import random

# 1. 페이지 설정 및 강제 여백 제거 (최상단)
st.set_page_config(page_title="행님 로또", page_icon="🎰", layout="centered")

# 2. 강력한 스타일 시트 (Streamlit 기본 디자인 무력화)
st.markdown("""
    <style>
    /* 앱 전체 여백 제거 */
    .main .block-container {
        padding: 10px 5px !important;
        max-width: 400px !important;
    }
    /* 제목 간격 줄이기 */
    h1 { margin-top: -30px !important; padding-bottom: 10px !important; font-size: 1.5rem !important; }
    
    /* 세트 박스 (세트 간 간격도 줄임) */
    .bundle-box {
        background-color: #fff;
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 8px;
        margin-bottom: 8px;
    }
    /* 조합 한 줄 (위아래 여백 거의 0) */
    .lotto-line {
        display: flex;
        align-items: center;
        padding: 2px 0 !important;
        margin: 0 !important;
        border-bottom: 1px solid #f0f0f0;
    }
    .lotto-line:last-child { border-bottom: none; }
    
    .label { width: 30px; font-size: 11px; color: #aaa; font-weight: bold; }
    .balls { display: flex; gap: 3px; }
    
    /* 공 크기 최적화 (모바일용) */
    .b {
        width: 28px;
        height: 28px;
        line-height: 28px;
        border-radius: 50%;
        text-align: center;
        color: white;
        font-weight: bold;
        font-size: 13px;
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

# 5. 출력 (최대한 밀착된 HTML 조립)
for idx, bundle in enumerate(st.session_state.bundles):
    html = f'<div class="bundle-box"><div style="font-size:10px; color:#ccc;">SET {idx+1}</div>'
    for i, nums in enumerate(bundle):
        balls = "".join([f'<div class="b" style="background-color:{get_c(n)}">{n}</div>' for n in nums])
        html += f'<div class="lotto-line"><div class="label">#{i+1}</div><div class="balls">{balls}</div></div>'
    html += '</div>'
    st.write(html, unsafe_allow_html=True)

st.caption("행님, 간격을 영혼까지 끌어모아 줄였습니다! 대박 나십쇼!")
