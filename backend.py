# Premium Flask Backend for Fein Trade
import os
import random
import math
from datetime import datetime, timedelta
from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__, static_folder=".")

# Ensure correct files are served when running backend
@app.route("/")
def serve_index():
    return send_from_directory(".", "index.html")

@app.route("/style.css")
def serve_css():
    return send_from_directory(".", "style.css")

@app.route("/script.js")
def serve_js():
    return send_from_directory(".", "script.js")

# Endpoint: Financial News Aggregator with AI Sentiment Tagging
@app.route("/api/news", methods=["GET"])
def get_market_news():
    news_pool = [
        {
            "title": "NYSE and NASDAQ experience heavy institutional volume ahead of consumer spending reports",
            "source": "Wall Street Journal",
            "sentiment": "BULLISH",
            "score": "82%",
            "summary": "Major investment houses are loading long equities, betting on stable consumer performance metrics. Technical supports remain extremely firm."
        },
        {
            "title": "Crypto Liquidation cascades brief Bitcoin drop to $65,500 level",
            "source": "CoinDesk",
            "sentiment": "BEARISH",
            "score": "68%",
            "summary": "Highly leveraged margin accounts experienced heavy liquidations as BTC hit minor local resistances, though buyers immediately stepped in to absorb supply."
        },
        {
            "title": "Federal Reserve Chairman hints at possible structural quantitative easing",
            "source": "Bloomberg Markets",
            "sentiment": "BULLISH",
            "score": "76%",
            "summary": "Recent inflation indicators are cooling faster than forecasted, prompting discussions about upcoming interest rate reductions by late Q3."
        },
        {
            "title": "Euro slides to 3-month lows following European Central Bank inflation downgrades",
            "source": "Reuters Business",
            "sentiment": "BEARISH",
            "score": "75%",
            "summary": "ECB officials state consumer spending indices require quantitative support, increasing likelihoods for multiple consecutive rate cuts."
        },
        {
            "title": "NEPSE Index gains 35 points in standard breakout on heavy utility volume",
            "source": "Kathmandu Post",
            "sentiment": "BULLISH",
            "score": "88%",
            "summary": "Hydroelectricity and Commercial Bank indices led Nepalese markets to high volumes as regulatory boards ease credit constraints."
        }
    ]
    # Add minor timestamp jitter
    for news in news_pool:
        news["time"] = f"{random.randint(5, 55)} minutes ago"
    
    return jsonify(news_pool)

# Endpoint: AI-driven Predictive ML Models (LSTM/ARIMA Mock)
@app.route("/api/predictions/<symbol>", methods=["GET"])
def get_prediction_trajectory(symbol):
    symbol = symbol.upper()
    
    # Generate historical and projected pricing data points using sinusoidal mathematical algorithms
    random.seed(hash(symbol)) # Deterministic for same symbol
    
    base_price = random.uniform(50.0, 500.0)
    if "USD" in symbol:
        base_price = random.uniform(100.0, 65000.0) if "BTC" in symbol or "ETH" in symbol else random.uniform(0.5, 2.0)
        
    days = 15
    historical = []
    forecast = []
    
    current_time = datetime.now()
    
    # Historical curve (last 10 days)
    for i in range(10, 0, -1):
        dt = current_time - timedelta(days=i)
        trend = math.sin(i * 0.4) * (base_price * 0.05)
        noise = random.uniform(-base_price * 0.01, base_price * 0.01)
        historical.append({
            "date": dt.strftime("%Y-%m-%d"),
            "price": round(base_price + trend + noise, 4)
        })
        
    # Projected curve (next 5 days) using simulated ML LSTM output
    last_hist_price = historical[-1]["price"]
    ml_confidence = random.randint(70, 95)
    direction = "BULLISH" if random.random() > 0.4 else "BEARISH"
    coef = 0.025 if direction == "BULLISH" else -0.02
    
    for i in range(1, 6):
        dt = current_time + timedelta(days=i)
        ml_prediction = last_hist_price * (1 + (coef * i) + random.uniform(-0.01, 0.01))
        forecast.append({
            "date": dt.strftime("%Y-%m-%d"),
            "price": round(ml_prediction, 4),
            "confidence_upper": round(ml_prediction * 1.05, 4),
            "confidence_lower": round(ml_prediction * 0.95, 4)
        })
        
    return jsonify({
        "symbol": symbol,
        "indicator": direction,
        "confidence": f"{ml_confidence}%",
        "historical": historical,
        "forecast": forecast
    })

# Endpoint: AI Trading Assistant Chatbot API
@app.route("/api/chat", methods=["POST"])
def post_chat_query():
    data = request.get_json() or {}
    query = data.get("query", "").strip()
    if not query:
        return jsonify({"reply": "Fein Core received empty terminal payload. Please specify a financial query."})
        
    upper = query.toUpperCase() if hasattr(query, 'toUpperCase') else query.upper()
    
    # Advanced responsive templates
    if "TSLA" in upper or "TESLA" in upper:
        reply = (
            "<strong>[Fein Server Analysis - TSLA]</strong><br>"
            "Tesla exhibits highly volatile MACD waves. Immediate supports have formed near $180, "
            "whereas resistance bands are firmly cap-staged at $188. Technical parameters suggest accumulating "
            "long shares on breakouts past $184 with strict stops set below $178."
        )
    elif "AAPL" in upper or "APPLE" in upper:
        reply = (
            "<strong>[Fein Server Analysis - AAPL]</strong><br>"
            "Apple consolidates tightly around its 50-day EMA support ($174.50). Orderbook depth indicates "
            "institutional accumulation patterns. Breakout structures above $176.50 confirm targets toward "
            "historical resistance levels near $182. Risk profile remains highly favorable."
        )
    elif "BTC" in upper or "BITCOIN" in upper:
        reply = (
            "<strong>[Fein Server Analysis - BTCUSD]</strong><br>"
            "Bitcoin holds crucial long-term supports at the $66,800 cluster. Volume profiles are thin, "
            "confirming consolidation ahead of major breakout expansions. Close above $68,200 sets targets "
            "toward fresh local highs at $71,500. Maintain defensive risk allocations."
        )
    else:
        reply = (
            "<strong>[Fein Quantitative Assistant]</strong><br>"
            "Your query has been indexed. General technical market conditions indicate constructive accumulation "
            "for top equities, while crypto markets are digesting recent high-leverage expansions. For detailed risk "
            "mitigation, we highly recommend utilizing the built-in position sizing calculator on your terminal!"
        )
        
    return jsonify({"reply": reply})

if __name__ == "__main__":
    print("-" * 60)
    print("      FEIN TRADE TERMINAL SERVER ACTIVE ON PORT 5000")
    print("      Navigate to: http://127.0.0.1:5000 in your browser")
    print("-" * 60)
    app.run(host="127.0.0.1", port=5000, debug=True)
