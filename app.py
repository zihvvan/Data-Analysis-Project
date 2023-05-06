import streamlit as st
import joblib
import matplotlib.pyplot as plt
from streamlit_folium import folium_static
import folium

# 나눔 폰트 설치
!sudo apt-get install -y fonts-nanum
!sudo fc-cache -fv
!rm ~/.cache/matplotlib -rf

# matplotlib에서 한글폰트 사용을 위한 설정
plt.rc('font', family='NanumBarunGothic') 

# streamlit에서 한글폰트 사용을 위한 설정
st.set_option('deprecation.showPyplotGlobalUse', False)

def draw_chart(root):
    with open(root, 'rb') as file:
        fig = joblib.load(file)
        if isinstance(fig, plt.Figure):
            st.pyplot(fig)
        elif isinstance(fig, folium.Map):
            folium_static(fig)
        else:
            st.warning("Unknown chart type")
            
st.set_option('deprecation.showfileUploaderEncoding', False) # streamlit 0.84.0 버전 이후 업로드 파일명 인코딩 에러 대처


st.title('서울특별시 데이터 시각화 (전기차/충전소) 프로젝트')

draw_chart("charger_graph.joblib")
draw_chart("charger_per_1000_graph.joblib")
draw_chart("graph.joblib")
draw_chart("seoul_electric_car_map.joblib")
