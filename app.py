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

    # Show the appropriate page based on the user's menu choice
    if choice == "Homepage":
        st.header("Data Analysis Project")
        st.subheader("서울특별시 전기차/충전기 데이터분석")
        st.write("김지환")
        st.markdown("---")
        seoul_img = Image.open("seoul.png")
        st.image(seoul_img, use_column_width=True)
        car_img = Image.open("car.png")
        st.image(car_img, use_column_width=True)
        

    elif choice == "Chart":
        chart_page()

    elif choice == "Map":
        map_page()

if __name__ == "__main__":
    main()
