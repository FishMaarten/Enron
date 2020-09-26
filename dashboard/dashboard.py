import streamlit as st

import numpy as np
import pandas as pd
import datetime

DATA_URL = ('./data/reduced_mails_FINAL.csv')
@st.cache
def load_data():
    df = pd.read_csv(DATA_URL, nrows=5000)
    df['Date'] = pd.to_datetime(df['Date'],utc=True)
    df = df.set_index(pd.DatetimeIndex(df['Date']))
    return df

SENTIMENT_URL = ('./data/emotional_content.csv')
@st.cache
def load_sentiment():
    dfs = pd.read_csv(SENTIMENT_URL, nrows=5000)
    dfs['Date'] = pd.to_datetime(dfs['Date'],utc=True)
    dfs = dfs.set_index(pd.DatetimeIndex(dfs['Date']))
    return dfs

def main():

    pages={
        'Company communications': page_first,
        'Employee communications': page_second,
        'Employee churn analytics':page_third,
        'Social networks': page_fourth,
        'Fraud analytics': page_fifth,
        }

    st.sidebar.title('Views')

    page = st.sidebar.radio('Select view', tuple(pages.keys()))

    pages[page]()

def page_first():
    st.title('Company communications dashboard')

    #import data
#    @st.cache
#    def load_data():


 #       return df

 #   data_load_state = st.text('Loading data...')
 #   data = load_data(10000)
 #   data_load_state.text("Done! (using st.cache)")

    #Make a date selector
    df = load_data()
    dfs = load_sentiment()
    selecteddate = st.date_input("Select date range", [df.index.min(), df.index.max()])

    #Resample email traffic by day
    chart_data = df.resample('D').size()

    #Plot email traffic
    st.line_chart(chart_data)

    #Plot sentiment
    st.subheader('Sentiment Trends')
    chart_data_sentiment = dfs.resample('D').size()
    st.line_chart(chart_data_sentiment)

#can also use st.dataframe() and st.table()

def page_second():
    st.title('Employee communications dashboard')
    df = load_data()
    employee = st.selectbox("Select employee", df["From"].unique())


def page_third():
    st.title('Employee Churn Analytics')
    st.subheader('A subheader here')

def page_fourth():
    st.title('Social networks')
    df = load_data()
    employee = st.selectbox("Select employee", df["From"].unique())


def page_fifth():
    st.title('Fraud Analytics')
    st.subheader('A subheader here')

if __name__ == '__main__':
    main()
