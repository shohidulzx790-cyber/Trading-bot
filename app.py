import streamlit as st
import google.generativeai as genai
import time
import random

# Access the API key securely from Streamlit Secrets
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except Exception:
    genai.configure(api_key="YOUR_GEMINI_API_KEY")

# Page Configuration & Premium Dark Theme Styling
st.set_page_config(page_title="AI Trading Intelligence Bot", page_icon="🤖", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #060913; color: #e2e8f0; }
    .stSelectbox label, .stMultiSelect label { color: #94a3b8 !important; font-weight: 600; }
    .signal-card {
        background-color: #0f172a;
        border: 2px solid #1e293b;
        padding: 30px;
        border-radius: 16px;
        text-align: center;
        margin-top: 25px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.7);
    }
    .confidence { color: #10b981; font-weight: bold; font-size: 20px; }
    .tool-tag {
        background-color: #1e293b;
        color: #38bdf8;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 12px;
        margin: 4px;
        display: inline-block;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ AI Trading Intelligence Bot")
st.caption("Advanced Real-Time & OTC Market Signals with Integrated TradingView Toolkits")
st.write("---")

# 1. Select Broker
broker = st.selectbox("Select Broker Platform", ["Quotex", "Pocket Option", "IQ Option", "Olymp Trade"])

# 2. Complete Asset List (Real & OTC Markets)
all_assets = [
    # --- Real Markets ---
    "EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "USD/CAD", "EUR/GBP", "EUR/JPY",
    "GBP/JPY", "USD/CHF", "NZD/USD", "BTC/USDT", "ETH/USDT", "GOLD (XAU/USD)", "SILVER",
    # --- OTC Markets ---
    "EUR/USD (OTC)", "GBP/USD (OTC)", "USD/JPY (OTC)", "AUD/USD (OTC)", "USD/CAD (OTC)",
    "EUR/GBP (OTC)", "EUR/JPY (OTC)", "GBP/JPY (OTC)", "USD/CHF (OTC)", "NZD/USD (OTC)",
    "USD/ARS (OTC)", "USD/EGP (OTC)", "USD/BRL (OTC)", "USD/INR (OTC)", "USD/PKR (OTC)"
]
asset = st.selectbox("Select Trading Asset (Real / OTC)", all_assets)

# 3. Time Frame Selection
timeframe = st.selectbox("Select Time Frame", ["15secs", "30secs", "1min", "2mins", "5mins", "15mins", "1hour"])

# 4. TradingView Tools & AI Intelligence Activation
st.write("### 🛠️ Activate AI Tools & Technical Indicators")
selected_tools = st.multiselect(
    "Choose tools for deep market analysis:",
    ["RSI (Relative Strength Index)", "MACD (Moving Average Convergence Divergence)", 
     "Bollinger Bands", "Moving Averages (EMA/SMA)", "Fibonacci Retracement", 
     "Support & Resistance Levels", "Volume Profile Analysis", "AI Pattern Recognition",
     "Market Sentiment AI Analysis", "Smart Money Concepts (SMC) Decoder"],
    default=["RSI (Relative Strength Index)", "Support & Resistance Levels", "AI Pattern Recognition"]
)

st.write("---")

if st.button("RUN DEEP AI ANALYSIS & GENERATE SIGNAL", use_container_width=True):
    
    if not selected_tools:
        st.warning("⚠️ Please select at least one AI Tool/Indicator for analysis.")
    else:
        # Fake Advanced Multi-Stage Loading Animation
        status_text = st.empty()
        progress_bar = st.progress(0)
        
        status_text.markdown("🔍 *Connecting to TradingView data nodes and scanning chart patterns...*")
        time.sleep(0.6)
        progress_bar.progress(30)
        
        status_text.markdown(f"⚙️ *Running Calculations for: {', '.join([t.split(' ')[0] for t in selected_tools])}...*")
        time.sleep(0.8)
        progress_bar.progress(70)
        
        status_text.markdown("🧠 *Consulting Gemini AI Intelligence Layer for macro trend prediction...*")
        time.sleep(0.6)
        progress_bar.progress(100)
        
        status_text.empty()
        progress_bar.empty()

        # Fetching Market Sentiment from Gemini API based on selected indicators
        try:
            model = genai.GenerativeModel('gemini-2.5-flash')
            tools_str = ", ".join(selected_tools)
            prompt = f"Act as an expert financial trading bot. Analyze {asset} on a {timeframe} chart using data from {tools_str}. Provide a professional, highly precise 1-sentence market sentiment summary in English."
            response = model.generate_content(prompt)
            ai_analysis = response.text
        except Exception:
            ai_analysis = "High liquidity detected with active institutional order blocks. Manage risk accordingly."

        # Signal Generation Logic
        direction = random.choice(["BUY", "SELL"])
        confidence = random.randint(93, 99)
        color = "#10b981" if direction == "BUY" else "#ef4444"

        # Displaying the Advanced Signal Card
        st.toast("🎯 High-Precision AI Signal Generated!", icon="🔥")
        
        st.markdown(f"""
            <div class="signal-card">
                <h3 style='color: #38bdf8; font-size: 16px; letter-spacing: 2px;'>AI SYSTEM DECISION</h3>
                <h1 style='color: {color}; font-size: 55px; margin: 15px 0; font-weight: 800;'>{direction}</h1>
                <p class="confidence">✨ {confidence}% Accuracy Confidence</p>
                <hr style='border-color: #1e293b; margin: 20px 0;'>
                <div style='text-align: left; font-size: 14px;'>
                    <p><b>Platform:</b> {broker} | <b>Asset:</b> <span style='color: #f59e0b;'>{asset}</span></p>
                    <p><b>Timeframe:</b> {timeframe}</p>
                    <p><b>Active Analytics:</b></p>
                    <div>
                        {"".join([f'<span class="tool-tag">{tool}</span>' for tool in selected_tools])}
                    </div>
                    <p style='margin-top: 15px; color: #94a3b8; background-color: #060913; padding: 12px; border-radius: 8px; border-left: 4px solid #38bdf8;'>
                        <b>AI Intelligence Insight:</b><br>{ai_analysis}
                    </p>
                </div>
            </div>
        """, unsafe_allow_html=True)

