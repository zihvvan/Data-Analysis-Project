import streamlit as st
from streamlit.state.session_state import SessionState
from chart import main as chart_page
from map import main as map_page

def main():
    session = st.SessionState.get(page="chart", data=42) # create a session state

    if session.page == "chart":
        chart_page()
    elif session.page == "map":
        map_page()

if __name__ == "__main__":
    main()
