import folium
import joblib
import streamlit as st

# Create map
map = folium.Map(location=[37.566345, 126.977893], zoom_start=12, width='%100', height='%100')
locations = list(zip(df3.lat, df3.lon))
from folium import plugins
cluster = plugins.MarkerCluster(locations=locations, popups=df3["addr"].tolist())
map.add_child(cluster)

# Save map using joblib
joblib.dump(map._repr_html_(), "map.pkl")

# Load map in Streamlit
st.set_page_config(page_title="Map Viewer")
st.markdown("<h1 style='text-align: center;'>Seoul EV Charger Locations</h1>", unsafe_allow_html=True)
map_html = joblib.load("map.pkl")
st.markdown(map_html, unsafe_allow_html=True)
