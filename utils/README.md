# 📁 utils/

## 📖 Dictionary

This folder contains a collection of utility tools (helper functions) designed to support a quantitative trading system.

The tools inside this folder are not the main trading strategies. Instead, they provide supporting functionality such as risk management, position sizing, indicators, signal filtering, validation, and statistical analysis tools.

The main purpose of this folder is to make the system more modular, organized, reusable, and easier to develop.

---

# 🧰 Tools

## 🧠 math_helper_v2.py

A lightweight Python command-line tool for basic statistical and financial data analysis.

This tool processes numerical input (space-separated values) and generates key statistical metrics for quick data analysis.

**Main Features:**
- Mean calculation
- Median calculation
- Variance calculation
- Standard deviation calculation
- Log return calculation
- Z-score normalization
- Mode calculation
- Range calculation
- Minimum value detection
- Maximum value detection

---

## 🧠 risk_management_v1.py

A basic risk management utility designed to calculate risk parameters for a trading system.

**Main Features:**
- Fixed risk percentage calculation
- Risk amount calculation
- Stop loss distance calculation
- Position sizing calculation
- Reward distance calculation
- Take profit calculation
- BUY / SELL support

---

## 📊 position_size_trade_spot_v1.py

A position size calculator for spot trading without leverage.

This tool helps determine the appropriate position size based on account balance, risk per trade, entry price, and stop loss level to maintain controlled risk exposure.

**Main Features:**
- Account balance input
- Fixed risk percentage
- Entry price and stop loss input
- Risk amount calculation
- Risk per unit calculation
- Position size calculation
- Capital requirement calculation
- BUY / SELL support
- Input validation
- Insufficient balance warning
- Spot trading focused (no leverage)

---

# 🎯 Objectives

- Separate trading strategies from utility functions
- Build a modular and structured trading system
- Create reusable tools for different strategies
- Improve maintainability and scalability
- Support future quantitative trading development
