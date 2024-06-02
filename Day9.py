import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from vega_datasets import data

st.header('Line chart')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.header('Altair Chart')


chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

c = alt.Chart(chart_data).mark_circle().encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])


st.altair_chart(c, use_container_width=True)




source = data.cars()

chart = alt.Chart(source).mark_circle().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
).interactive()

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Altair native theme"])

with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.altair_chart(chart, theme="streamlit", use_container_width=True)
with tab2:
    # Use the native Altair theme.
    st.altair_chart(chart, theme=None, use_container_width=True)