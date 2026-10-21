print("=== WIN RATE CALCULATOR ===")

wins = float(input("Enter number of winning trades: "))
losses = float(input("Enter number of losing trades: "))   
total_trades = wins + losses

if wins == 0:
  print("Error: Number of trades cannot be negative.")

elif losses == 0:
  print("No trades available to calculate win rate.")


else:
    win_rate = (wins / total_trades) * 100

    print("\n=== RESULTS ===")
    print(f"Total Trades    : {total_trades}")
    print(f"Winning Trades  : {wins}")
    print(f"Losing Trades   : {losses}")
    print(f"Win Rate        : {win_rate:.2f}%")
