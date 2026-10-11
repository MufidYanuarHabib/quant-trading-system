print("=" * 30)
print("     RISK REWARD TOOL")
print("=" * 30)
print()

while True:
  entry = input("Price entry / EXIT: ")

  if entry.upper() == "EXIT":
    print("See you!")
    break

  entry = float(entry)
  sl = float(input("Price stop loss: "))
  tp = float(input("Price take profit: "))

  risk = abs(entry - sl)
  reward = abs(tp - entry)

  if risk == 0:
    print("Error: Entry and SL can't be equal!")
    print()
    continue

  if reward == 0:
    print("Error: Entry and TP can't be equal!")
    print()
    continue

  rr = reward / risk
  breakeven = risk / (risk + reward) * 100

  print()
  print("-" * 30)
  print(f"Entry Price        : {entry}")
  print(f"Risk Distance      : {risk}")
  print(f"Reward Distance    : {reward}")
  print(f"Risk Reward        : 1 : {rr:.2f}")
  print(f"Breakeven Win Rate : {breakeven:.2f}%")
  print("-" * 30)
  print()
