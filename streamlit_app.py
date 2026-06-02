import streamlit as st

# 앱 제목
st.title("🎬 영화관 세트메뉴 조합기")

popcorn_options = ["기본", "카라멜", "어니언"]
drink_options = ["생수", "탄산음료"]

st.subheader("선택 가능한 모든 세트메뉴 목록")

# 기존 for문을 활용한 화면 출력
for popcorn in popcorn_options:
    for drink in drink_options:
        # st.write를 사용하면 웹 화면에 텍스트가 출력됩니다.
        st.write(f"🍿 세트메뉴: **{popcorn} 팝콘** + 🥤 **{drink}**")