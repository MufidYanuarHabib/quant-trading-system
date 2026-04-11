import numpy as np
import csv
import os

def draw_equity_curve(equity):
        print("\===== EQUITY CURVE =====")

        max_val = max(equity)
        min_val = min(equity)

        height = 10

        for level in range(height, -1, -1):
                threshold = min_val + (max_val - min_val) * level / height
                line = ""

                for val in euqity:
                        if val >= threshold:
                                line += "█"
                        else:
                                line += ""

                print(line)

FILENAME = "journal.csv"

# =========================
# CREATE FILE IF NOT EXISTS
# =========================
if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "pair", "r"])

# =========================
# MAIN LOOP
# =========================
while True:

    print("\n===== TRADING JOURNAL =====")
    print("1. Add Trade")
    print("2. Analyze Journal")
    print("3. Exit")

    choice = input("Choose (1/2/3): ")

    # =========================
    # ADD TRADE
    # =========================
    if choice == "1":
        with open(FILENAME, "a", newline="") as f:
            writer = csv.writer(f)

            date = input("Date (YYYY-MM-DD): ")
            pair = input("Pair (XAUUSD, GBPUSD, BTCUSD): ")
            r = float(input("R multiple: "))

            writer.writerow([date, pair, r])

        print("Trade saved successfully ✅")

    # =========================
    # ANALYZE
    # =========================
    elif choice == "2":
        R = []
        pairs = {}

        with open(FILENAME) as f:
            reader = csv.DictReader(f)
            for row in reader:
                r = float(row["r"])
                pair = row["pair"]

                R.append(r)
                if pair not in pairs:
                        pairs[pair] = []
                pairs[pair].append(r)

        if len(R) == 0:
            print("No trades found.")
            continue

        R = np.array(R)

        total_trades = len(R)
        wins = R[R > 0]
        losses = R[R < 0]

        winrate = len(wins) / total_trades * 100
        avg_win = wins.mean() if len(wins) > 0 else 0
        avg_loss = losses.mean() if len(losses) > 0 else 0
        expectancy = R.mean()
        profit_factor = wins.sum() / abs(losses.sum()) if len(losses) > 0 else 0
        std_R = R.std()
        sharpe = expectancy / std.R if std_R != 0 else 0

        equity_curve = np.cumsum(R)
        if len (equity_curve) >1:
                draw_equity_curve(equity_curve):
        print(f"Start Equity : {equity_curve[0]:.2f}")
        print(f"End Equity   : {equity_curve[-1]:.2f}")
        peak = np.maximum.accumulate(equity_curve)
        drawdown = equity_curve - peak
        max_drawdown = drawdown.min()

        loss_streak = 0
        max_loss_streak = 0
        for r in R:
            if r < 0:
                loss_streak += 1
                max_loss_streak = max(max_loss_streak, loss_streak)
            else:
                loss_streak = 0

        print("\n===== JOURNAL ANALYSIS =====")
        print(f"Total trades      : {total_trades}")
        print(f"Winrate           : {winrate:.2f}%")
        print(f"Expectancy (R)    : {expectancy:.2f}")
        print(f"Avg Win (R)       : {avg_win:.2f}")
        print(f"Avg Loss (R)      : {avg_loss:.2f}")
        print(f"Profit Factor     : {profit_factor:.2f}")
        print(f"Max Drawdown (R)  : {max_drawdown:.2f}")
        print(f"Max Loss Streak   : {max_loss_streak}")
        print(f"Std Dev (R)       : {std_R:.2f}")
        print(f"Sharpe Ratio      : {sharpe:.2f}")

        print("\n===== PAIR ANALYSIS =====")
                for pair, data in pairs.items():
                        data = np.array(data)
                        print(f"\n{pair}")
                        print(f"Trades      : {len(data)}")
                        print(f"Expectancy  : {data.mean():.2f}")

        if winrate < 40:
                print("⚠️ WARNING: Winrate low. Review strategy.")

        if max_loss_streak >= 5:
                print("⚠️ WARNING: Losing streak tinggi. Stop trading dulu.")

    # =========================
    # EXIT
    # =========================
    elif choice == "3":
        print("Good trading bro 😎📊")
        break

    else:
        print("Invalid choice.")
