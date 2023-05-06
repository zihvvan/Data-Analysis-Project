import folium
import joblib
import streamlit as st


def main():
    # Load map in Streamlit
    map_html = joblib.load("map.pkl")
    st.markdown(map_html, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
