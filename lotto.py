import streamlit as st
import random

# 1. 페이지 설정
st.set_page_config(page_title="행님 로또 명당", page_icon="🎰", layout="centered")

# 2. 스타일 설정 (공 디자인)
st.markdown("""
    <style>
    .main .block-container { padding: 1rem 0.5rem !important; max-width: 500px !important; }
    .stButton>button { width: 100%; border-radius: 12px; height: 3.5rem; font-weight: bold !important; }
    
    /* 로또 공 디자인 */
    .lotto-ball {
        display: inline-block;
        width: 38px; height: 38px; line-height: 38px;
        border-radius: 50%; text-align: center;
        color: white !important; font-weight: bold; font-size: 15px;
        margin: 3px;
        box-shadow: inset -2px -2px 4px rgba(0,0,0,0.2);
    }
    /* 세트 박스 */
    .bundle-card {
        border: 1px solid #e0e0e0; border-radius: 15px;
        padding: 15px 10px; margin-bottom: 20px;
        background-color: #ffffff; box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎰 행님 로또 명당")

# 3. 로또 번호 생성 로직 (1회~최신 최다 빈도 반영)
# 실제 통계상 자주 나오는 번호들에 가중치를 둡니다.
frequent_pool = [1, 10, 12, 13, 14, 17, 18, 21, 24, 26, 27, 33, 34, 39, 40, 43, 45]

def generate_lotto_bundle():
    bundle = []
    for _ in range(5):
        # 최다 빈도군에서 3개 + 나머지에서 3개 전략적 조합
        high_part = random.sample(frequent_pool, 3)
        others = [n for n in range(1, 46) if n not in high_part]
        low_part = random.sample(others, 3)
        bundle.append(sorted(high_part + low_part))
    return bundle

def get_ball_color(n):
    if n <= 10: return "#fbc400" # 노랑
    if n <= 20: return "#69c8f2" # 파랑
    if n <= 30: return "#ff7272" # 빨강
    if n <= 40: return "#aaaaaa" # 회색
    return "#b0d840" # 초록

# 4. 세션 관리
if 'all_data' not in st.session_state:
    st.session_state.all_data = [generate_lotto_bundle()]

# 5. 조작 버튼
col1, col2 = st.columns(2)
with col1:
    if st.button("🔄 전체 새로고침"):
        st.session_state.all_data = [generate_lotto_bundle()]
        st.rerun()
with col2:
    if st.button("➕ 5조합 세트 추가"):
        st.session_state.all_data.append(generate_lotto_bundle())

# 6. 결과 출력 (코드 노출 방지를 위해 단일 렌더링 사용)
for b_idx, bundle in enumerate(st.session_state.all_data):
    # 카드 전체를 하나의 큰 문자열로 미리 조립해서 한 번에 출력
    card_content = f'<div class="bundle-card">'
    card_content += f'<div style="font-size:0.8rem; color:#bbb; margin-bottom:10px; font-weight:bold;">SET {b_idx + 1}</div>'
    
    for i, nums in enumerate(bundle):
        balls_html = "".join([f'<div class="lotto-ball" style="background-color:{get_ball_color(n)}">{n}</div>' for n in nums])
        card_content += f'''
            <div style="display:flex; align-items:center; border-bottom:1px solid #f8f9fa; padding:5px 0;">
                <div style="width:35px; color:#ddd; font-size:12px; font-weight:bold;">#{i+1}</div>
                <div style="flex-grow:1; text-align:center;">{balls_html}</div>
            </div>
        '''
    card_content += '</div>'
    
    # st.markdown 하나로 카드 한 장을 통째로 그림
    st.markdown(card_content, unsafe_allow_html=True)

st.divider()
st.info("행님, 이제 조합도 확실히 나오고 프레임도 안 깨집니다! 1등 가즈아! 🚀")
