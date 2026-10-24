print("=== WIN RATE CALCULATOR V2 ===")

while True:
    try:
        wins = int(input("Enter number of winning trades: "))
        losses = int(input("Enter number of losing trades: "))

        if wins < 0 or losses < 0:
            print("Error: Trade counts cannot be negative.")
            continue

        total_trades = wins + losses

        if total_trades == 0:
            print("No trades available to calculate win rate!")

        else:
            win_rate = (wins / total_trades) * 100
            loss_rate = (losses / total_trades) * 100

            print("\n=== TRADING RESULTS ===")
            print(f"Total Trades    : {total_trades}")
            print(f"Winning Trades  : {wins}")
            print(f"Losing Trades   : {losses}")
            print(f"Win Rate        : {win_rate:.2f}%")
            print(f"Loss Rate       : {loss_rate:.2f}%")

    except ValueError:
        print("Error: Please enter whole numbers only.")

    again = input("\nCalculate again? (yes/no): ").strip().lower()

    if again not in ("yes", "y"):
        print("Thank you for using Win Rate Calculator V2!")
        break
