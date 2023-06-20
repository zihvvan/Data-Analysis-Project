import streamlit as st
from PIL import Image
import pandas as pd

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
    st.markdown("---")
    
    # 이미지와 연결할 링크 주소
    image_path = "car_map.png"
    link_url = "https://colab.research.google.com/drive/1DW3oz7BdlPjTF86qCej086zlBkL9JjzU?usp=sharing"

    # 이미지를 streamlit에 추가합니다.
    image = open("car_map.png", "rb")
    st.image(image, use_column_width=True)

    # 이미지를 클릭할 때 링크로 연결합니다.
    if st.button("Click to Open Link"):
        js = f"window.open('{link_url}')"
        html = '<img src onerror="{}">'.format(js)
        div = '<div>{}</div>'.format(html)
        st.markdown(div, unsafe_allow_html=True)
if __name__ == "__main__":
    main()


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

#     # FastMarkerCluster를 사용하여 각 충전소에 마커 추가
#     marker_cluster = FastMarkerCluster(data=list(zip(df3['lat'], df3['lon'])))
#     marker_cluster.add_to(m)

#     # 각 마커에 팝업 추가
#     for idx, row in df3.iterrows():
#         popup = f"{row['stat_nm']}<br>{[row['addr']]}<br>{[row['charger_type']]}"
#         tooltip = row['stat_nm']
#         folium.Marker(
#             location=[row['lat'], row['lon']],
#             popup=popup,
#             tooltip=tooltip,
#         ).add_to(marker_cluster)

#     # Folium을 사용하여 지도 렌더링
#     folium_static(m)
#     st.markdown("---")

# if __name__ == "__main__":
#     main()























