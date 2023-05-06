import streamlit as st
from PIL import Image
from streamlit_folium import folium_static
import folium
import joblib

def main():
    st.title('서울특별시 데이터 시각화 (전기차/충전소) 프로젝트')
    
    # 전기차 등록 대수 그래프
    st.header('전기차 등록 대수 그래프')
    image = Image.open('charger_graph.png')
    st.image(image, caption='전기차 등록 대수 그래프', use_column_width=True)
    
    # 전기차 1000대당 충전소 개수 그래프
    st.header('전기차 1000대당 충전소 개수 그래프')
    image = Image.open('charger_per_1000_graph.png')
    st.image(image, caption='전기차 1000대당 충전소 개수 그래프', use_column_width=True)
    
    # 전기차 등록 대수와 충전소 개수 지도
    st.header('전기차 등록 대수와 충전소 개수 지도')
    map = joblib.load('seoul_electric_car_map.joblib')
    folium_static(map)
    
    # 기타 그래프
    st.header('기타 그래프')
    image = Image.open('graph.png')
    st.image(image, caption='기타 그래프', use_column_width=True)

if __name__ == '__main__':
    main()
