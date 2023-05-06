import streamlit as st
from PIL import Image
from streamlit_folium import folium_static
import folium
import joblib

def main():
    st.title('데이터 시각화 프로젝트')
    st.subheader('서울특별시 전기차/충전기 데이터분석')
    st.markdown("---")
    # 지자체별 전기차 충전기(급속/완속) 갯수
    st.header('지자체별 전기차 충전기(급속/완속) 갯수')
    image = Image.open('charger_graph.png')
    st.image(image, caption='지자체별 전기차 충전기(급속/완속) 갯수', use_column_width=True)
    st.markdown("---")
    # 지자체별 전기차 1,000대당 충전기 갯수
    st.header('지자체별 전기차 1,000대당 충전기 갯수')
    image = Image.open('charger_per_1000_graph.png')
    st.image(image, caption='지자체별 전기차 1,000대당 충전기 갯수', use_column_width=True)
    st.markdown("---")
    # 서울특별시 연도별 전기차 등록대수(사업용/비사업용)
    st.header('서울특별시 연도별 전기차 등록대수')
    st.subheader('(사업용/비사업용)')
    image = Image.open('graph.png')
    st.image(image, caption='서울특별시 연도별 전기차 등록대수(사업용/비사업)', use_column_width=True)
    st.markdown("---")
    map_html = joblib.load("map.pkl")

if __name__ == '__main__':
    main()
