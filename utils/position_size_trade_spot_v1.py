print("===== POSITION SIZE CALCULATOR TRADE SPOT =====")
print("Notes: ")
print("Use prices in the chart or market for entry and stop loss.")
print("Designed for spot trade (no leverage).")
print("-" * 30)
print()

balance = 0

while True:
  balance_input = input("Input balance ('exit' for stop system): ")
  if balance_input.upper() == "EXIT":
    print("See you next time")
    break

  balance = float(balance_input)

  risk = float(input("Risk per trade: "))
  type_entry = input("Type entry BUY or SELL: ")
  price_entry = float(input("Input entry: "))
  stop_loss = float(input("Input stop loss: "))
  if type_entry.upper() == "BUY":
    risk_per_unit = abs( price_entry - stop_loss)
  else:
    risk_per_unit = abs( stop_loss - price_entry)
  if risk_per_unit == 0:
    print("Entry and stop los can't be same")
    continue

  risk_amount = balance * (risk / 100)
  position_size = risk_amount / risk_per_unit
  total_capital_needed = position_size * price_entry
  warning = total_capital_needed > balance
  if warning:
    print("\nWARNING: Capital Needed exceeds Account Balance")

  print()
  print("-" * 30)
  print("===== RESULTS =====")
  print("-" * 30)
  print(f"{'Balance':<15}: {balance:.2f}")
  print(f"{'Risk (%)':<15}: {risk:.2f} %")
  print(f"{'Type Entry':<15}: {type_entry}")
  print(f"{'Price entry':<15}: {price_entry:.2f}")
  print(f"{'Stop loss':<15}: {stop_loss:.2f}")
  print(f"{'Risk Amount':<15}: {risk_amount:.2f}")
  print(f"{'Risk/Unit':<15}: {risk_per_unit:.2f}")
  print(f"{'Position Size':<15}: {position_size:.2f}")
  print(f"{'Capital needed':<15}: {total_capital_needed:.2f}")
  print("-" * 30)
