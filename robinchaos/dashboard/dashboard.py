import streamlit as st

import numpy as np
import pandas as pd

st.title('Email dashboard')
st.write(pd.DataFrame({
    'first column': [ 1,2,3,4],
    'second column': [10,20, 30, 40]
}))

#can also use st.dataframe() and st.table()

#Add a chart
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
