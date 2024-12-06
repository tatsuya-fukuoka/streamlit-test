import pandas as pd
import streamlit as st

st.title('Hello, Streamlit!')

df = pd.DataFrame({
    '名前': ['Alice', 'Bob', 'Charlie'],
    'スコア': [85, 90, 78]
})

st.write("学生のスコア")
st.dataframe(df)