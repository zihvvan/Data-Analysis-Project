import streamlit as st
from PIL import Image
from streamlit_folium import folium_static
import folium
import joblib

def main():
    st.header('서울특별시 데이터 시각화')
    st.subheader('(전기차/충전소) 프로젝트')
    
    # 지자체별 전기차 충전기(급속/완속) 갯수
    st.header('지자체별 전기차 충전기(급속/완속) 갯수')
    image = Image.open('charger_graph.png')
    st.image(image, caption='지자체별 전기차 충전기(급속/완속) 갯수', use_column_width=True)
    
    # 지자체별 전기차 1,000대당 충전기 갯수
    st.header('지자체별 전기차 1,000대당 충전기 갯수')
    image = Image.open('charger_per_1000_graph.png')
    st.image(image, caption='지자체별 전기차 1,000대당 충전기 갯수', use_column_width=True)
    
    # 서울특별시 연도별 전기차 등록대수(사업자/비사업자)
    st.header('서울특별시 연도별 전기차 등록대수(사업자/비사업자)')
    image = Image.open('graph.png')
    st.image(image, caption='서울특별시 연도별 전기차 등록대수(사업자/비사업자)', use_column_width=True)
    
    # 서울특별시 전기차 충전기 위치 및 개수
    st.header('전기차 등록 대수와 충전소 개수 지도')
    map = joblib.load('seoul_electric_car_map.joblib')
    folium_static(map)

if __name__ == '__main__':
    main()
