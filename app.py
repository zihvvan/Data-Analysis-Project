import streamlit as st
import pickle
import matplotlib
# import pandas as pd
# import plotly.express as px

# 데이터 로드
# @st.cache
# def load_data():
    # df1 = pd.read_csv('/content/전기차 등록대수.csv')
    # df1 = df1.set_index('구분')

    # df2 = pd.read_csv('/content/전기차 충전소.csv')
    # df2 = df2.set_index('구분')

    # df3 = pd.read_csv('/content/서울특별시 전기차 충전소.csv')

    # result = pd.concat([df1, df2], axis=1)

    # result["2017년"] = result["2017.12.31(사업용)"] + result["2017.12.31(비사업용)"]
    # result["2018년"] = result["2018.12.31(사업용)"] + result["2018.12.31(비사업용)"]
    # result["2019년"] = result["2019.12.31(사업용)"] + result["2019.12.31(비사업용)"]
    # result["2020년"] = result["2020.12.31(사업용)"] + result["2020.12.31(비사업용)"]
    # result["2021년"] = result["2021.12.31(사업용)"] + result["2021.12.31(비사업용)"]
    # result["2022년"] = result["2022.12.31(사업용)"] + result["2022.12.31(비사업용)"]

    # result = result.drop(result.columns[0:12], axis=1)

def draw_chart(root):
    with open(root, 'rb') as file:
       fig = pickle.load(file)

    
st.title(' 서울특별시 데이터 시각화 (전기차/충전소) 프로젝트')

draw_chart("barchart.pickle")
draw_chart("barchart2.pickle")
draw_chart("barchart3.pickle")
draw_chart("mapchart.pickle")

    

    
