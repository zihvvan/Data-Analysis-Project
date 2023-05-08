import folium
import joblib
import streamlit as st
import pandas as pd


def main():
    # CSV 파일을 Pandas DataFrame으로 읽어들임
    df3 = pd.read_csv("서울특별시 전기차 충전소.csv")

    # 데이터프레임 출력
    st.dataframe(df3)

    # Create a map centered on Seoul
    m = folium.Map(location=[37.566345, 126.977893])

    # Add markers for each charging station
    for i in range(len(df3)):
        lat = df3.loc[i, "위도"]
        lon = df3.loc[i, "경도"]
        name = df3.loc[i, "충전소명"]
        address = df3.loc[i, "주소"]
        charger = df3.loc[i, "충전기타입(명)"]
        folium.Marker([lat, lon], tooltip=name, popup=f"{name}<br>{address}<br>{charger}").add_to(m)

    # Render map using Folium
    folium_static(m)

if __name__ == "__main__":
    main()

# # CSV 파일을 Pandas DataFrame으로 읽어들임
# df3 = pd.read_csv("서울특별시 전기차 충전소.csv")

# # 데이터프레임 출력
# st.dataframe(df3)

# # def main():
# #     # Load map in Streamlit
# #     map_html = joblib.load("map.pkl")
# #     st.markdown(map_html, unsafe_allow_html=True)

# if __name__ == "__main__":
#     main()
