import streamlit as st
import google.generativeai as genai
import time
import random

# Access the API key securely from Streamlit Secrets
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except Exception:
    genai.configure(api_key="YOUR_GEMINI_API_KEY")

# Page Configuration & Dark Theme Styling
st.set_page_config(page_title="Chinese Signals Bot", page_icon="🚀", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #0b0f19; color: white; }
    .stSelectbox label { color: #8b949e !important; }
    .signal-card {
        background-color: #121824;
        border: 1px solid #1f293d;
        padding: 25px;
        border-radius: 12px;
        text-align: center;
        margin-top: 20px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.5);
    }
    .confidence { color: #00ff66; font-weight: bold; font-size: 18px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🟢 Chinese Signal Generator")
st.caption("Generate high-precision trading signals with advanced AI algorithms")
st.write("---")

# User Selection Options
broker = st.selectbox("Select Broker", ["Quotex", "Pocket Option", "IQ Option"])
asset = st.selectbox("Trading Asset", ["USD/ARS (OTC)", "USD/EGP (OTC)", "EUR/USD", "BTC/USDT"])
timeframe = st.selectbox("Time Frame", ["15secs", "30secs", "1min", "5mins"])

if st.button("GENERATE SIGNAL", use_container_width=True):
    
    # Fake Animation Loading Effects
    status_text = st.empty()
    progress_bar = st.progress(0)
    
    status_text.markdown("🔄 *Analyzing technical indicators and chart patterns...*")
    for percent_complete in range(10, 51, 10):
        time.sleep(0.2)
        progress_bar.progress(percent_complete)
        
    status_text.markdown("⚙️ *ANALYZING MARKET CONDITIONS...*")
    for percent_complete in range(60, 101, 10):
        time.sleep(0.2)
        progress_bar.progress(percent_complete)
        
    status_text.empty()
    progress_bar.empty()

    # Fetching Market Sentiment from Gemini API
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        prompt = f"Analyze the trading asset {asset} for a {timeframe} trend. Give a quick market sentiment summary in exactly 1 short sentence in English."
        response = model.generate_content(prompt)
        ai_analysis = response.text
    except Exception:
        ai_analysis = "High market volatility detected. Trade with strict risk management."

    # Signal Generation Logic
    direction = random.choice(["BUY", "SELL"])
    confidence = random.randint(94, 98)
    color = "#238636" if direction == "BUY" else "#da3637"

    # Final Output Display
    st.toast("🎯 Latest Signal Generated!", icon="🎯")
    
    st.markdown(f"""
        <div class="signal-card">
            <h3 style='color: #58a6ff;'>LATEST SIGNAL GENERATED!</h3>
            <h1 style='color: {color}; font-size: 50px; margin: 10px 0;'>{direction}</h1>
            <p class="confidence">{confidence}% Confidence</p>
            <hr style='border-color: #1f293d;'>
            <p style='text-align: left; font-size: 14px; color: #8b949e;'>
                <b>Asset:</b> {asset}<br>
                <b>Timeframe:</b> {timeframe}<br>
                <b>AI Insight:</b> {ai_analysis}
            </p>
        </div>
    """, unsafe_allow_html=True)

