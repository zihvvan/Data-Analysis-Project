import streamlit as st
from chart import main as chart_page
from map import main as map_page
from PIL import Image


# Set page configuration
st.set_page_config(page_title="Data Analysis Project")

def main():
    # Create a menu with options to select different pages
    menu = ["Homepage", "Chart", "Map"]
    choice = st.sidebar.selectbox("Select a page", menu)
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"<div align=center><h1>📚 Reference </h1></div>", unsafe_allow_html=True)
    st.sidebar.markdown(":point_down:")
    st.sidebar.markdown("[![Git](https://img.shields.io/badge/git-444444?style=for-the-badge&logo=git)](https://github.com/zihvvan/DataAnalysis-Project)")
    st.sidebar.markdown("[![Colab](https://img.shields.io/badge/Colab-444444?style=for-the-badge&logo=Colab)](https://colab.research.google.com/drive/1TTRjmK7EoQomnjUe4Ec85ItlrhjJ3WK4?usp=sharing)")
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"<div align=center><h1>🖥 Tech Stack </h1></div>", unsafe_allow_html=True)
    st.sidebar.markdown("[![Python](https://img.shields.io/badge/Python-#3776AB?style=flat-square&logo=Python&logoColor=white)]")
    st.sidebar.markdown("[![Git](https://img.shields.io/badge/git-444444?style=for-the-badge&logo=git)]")
    st.sidebar.markdown("[![Git](https://img.shields.io/badge/git-444444?style=for-the-badge&logo=git)]")
    st.sidebar.markdown("[![Git](https://img.shields.io/badge/git-444444?style=for-the-badge&logo=git)]")
    
    
    # Show the appropriate page based on the user's menu choice
    if choice == "Homepage":
        st.header("Data Analysis Project👨‍💼")
        st.subheader("서울특별시 전기차/충전기 데이터분석⚡🚘")
        st.write("**김지환**")
        st.write("전기차와 충전소의 수는 최근 몇 년 간 급격히 증가하고 있습니다.\n"
          "서울시는 2025년까지 20만 대 이상의 전기차 보급을 목표로 하고 있으며, 이를 위해 전기차와 충전소의 수를 늘리고 있습니다.\n"
          "이에 따라 전기차와 충전소의 사용 현황을 파악하고 이를 분석하여 보다 효율적인 전기차 보급 및 충전 시스템을 구축할 수 있는 방안을 모색하고자 하였습니다.")
        st.markdown("---")
        seoul_img = Image.open("seoul.png")
        st.image(seoul_img, use_column_width=True, caption='서울특별시')
        st.markdown("---")
        car_img = Image.open("car.png")
        st.image(car_img, use_column_width=True, caption='전기차/충전기')
        st.markdown("---")

    elif choice == "Chart":
        chart_page()

    elif choice == "Map":
        map_page()
        

if __name__ == "__main__":
    main()
