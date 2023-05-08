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
    st.dataframe(df3)
    
    st.dataframe(df3)
    st.markdown("---")
    # Create a map centered on Seoul
    m = folium.Map(location=[37.566345, 126.977893], zoom_start=11)

    # Add markers for each charging station using MarkerCluster
    marker_cluster = MarkerCluster().add_to(m)
    for i in range(len(df3)):
        lat = df3.loc[i, "위도"]
        lon = df3.loc[i, "경도"]
        folium.Marker([lat, lon]).add_to(marker_cluster)

    # Render map using Folium
    folium_static(m)

if __name__ == "__main__":
    main()


# def main():    
#     st.title('데이터 시각화 프로젝트')
#     st.subheader('서울특별시 전기차 충전소 위치🏁')
#     st.markdown("---")
#     # CSV 파일을 Pandas DataFrame으로 읽어들임
#     df3 = pd.read_csv("서울특별시 전기차 충전소.csv")

#     # 데이터프레임 출력
#     st.dataframe(df3)
#     st.markdown("---")
#     # Create a map centered on Seoul
#     m = folium.Map(location=[37.566345, 126.977893])

#     # Add markers for each charging station
#     for i in range(len(df3)):
#         lat = df3.loc[i, "lat"]
#         lon = df3.loc[i, "lon"]
#         folium.Marker([lat, lon]).add_to(m)

#     # Render map using Folium
#     folium_static(m)

# if __name__ == "__main__":
#     main()

