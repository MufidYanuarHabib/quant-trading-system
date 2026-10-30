
def get_trade_count(message):
    while True:
        try:
            count = int(input(message))

            if count < 0:
                print("Error: Trade counts cannot be negative.")
                continue

            return count

        except ValueError:
            print("Error: Please enter whole numbers only.")


def calculate_results(wins, losses, breakeven):
    total_trades = wins + losses + breakeven

    if total_trades == 0:
        print("\nNo trades available to calculate results!")
        return

    win_rate = (wins / total_trades) * 100
    loss_rate = (losses / total_trades) * 100
    breakeven_rate = (breakeven / total_trades) * 100

    print("\n" + "=" * 35)
    print("         TRADING RESULTS")
    print("=" * 35)

    print(f"Total Trades       : {total_trades}")
    print(f"Winning Trades     : {wins}")
    print(f"Losing Trades      : {losses}")
    print(f"Breakeven Trades   : {breakeven}")

    print("-" * 35)

    print(f"Win Rate           : {win_rate:.2f}%")
    print(f"Loss Rate          : {loss_rate:.2f}%")
    print(f"Breakeven Rate     : {breakeven_rate:.2f}%")

    print("=" * 35)


def main():
    print("=== WIN RATE CALCULATOR V3 ===")

    while True:
        wins = get_trade_count(
            "Enter number of winning trades: "
        )

        losses = get_trade_count(
            "Enter number of losing trades: "
        )

        breakeven = get_trade_count(
            "Enter number of breakeven trades: "
        )

        calculate_results(wins, losses, breakeven)

        while True:
            again = input(
                "\nCalculate again? (yes/no): "
            ).strip().lower()

            if again in ("yes", "y"):
                break

            elif again in ("no", "n"):
                print(
                    "\nThank you for using "
                    "Win Rate Calculator V3!"
                )
                return

            else:
                print("Please enter yes or no.")


if __name__ == "__main__":
    main()
