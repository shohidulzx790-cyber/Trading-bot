

import streamlit as st
import google.generativeai as genai
import time
import random
import yfinance as yf
import pandas as pd

# Gemini API Configuration
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except:
    genai.configure(api_key="YOUR_GEMINI_API_KEY")

st.set_page_config(page_title="Pro-Level AI Trading", layout="centered")

# CSS Styling
st.markdown("""
    <style>
    .main { background-color: #050505; color: #fff; }
    .card { background: #121212; padding: 20px; border-radius: 15px; border: 1px solid #333; }
    .signal { font-size: 40px; font-weight: bold; text-align: center; }
    </style>
""", unsafe_allow_html=True)

st.title("🚀 Pro AI Trading Intelligence")

# Inputs
asset_mapping = {"EUR/USD": "EURUSD=X", "GBP/USD": "GBPUSD=X", "BTC/USDT": "BTC-USD", "ETH/USDT": "ETH-USD"}
asset = st.selectbox("Select Asset", list(asset_mapping.keys()))
timeframe = st.selectbox("Timeframe", ["1m", "5m", "15m"])

if st.button("RUN PRO ANALYSIS"):
    ticker = yf.Ticker(asset_mapping[asset])
    df = ticker.history(period="5d", interval=timeframe)
    
    # 1. RSI
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(14).mean()
    rsi = 100 - (100 / (1 + (gain / loss)))
    rsi_val = rsi.iloc[-1]
    
    # 2. MACD
    ema12 = df['Close'].ewm(span=12).mean()
    ema26 = df['Close'].ewm(span=26).mean()
    macd = ema12 - ema26
    macd_signal = macd.ewm(span=9).mean()
    
    # 3. Bollinger Bands
    sma20 = df['Close'].rolling(20).mean()
    std20 = df['Close'].rolling(20).std()
    upper_band = sma20 + (std20 * 2)
    lower_band = sma20 - (std20 * 2)
    
    # Logic Engine
    curr_price = df['Close'].iloc[-1]
    if rsi_val < 30 and macd.iloc[-1] > macd_signal.iloc[-1]:
        signal = "BUY"
    elif rsi_val > 70 and macd.iloc[-1] < macd_signal.iloc[-1]:
        signal = "SELL"
    else:
        signal = "WAIT/NEUTRAL"

    # Display
    st.markdown(f"""
    <div class="card">
        <div class="signal" style="color: {'#00ff00' if signal == 'BUY' else '#ff0000' if signal == 'SELL' else '#ffff00'}">{signal}</div>
        <p>RSI: {rsi_val:.2f}</p>
        <p>MACD Momentum: {'Bullish' if macd.iloc[-1] > macd_signal.iloc[-1] else 'Bearish'}</p>
        <p>Bollinger Condition: {'Near Lower Band' if curr_price < lower_band.iloc[-1] else 'Near Upper Band' if curr_price > upper_band.iloc[-1] else 'Stable'}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # AI Insight
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(f"Analyze this trading data: Asset={asset}, RSI={rsi_val}, MACD={macd.iloc[-1]}. Give a 1-sentence trading advice.")
    st.info(response.text)
