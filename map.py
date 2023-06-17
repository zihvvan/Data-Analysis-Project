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

import pandas as pd
import folium
from folium.plugins import FastMarkerCluster
import streamlit as st

# 데이터 예시 (실제 데이터에서 이 부분을 수정해 주세요)
data = {'lat': [37, 37.5], 'lon': [126, 126.5], 'stat_nm': ['A', 'B'],
    'addr': ['Address A', 'Address B'], 'charger_type': ['Type A', 'Type B']}
df3 = pd.DataFrame(data)

# 지도 만들기
def render_map(df    map = folium.Map(location=[37.566345, 126.977893], zoom_start=12, width='100%', height='100%')

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

streamlit_map = render_map(df3)

# 지도를 streamlit에 표시
st.title(" 지도 ")
folium_static(streamlit_map)

if __name__ == "__main__":
    main()



















