# import streamlit as st
# from streamlit_folium import folium_static
# import pandas as pd
# import folium
# from folium.plugins import FastMarkerCluster


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

import streamlit as st
import folium
from folium.plugins import FastMarkerCluster
import pandas as pd
import io
import base64

def create_map(df):
    # 지도 생성
    map = folium.Map(location=[37.566345, 126.977893], zoom_start=12)

    # FastMarkerCluster 추가
    cluster = FastMarkerCluster(data=list(zip(df['lat'], df['lon'])))
    map.add_child(cluster)

    # 각 마커에 팝업 추가
    for idx, row in df.iterrows():
        popup = f"<b>{row['stat_nm']}</b><br>[주소: {row['addr']}]<br>[충전 종류: {row['charger_type']}]"
        tooltip = row['stat_nm']
        folium.Marker(
            location=[row['lat'], row['lon']],
            popup=popup,
            tooltip=tooltip,
        ).add_to(cluster)

    return map

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

    # Folium 지도 생성
    my_map = create_map(df3)

    # Folium 지도를 HTML로 변환
    map_html = my_map.get_root().render()

    # HTML을 바이너리 데이터로 변환하여 다운로드 링크 생성
    b64 = base64.b64encode(map_html.encode()).decode()
    html = f'<img src="data:image/png;base64,{b64}" width="100%" height="100%">'
    st.markdown(html, unsafe_allow_html=True)

if __name__ == "__main__":
    main()




















