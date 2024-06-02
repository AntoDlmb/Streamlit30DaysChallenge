import streamlit as st

st.header('Select box')

fav_color = st.selectbox('What is your favorite color ?',('Blue','Green','Yellow','Red','Purple','Orange'))

st.write('Your favourite color is ',fav_color)