import streamlit as st
import numpy as np
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium

df=pd.read_excel('data/평점 4이상 맛집리스트.xlsx',index_col=0)
