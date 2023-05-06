import streamlit as st
import pickle
import matplotlib.pyplot as plt
from streamlit_folium import folium_static
import folium
import joblib

def draw_chart(root):
    with open(root, 'rb') as file:
        fig = pickle.load(file)
        if isinstance(fig, plt.Figure):
            st.pyplot(fig)
        elif isinstance(fig, folium.Map):
            folium_static(fig)
        else:
            st.warning("Unknown chart type")


st.title('서울특별시 데이터 시각화 (전기차/충전소) 프로젝트')

draw_chart("charger_graph.pkl")
draw_chart("charger_per_1000_graph.pkl")
draw_chart("graph.pickle")
draw_chart("seoul_electric_car_map.pickle")


