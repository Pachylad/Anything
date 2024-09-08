# Import Libraries
import streamlit as st
import pandas as pd


# Set Page configuration
# Read more at [docs.streamlit.io URL]

add_selectbox = st.sidebar.selectbox(
    'Artist',
    ('AB', 'Homphsne', 'Cobile phone')