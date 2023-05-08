import folium
from folium.plugins import MarkerCluster
import pandas as pd
import streamlit as st
from streamlit_folium import folium_static

def main():
    st.title('데이터 시각화 프로젝트')
    st.subheader('서울특별시 전기차 충전소 위치🏁')
    st.markdown("---")
    # CSV 파일을 Pandas DataFrame으로 읽어들임
    df3 = pd.read_csv("서울특별시 전기차 충전소.csv")

    # 데이터프레임 출력
    st.header("서울특별시 전기차 충전소.csv 📄")
    st.dataframe(df3)
    st.markdown("---")
    st.header("서울특별시 전기차 충전소 지도 🗺")
    # Create a map centered on Seoul
    m = folium.Map(location=[37.566345, 126.977893], zoom_start=11)

    # Add markers for each charging station using MarkerCluster
    marker_cluster = MarkerCluster().add_to(m)
    for i in range(len(df3)):
        lat = df3.loc[i, "lat"]
        lon = df3.loc[i, "lon"]
        name = df3.loc[i, "stat_nm"]
        address = df3.loc[i, "addr"]
        charger = df3.loc[i, "charger_type"]
        folium.Marker([lat, lon], tooltip=name, popup=f"{name}<br>{address}<br>{charger}").add_to(m)

    # Render map using Folium
    folium_static(m)
    st.markdown("---")

if __name__ == "__main__":
    main()

