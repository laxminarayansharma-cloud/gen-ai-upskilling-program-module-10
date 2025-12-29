import streamlit as st
import yfinance as yf
from transformers import pipeline

menu = st.sidebar.radio("Select Option", ["Stock Chart", "Text Summarizer"])

if menu == "Stock Chart":
    st.title("Stock Price Dashboard")

    # Sidebar for user input
    ticker = st.sidebar.text_input('Enter Stock Ticker')
    period = st.sidebar.selectbox('Period', ['1d', '5d', '1mo', '6mo', '1y', '5y', 'max'], index=4)
    interval = st.sidebar.selectbox('Interval', ['1m', '5m', '15m', '1h', '1d', '1wk', '1mo'], index=4)

    if ticker:
        # Fetch data
        data = yf.download(ticker, period=period, interval=interval)
        if not data.empty:
            st.write(f"Displaying data for {ticker}")
            st.line_chart(data['Close'])
            # fig = go.Figure(data=[go.Candlestick(
            #     x=data.index,
            #     open=data['Open'],
            #     high=data['High'],
            #     low=data['Low'],
            #     close=data['Close']
            # )])
            # st.plotly_chart(fig)
        else:
            st.warning("No data found for the selected ticker and period.")


elif menu == "Text Summarizer":
    st.header("Text Summarizer")
    text = st.text_area("Enter stock-related text", height=200)
    if st.button("Summarize"):
        with st.spinner("Summarizing... Please wait."):
            summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
            summary = summarizer(text, max_length=80, min_length=25, do_sample=False)
        st.success(summary[0]['summary_text'])




        #         # with st.spinner("Summarizing..."):