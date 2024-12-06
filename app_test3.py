import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
 
st.title('Hello, Streamlit!')
 
# データの作成
data = np.random.randn(100, 3)
df = pd.DataFrame(data, columns=['A', 'B', 'C'])
 
# チャートの作成
st.line_chart(df)