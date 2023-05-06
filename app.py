import streamlit as st
from chart import main as chart_page
from map import main as map_page

def main():
    st.set_page_config(page_title="Data Analysis Project")

    tabs = ["Chart", "Map"]

    # Set page to display based on tab selection
    page = st.sidebar.selectbox("Select a page", tabs)

    if page == "Chart":
        chart_page()
    elif page == "Map":
        map_page()

if __name__ == "__main__":
    main()
