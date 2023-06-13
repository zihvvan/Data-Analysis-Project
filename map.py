# import folium
# from folium.plugins import FastMarkerCluster
# import pandas as pd
# import streamlit as st


# def main():
#     st.title('데이터 시각화 프로젝트')
#     st.subheader('서울특별시 전기차 충전소 위치🏁')
#     st.markdown("---")
#     # CSV 파일을 Pandas DataFrame으로 읽어들임
#     df3 = pd.read_csv("서울특별시 전기차 충전소.csv")

#     # 데이터프레임 출력
#     st.header("서울특별시 전기차 충전소.csv 📄")
#     st.dataframe(df3)
#     st.markdown("---")
#     st.header("서울특별시 전기차 충전소 지도 🗺")
#     # Create a map centered on Seoul
#     m = folium.Map(location=[37.566345, 126.977893], zoom_start=11)

#     # Add markers for each charging station using FastMarkerCluster
#     marker_cluster = FastMarkerCluster(data=list(zip(df3['lat'], df3['lon'])))
#     marker_cluster.add_to(m)

#     # Add popup to each marker
#     for idx, row in df3.iterrows():
#         popup = f"{row['stat_nm']}<br>{[row['addr']]}<br>{[row['charger_type']]}"
#         tooltip = row['stat_nm']
#         folium.Marker(
#             location=[row['lat'], row['lon']],
#             popup=popup,
#             tooltip=tooltip,
#         ).add_to(marker_cluster)

#     # Render map using Folium
#     folium_static(m)
#     st.markdown("---")





# if __name__ == "__main__":
#     main()


import folium
from folium.plugins import FastMarkerCluster
import pandas as pd
import streamlit as st


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

    # Add markers for each charging station using FastMarkerCluster
    marker_cluster = FastMarkerCluster(data=list(zip(df3['lat'], df3['lon'])))
    marker_cluster.add_to(m)

    # Add popup to each marker
    for idx, row in df3.iterrows():
        popup = f"{row['stat_nm']}<br>{[row['addr']]}<br>{[row['charger_type']]}"
        tooltip = row['stat_nm']
        folium.Marker(
            location=[row['lat'], row['lon']],
            popup=popup,
            tooltip=tooltip,
        ).add_to(marker_cluster)

    # Render map using Folium
    folium_static(m)
    st.markdown("---")

if __name__ == "__main__":
    main()

