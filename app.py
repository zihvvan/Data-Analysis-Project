import streamlit as st
from streamlit.state.session_state import SessionState
from chart import main as chart_page
from map import main as map_page

def main():
    session = SessionState.get(page="chart", data=42) # create a session state

    if session.page == "chart":
        home_page(session)
    elif session.page == "map":
        dashboard_page(session)

if __name__ == "__main__":
    main()
