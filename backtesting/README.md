# 📊 Backtesting Engine

- Strategy simulation on historical data  
- Performance metrics calculation  
- Trade-by-trade analysis  
- Basic risk evaluation  

---

## 📌 Overview

Backtesting allows strategies to be tested against past market conditions to assess their performance, robustness, and risk profile before live deployment.

This module focuses on evaluating trading strategies using historical data.

---

## 🧠 Purpose

To validate trading ideas using data-driven methods and reduce the risk of deploying untested strategies.

---

## 📂 Files

• `backtest_engine.py` — core backtesting logic  
  - CSV-based OHLC data loader  
  - Manual trade input (Buy / Sell)  
  - Stop Loss & Take Profit logic  
  - Risk-based position sizing  
  - Winrate & PnL calculation  
  - CLI menu system (loop + exit)  

---

## 🚀 Future Improvements

- Multi-asset backtesting  
- Slippage and transaction cost modeling  
- Walk-forward analysis  
- Monte Carlo simulation
