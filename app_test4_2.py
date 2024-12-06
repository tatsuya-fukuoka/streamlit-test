import streamlit as st
 
st.title('Hello, Streamlit!')
 
if 'count' not in st.session_state:
    st.write('変数を設定')
    st.session_state['count'] = 0
 
if st.button('push me'):
    st.write('ボタンを押しました')
    st.session_state.count += 1
    # st.session_state['count'] += 1 でもOK
 
st.write('count = ', st.session_state.count)