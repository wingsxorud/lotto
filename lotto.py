import streamlit as st
import random

# 1. 페이지 기본 설정
st.set_page_config(page_title="행님 로또 명당", page_icon="🎰", layout="centered")

# 2. 모바일 밀착형 CSS 최적화
st.markdown("""
    <style>
    /* 전체 여백 줄이기 */
    .block-container {
        padding: 1rem 0.5rem !important;
        max-width: 450px;
    }
    /* 버튼 디자인 */
    .stButton>button {
        width: 100%;
        height: 3.2em;
        font-weight: bold !important;
        border-radius: 12px;
        background-color: #4CAF50;
        color: white;
    }
    /* 세트 박스 디자인 */
    .bundle-card {
        background-color: white;
        border: 1px solid #ddd;
        border-radius: 12px;
        padding: 10px;
        margin-bottom: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    /* 조합 한 줄 레이아웃 */
    .lotto-row {
        display: flex;
        align-items: center;
        padding: 4px 0;
        border-bottom: 1px solid #f1f1f1;
    }
    .lotto-row:last-child { border-bottom: none; }
    
    .row-label {
        width: 35px;
        font-size: 0.75rem;
        color: #999;
        font-weight: bold;
        text-align: center;
    }
    .ball-list {
        display: flex;
        gap: 4px;
        margin-left: 5px;
    }
    .ball {
        width: 32px;
        height: 32px;
        line-height: 32px;
        border-radius: 50%;
        text-align: center;
        color: white;
        font-weight: bold;
        font-size: 14px;
        box-shadow: inset -2px -2px 3px rgba(0,0,0,0.2);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎰 행님 로또 명당")

# 3. 로직 (통계 기반 추출)
frequent_nums = [1, 10, 12, 13, 14, 17, 18, 21, 24, 26, 27, 33, 34, 39, 40, 43, 45]

def generate_five_sets():
    sets = []
    for _ in range(5):
        high = random.sample(frequent_nums, 3)
        others = [n for n in range(1, 46) if n not in high]
        low = random.sample(others, 3)
        sets.append(sorted(high + low))
    return sets

def get_color(n):
    if n <= 10: return "#fbc400" # 노랑
    if n <= 20: return "#69c8f2" # 파랑
    if n <= 30: return "#ff7272" # 빨강
    if n <= 40: return "#aaaaaa" # 회색
    return "#b0d840" # 초록

# 4. 세션 관리
if 'all_bundles' not in st.session_state:
    st.session_state.all_bundles = [generate_five_sets()]

# 5. 상단 버튼
c1, c2 = st.columns(2)
with c1:
    if st.button("🔄 새로고침"):
        st.session_state.all_bundles = [generate_five_sets()]
        st.rerun()
with c2:
    if st.button("➕ 5세트 추가"):
        st.session_state.all_bundles.append(generate_five_sets())

# 6. 결과 출력 (HTML을 하나의 변수에 통째로 담아 출력)
for b_idx, bundle in enumerate(st.session_state.all_bundles):
    # 세트 박스 시작
    full_html = f'<div class="bundle-card">'
    full_html += f'<div style="font-size:0.7rem; color:#bbb; margin-bottom:4px;">SET {b_idx + 1}</div>'
    
    for i, nums in enumerate(bundle):
        balls_html = "".join([
            f'<div class="ball" style="background-color:{get_color(n)}">{n}</div>' 
            for n in nums
        ])
        # 각 조합 줄 추가
        full_html += f'''
            <div class="lotto-row">
                <div class="row-label">#{i+1}</div>
                <div class="ball-list">{balls_html}</div>
            </div>
        '''
    
    full_html += '</div>' # 세트 박스 닫기
    
    # 세트 단위로 렌더링
    st.write(full_html, unsafe_allow_html=True)

st.divider()
st.caption("행님, 이번엔 진짜 제대로 나올 겁니다! 행운을 빕니다! 🚀")
