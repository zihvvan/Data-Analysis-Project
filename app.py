import streamlit as st
import pickle
import matplotlib as plt
import folium


def draw_chart(root):
    with open(root, 'rb') as file:
       fig = pickle.load(file)
       fig.show()
        

    
st.title(' 서울특별시 데이터 시각화 (전기차/충전소) 프로젝트')

draw_chart("barchart.pickle")
draw_chart("barchart2.pickle")
draw_chart("barchart3.pickle")
draw_chart("mapchart.pickle")


    

    
