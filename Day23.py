import streamlit as st

st.title('st.query_params')

with st.expander('About this app'):
  st.write("`st.query_params` allows the retrieval of query parameters directly from the URL of the user's browser.")

# 1. Instructions
st.header('1. Instructions')
st.markdown('''
In the above URL bar of your internet browser, append the following:
`?firstname=Jack&surname=Beanstalk`
after the base URL `http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/`
such that it becomes 
`http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/?firstname=Jack&surname=Beanstalk`
''')


# 2. Contents of st.experimental_get_query_params
st.header('2. Type of st.query_params')
st.write('type(st.query_params) : just so you know it s a dictionnary')
st.write(len(st.query_params))

# 3. Retrieving and displaying information from the URL
st.header('3. Retrieving and displaying information from the URL')

firstname = st.query_params['firstname']
surname = st.query_params['surname']

st.write(f'Hello **{firstname} {surname}**, how are you?')

clear = st.button('Clear params')

if clear:
  st.query_params.clear()