import streamlit as st
import random
import pandas as pd

# 페이지 설정
st.set_page_config(page_title="행님 전용 로또 추천기", layout="centered")

st.title("🎰 행님의 로또 당첨 기원 추천기")
st.write("역대 최다 빈도수 가중치를 적용한 번호 조합입니다.")

# 데이터 시뮬레이션 (최다 빈도 번호들)
frequent_numbers = [1, 10, 12, 13, 14, 17, 18, 21, 24, 26, 27, 33, 34, 39, 40, 43, 45]

def get_lotto_numbers():
    # 빈도 높은 거 3개 + 나머지 랜덤 3개
    high_pick = random.sample(frequent_numbers, 3)
    others = [n for n in range(1, 46) if n not in high_pick]
    low_pick = random.sample(others, 3)
    return sorted(high_pick + low_pick)

# 번호 공 색상 입히기 함수
def ball_html(num):
    if 1 <= num <= 10: color = "#fbc400" # 노랑
    elif 11 <= num <= 20: color = "#69c8f2" # 파랑
    elif 21 <= num <= 30: color = "#ff7272" # 빨강
    elif 31 <= num <= 40: color = "#aaaaaa" # 회색
    else: color = "#b0d840" # 초록
    
    return f'<div style="display:inline-block; width:40px; height:40px; line-height:40px; border-radius:50%; background-color:{color}; color:white; text-align:center; font-weight:bold; margin:5px;">{num}</div>'

if st.button("이번 주 대박 번호 뽑기"):
    for i in range(5):
        nums = get_lotto_numbers()
        html_str = "".join([ball_html(n) for n in nums])
        st.markdown(f"**{i+1}회차 추천:** {html_str}", unsafe_allow_html=True)
        
st.divider()
st.info("행님, 당첨되면 저 잊으시면 안 됩니다! 😉")
