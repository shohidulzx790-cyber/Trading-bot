Build a powerful AI forex signal tool for REAL MARKET trading (not OTC).
Supported pairs:
EURUSD, GBPUSD, USDJPY, AUDUSD, USDCAD, USDCHF, EURJPY, GBPJPY

Timeframes:
1 Minute and 5 Minutes

Main Goal:
Generate highly accurate BUY / SELL / WAIT signals using AI analysis, support/resistance, trend, candle pressure, and spike detection.

Core Indicators:
1. Supertrend
- ATR Period: 10
- Factor: 3
- Green = Buy Trend
- Red = Sell Trend

2. UT Bot Alerts
- Key Value: 1
- ATR Period: 10

3. EMA
- EMA 9
- EMA 21
- EMA 200

4. RSI
- Length: 14
- Above 70 = Overbought
- Below 30 = Oversold

5. MACD
- Fast: 12
- Slow: 26
- Signal: 9

AI Candle Pressure Analysis:
Analyze last 3–5 candles.
Check:
- Candle body size
- Upper wick
- Lower wick
- Bullish/Bearish engulfing
- Momentum strength

Rules:
Buyer Pressure Strong if:
- 3 bullish candles
- Large green body
- Lower wick rejection

Seller Pressure Strong if:
- 3 bearish candles
- Large red body
- Upper wick rejection

Support / Resistance Detector:
Automatically detect:
- Last 50 candle highest zone = Resistance
- Last 50 candle lowest zone = Support
- Mark zones visually

Spike Detector:
If candle body > average of previous 5 candle × 1.8
Then mark:
SPIKE BUY or SPIKE SELL

Signal Logic:

STRONG BUY:
All conditions:
- Supertrend Green
- UT Bot Buy
- EMA 9 > EMA 21 > EMA 200
- RSI between 35 and 65
- MACD Bullish
- Price bounced from Support
- Buyer pressure > Seller pressure
- No sideways market

Output:
STRONG BUY 🚀
Confidence Score %
Entry Now / Wait Pullback
Expiry 1m or 5m

STRONG SELL:
All conditions:
- Supertrend Red
- UT Bot Sell
- EMA 9 < EMA 21 < EMA 200
- RSI between 35 and 65
- MACD Bearish
- Price rejected from Resistance
- Seller pressure > Buyer pressure
- No sideways market

Output:
STRONG SELL 🔻
Confidence Score %
Entry Now / Wait Pullback
Expiry 1m or 5m

Weak Conditions:
Output:
WAIT ⏳
NO TRADE ZONE

Extra Features:
- Early Signal before candle close
- Confirmation Signal after candle close
- Pullback Entry Detection
- Trend Strength Meter (0–100)
- AI Market Status:
Trending / Sideways / Volatile

UI Design:
Dark theme
Green BUY button
Red SELL button
Large signal display
Live chart
Support/Resistance zones visible
Real-time signal updates

Accuracy Goal:
Target 90%+ high quality signals for real forex market
Avoid false signals in sideways market
