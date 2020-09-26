import streamlit as st

import numpy as np
import pandas as pd
import datetime

def main():

    pages={
        'Company communications': page_first,
	'Employee communications': page_second,
        'Fraud analytics': page_third,
	}

    st.sidebar.title('Views')

    page = st.sidebar.radio('Select view', tuple(pages.keys()))

    pages[page]()

def page_first():
    st.title('Company communications dashboard')

    #import data
#    @st.cache
#    def load_data():

    #Read csv from ./data folder
    pathtodata='./data/reduced_mails_FINAL.csv'
    df = pd.read_csv(pathtodata, nrows=5000)
        #convert columns to datetime
    df['Date'] = pd.to_datetime(df['Date'],utc=True)
    df = df.set_index(pd.DatetimeIndex(df['Date']))
 #       return df

 #   data_load_state = st.text('Loading data...')
 #   data = load_data(10000)
 #   data_load_state.text("Done! (using st.cache)")

    #Make a date selector
    selecteddate = st.date_input("Select date range", [df.index.min(), df.index.max()])

    #Resample email traffic by day
    chart_data = df.resample('D').size()

    #Plot email traffic
    st.line_chart(chart_data)

    st.subheader('A subheader for something else')

#can also use st.dataframe() and st.table()

def page_second():
    st.subheader('A subheader here')

def page_third():
    st.subheader('A subheader here')

if __name__ == '__main__':
    main()
