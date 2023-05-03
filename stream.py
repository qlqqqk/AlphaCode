import streamlit as st
import pandas as pd
from bit_search import *

st.title('''
         Bithumb Data Analysis
         ''')

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
df,utc = price_df()
st.text(f'{utc.tm_year}/{utc.tm_mon}/{utc.tm_mday} {utc.tm_hour}시 {utc.tm_min}분 {utc.tm_sec}초 UTC 기준')
st.dataframe(df)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')