print("=" * 30)
print("    RISK MANAGEMENT")
print("=" * 30)
print()

while True:
  balance = input("Balance ('EXIT' for break the system): ")
  if balance.upper()  == "EXIT":
    print("See You!")
    break
  balance = float(balance)

  risk = float(input("Risk: "))
  rr = float(input("RR: "))
  tipe_entry = input("Tipe Entry (BUY/SELL): ").upper()
  entry = float(input("Entry: "))
  stop_loss = float(input("Price for stop loss: "))

  #risk management
  risk_amount = balance * (risk / 100)
  sl_distance = entry - stop_loss
  lot = risk / sl_distance
  reward = sl_distance * rr

  #tipe entry
  if tipe_entry == "BUY":
    tp = entry + reward
  else:
    tp = entry - reward

  print()
  print("-" * 30)
  print(f"{'Balance':<12}: {balance:.2f}")
  print(f"{'Risk Amount':<12}: {risk_amount:.2f}")
  print(f"{'Lot Size':<12}: {lot:.2f}")
  print(f"{'RR':<12}: {rr:.2f}")
  print(f"{'Tipe Entry':<12}: {tipe_entry}")
  print(f"{'Take Profit':<12}: {tp:.2f}")
  print("-" * 30)
  print()
