📁 utils/

📖 Dictionary

This folder contains a collection of utility tools (helper functions) designed to support a quantitative trading system.

These tools are not the main trading strategies. Instead, they provide supporting functionality such as risk management, position sizing, indicators, signal filtering, validation, and statistical analysis.

The main purpose of this folder is to make the system more modular, organized, reusable, and easier to develop.

---

🧰 Tools

1. "math_helper_v2.py"

A lightweight Python command-line tool for basic statistical and financial data analysis.

This tool processes numerical input (space-separated values) and generates key statistical metrics for quick data analysis.

Main Features:

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

2. "risk_management_v1.py"

A basic risk management utility designed to calculate risk parameters for a trading system.

Main Features:

- Fixed risk percentage calculation
- Risk amount calculation
- Stop loss distance calculation
- Position sizing calculation
- Reward distance calculation
- Take profit calculation
- BUY/SELL support

---

3. "position_size_trade_spot_v1.py"

A position size calculator for spot trading without leverage.

This tool helps determine the appropriate position size based on account balance, risk per trade, entry price, and stop loss level to maintain controlled risk exposure.

Main Features:

- Account balance input
- Fixed risk percentage
- Entry price and stop loss input
- Risk amount calculation
- Risk per unit calculation
- Position size calculation
- Capital requirement calculation
- BUY/SELL support
- Input validation
- Insufficient balance warning
- Spot trading focus (no leverage)

---

4. "risk_reward_v3.py"

A Python command-line tool for calculating the risk-to-reward ratio and theoretical breakeven win rate based on entry price, stop loss, and take profit.

Main Features:

- Entry price, stop loss, and take profit input
- BUY/SELL selection and price validation
- Risk distance calculation
- Reward distance calculation
- Risk-to-reward ratio calculation
- Breakeven win rate calculation
- Zero-risk and zero-reward validation
- Position validation
- Input validation
- Modular function structure
- Interactive menu
- Repeated calculations without restarting
- Exit command
- Verified calculations
- Formatted output

---

5. "win_rate_v2.py"

A win rate calculator for trading strategies.

This tool measures the percentage of winning trades relative to the total number of completed trades to evaluate trading performance.

Main Features:

- Winning trades input
- Losing trades input
- Total trades calculation
- Win rate percentage calculation
- Input validation
- Formatted results display
- Input validation for negative trade counts
- Error handling for invalid inputs
- Win rate and loss rate calculations
- Zero-trade handling
- Repeat calculation functionality

---

🎯 Objectives

- Separate trading strategies from utility functions
- Build a modular and structured trading system
- Create reusable tools for different strategies
- Improve maintainability and scalability
- Support future quantitative trading development
