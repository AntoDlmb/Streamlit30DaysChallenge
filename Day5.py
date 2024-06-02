import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')
st.subheader('Essai des différentes solutions')
st.markdown('Ceci est un markdown')
st.caption('Ceci est une caption')
st.text('Ceci est du text')
st.latex('Ceci est du latex')
st.code('ceci est du code')
st.code('''import numpy as np
import streamlit as st
import altair''',line_numbers=True)

# Example 1

st.write('Hello, *World!* :sunglasses:')

# Example 2

st.write(1234)

# Example 3

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

# Example 4

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Example 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])

st.write(df2)
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)