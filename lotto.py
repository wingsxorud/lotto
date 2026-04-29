import streamlit as st
import random

# 1. 페이지 설정 및 모바일 화면 고정
st.set_page_config(
    page_title="행님 로또 명당", 
    page_icon="🎰", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. 모바일 반응형 CSS (영혼을 갈아넣었습니다 행님)
st.markdown("""
    <style>
    /* 1. Streamlit 기본 패딩 강제 제거 */
    .main .block-container {
        padding: 10px 5px !important;
        max-width: 100% !important;
    }
    
    /* 2. 제목 스타일 최적화 */
    .title-text {
        font-size: 1.8rem !important;
        font-weight: 800;
        text-align: center;
        margin-bottom: 20px;
        color: #333;
    }

    /* 3. 버튼 레이아웃 - 모바일에서 나란히 배치 */
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3.5rem;
        font-weight: bold !important;
        font-size: 1rem !important;
    }

    /* 4. 세트 박스 - 모바일 폭에 맞게 패딩 조절 */
    .bundle-card {
        background: #ffffff;
        border: 1px solid #eee;
        border-radius: 15px;
        padding: 10px 5px;
        margin: 10px 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }

    /* 5. 로또 줄 레이아웃 - 핵심 */
    .lotto-row {
        display: flex;
        align-items: center;
        justify-content: flex-start;
        padding: 8px 0;
        border-bottom: 1px solid #f9f9f9;
        width: 100%;
    }
    .lotto-row:last-child { border-bottom: none; }

    .row-idx {
        width: 35px;
        font-size: 0.8rem;
        color: #999;
        font-weight: bold;
        flex-shrink: 0;
        text-align: center;
    }

    /* 6. 공 컨테이너 - 화면 폭에 맞춰 자동 조절 */
    .ball-container {
        display: flex;
        justify-content: space-between;
        flex-grow: 1;
        max-width: calc(100% - 45px); /* 번호 라벨 제외한 나머지 공간 */
        padding-right: 5px;
    }

    /* 7. 반응형 공 디자인 */
    .ball {
        width: 13vw; /* 화면 폭의 13% 크기 (반응형) */
        height: 13vw;
        max-width: 45px; /* 너무 커지는 것 방지 */
        max-height: 45px;
        line-height: 13vw;
        border-radius: 50%;
        text-align: center;
        color: white !important;
        font-weight: bold;
        font-size: 1rem;
        box-shadow: inset -2px -2px 4px rgba(0,0,0,0.2);
    }
    
    /* 숫자 위치 보정 (라인 높이 맞춤) */
    @media (min-width: 450px) {
        .ball { line-height: 45px; font-size: 1.1rem; }
    }
    @media (max-width: 450px) {
        .ball { line-height: 13vw; font-size: 0.9rem; }
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="title-text">🎰 행님 로또 명당</div>', unsafe_allow_html=True)

# 3. 번호 생성 로직
frequent_nums = [1, 10, 12, 13, 14, 17, 18, 21, 24, 26, 27, 33, 34, 39, 40, 43, 45]

def generate_lotto():
    picks = random.sample(frequent_nums, 3)
    others = [n for n in range(1, 46) if n not in picks]
    return sorted(picks + random.sample(others, 3))

def ball_color(n):
    if n <= 10: return "#fbc400"
    if n <= 20: return "#69c8f2"
    if n <= 30: return "#ff7272"
    if n <= 40: return "#aaaaaa"
    return "#b0d840"

# 4. 세션 관리
if 'bundles' not in st.session_state:
    st.session_state.bundles = [[generate_lotto() for _ in range(5)]]

# 5. 상단 버튼 (모바일 2열)
col1, col2 = st.columns(2)
with col1:
    if st.button("🔄 새로고침"):
        st.session_state.bundles = [[generate_lotto() for _ in range(5)]]
        st.rerun()
with col2:
    if st.button("➕ 5세트 추가"):
        st.session_state.bundles.append([generate_lotto() for _ in range(5)])

# 6. 결과 렌더링
for b_idx, bundle in enumerate(st.session_state.bundles):
    html = f'<div class="bundle-card">'
    html += f'<div style="font-size:0.7rem; color:#bbb; margin-left:10px; margin-bottom:5px;">SET {b_idx + 1}</div>'
    
    for i, nums in enumerate(bundle):
        balls_html = "".join([
            f'<div class="ball" style="background-color:{ball_color(n)}">{n}</div>' 
            for n in nums
        ])
        html += f'''
            <div class="lotto-row">
                <div class="row-idx">#{i+1}</div>
                <div class="ball-container">{balls_html}</div>
            </div>
        '''
    html += '</div>'
    st.write(html, unsafe_allow_html=True)

st.divider()
st.info("행님, 폰 화면에 딱 맞췄습니다! 캡처해서 대박 나십쇼! 🚀")
