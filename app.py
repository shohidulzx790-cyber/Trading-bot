import streamlit as st
import google.generativeai as genai
import random

st.set_page_config(page_title="Dragon AI Signal Bot", page_icon="🤖")

st.title("🤖 Dragon Chinese AI Signal Bot")
st.write("Real Market + OTC Signal Analysis")

broker = st.selectbox(
    "Select Broker",
    ["Quotex", "Pocket Option", "IQ Option"]
)

asset = st.selectbox(
    "Select Asset",
    [
        "EUR/USD",
        "GBP/USD",
        "USD/JPY",
        "GOLD",
        "BTC/USD",
        "EUR/USD OTC",
        "GBP/USD OTC"
    ]
)

timeframe = st.selectbox(
    "Select Timeframe",
    ["30 sec", "1 min", "5 min"]
)

if st.button("GENERATE SIGNAL"):

    signal = random.choice(["BUY", "SELL", "NO TRADE"])
    confidence = random.randint(75, 95)

    st.subheader("Signal Result")
    st.write("Broker:", broker)
    st.write("Asset:", asset)
    st.write("Timeframe:", timeframe)
    st.write("Signal:", signal)
    st.write("Confidence:", str(confidence) + "%")
