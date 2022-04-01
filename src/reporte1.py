import streamlit as st
import pandas as pd
import numpy as np

st.title('Reporte: Data ')


@st.cache
def load_data(nrows):
    data  = pd.read_csv('./data/train.csv', nrows=nrows)
    data  = pd.read_csv('./data/test', nrows=nrows)
    
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)


st.subheader('XXX')
st.write(data)
