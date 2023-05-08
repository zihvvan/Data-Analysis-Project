import folium
import joblib
import streamlit as st
import pandas as pd

# CSV 파일을 Pandas DataFrame으로 읽어들임
df3 = pd.read_csv("서울특별시 전기차 충전소.csv")

# 데이터프레임 출력
st.dataframe(df3)

# def main():
#     # Load map in Streamlit
#     map_html = joblib.load("map.pkl")
#     st.markdown(map_html, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
