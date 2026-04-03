import streamlit as st
import pandas as pd
import yfinance as yf

st.set_page_config(layout="wide")

st.title("📊 Portfolio Dashboard")

# =====================
# YOUR PORTFOLIO
# =====================
portfolio = {
    "MSFT": 3,
    "META": 2,
    "V": 3,
    "GOOGL": 2,
    "SPGI": 3,
    "MCO": 3,
    "GE": 7,
    "AIR.PA": 7,
    "SAF.PA": 5,
    "DG.PA": 10,
    "PM": 5,
    "T": 10,
    "VZ": 10,
    "CCJ": 8,
    "Z": 22,
    "FLUT": 5,
    "FWONA": 9,
    "LNW": 6,
    "RPRX": 12
}

tickers = list(portfolio.keys())

# =====================
# GET LIVE PRICES
# =====================
data = yf.download(tickers, period="1d", interval="1m")["Close"].iloc[-1]

# =====================
# BUILD DATAFRAME
# =====================
df = pd.DataFrame({
    "Ticker": tickers,
    "Shares": [portfolio[t] for t in tickers],
    "Price": [data[t] for t in tickers]
})

df["Value"] = df["Shares"] * df["Price"]

total_value = df["Value"].sum()

# =====================
# DISPLAY
# =====================
st.metric("Portfolio Value", f"£{total_value:,.0f}")

st.dataframe(df)

st.subheader("Allocation")
st.bar_chart(df.set_index("Ticker")["Value"])
