import numpy as np
import csv
import os
from collections import defaultdict

FILENAME = "journal.csv"


# =========================
# FILE SETUP
# =========================
def initialize_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["date", "pair", "r", "emotion", "notes"])


# =========================
# DISPLAY / UI                                                  # =========================
def show_menu():
    print("\n===== TRADING JOURNAL =====")
    print("1. Add Trade")
    print("2. Analyze Journal")
    print("3. Exit")


def draw_equity_curve(equity):
    print("\n===== EQUITY CURVE =====")

    max_val = max(equity)
    min_val = min(equity)
    height = 10

    for level in range(height, -1, -1):
        threshold = min_val + (max_val - min_val) * level / height
        line = ""

        for val in equity:
            line += "█" if val >= threshold else " "

        print(line)


# =========================
# TRADE INPUT
# =========================
def add_trade():
    with open(FILENAME, "a", newline="") as f:
        writer = csv.writer(f)

        date = input("Date (YYYY-MM-DD): ")
        pair = input("Pair (BTCUSD/XAUUSD/etc): ")
        r = float(input("R Multiple: "))
        emotion = input("Emotion: ")
        notes = input("Notes: ")

        writer.writerow([date, pair, r, emotion, notes])

    print("✅ Trade saved successfully")


# =========================
# LOAD JOURNAL DATA
# =========================
def load_journal_data():
    R = []
    pairs = defaultdict(list)
    monthly = defaultdict(list)
    emotions = defaultdict(int)

    with open(FILENAME) as f:
        reader = csv.DictReader(f)

        for row in reader:
            r = float(row["r"])
            pair = row["pair"]
            month = row["date"][:7]
            emotion = row["emotion"]

            R.append(r)
            pairs[pair].append(r)
            monthly[month].append(r)
            emotions[emotion] += 1

    return np.array(R), pairs, monthly, emotions


# =========================
# CORE METRICS
# =========================
def calculate_metrics(R):
    wins = R[R > 0]
    losses = R[R < 0]

    metrics = {
        "total_trades": len(R),
        "winrate": (len(wins) / len(R) * 100) if len(R) else 0,
        "expectancy": R.mean() if len(R) else 0,
        "avg_win": wins.mean() if len(wins) else 0,
        "avg_loss": losses.mean() if len(losses) else 0,
        "profit_factor": wins.sum() / abs(losses.sum()) if len(losses) else 0,
        "std_dev": R.std() if len(R) else 0,
    }

    metrics["sharpe"] = (
        metrics["expectancy"] / metrics["std_dev"]
        if metrics["std_dev"] != 0 else 0
    )

    return metrics


# =========================
# RISK STATS
# =========================
def calculate_risk_stats(R):
    equity_curve = np.cumsum(R)

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

    return equity_curve, max_drawdown, max_loss_streak


# =========================
# REPORTS
# =========================
def show_pair_analysis(pairs):
    print("\n===== PAIR ANALYSIS =====")

    for pair, data in pairs.items():
        data = np.array(data)
        wins = data[data > 0]

        print(f"\n{pair}")
        print(f"Trades      : {len(data)}")
        print(f"Winrate     : {len(wins)/len(data)*100:.2f}%")
        print(f"Expectancy  : {data.mean():.2f}")
        print(f"Total R     : {data.sum():.2f}")
        print(f"Best Trade  : {data.max():.2f}")
        print(f"Worst Trade : {data.min():.2f}")


def show_monthly_report(monthly):
    print("\n===== MONTHLY REPORT =====")

    for month, data in monthly.items():
        print(f"{month}: {sum(data):.2f}R")


def show_emotion_analysis(emotions):
    print("\n===== EMOTION ANALYSIS =====")

    for emotion, count in emotions.items():
        print(f"{emotion}: {count} trades")


# =========================
# MAIN ANALYSIS
# =========================
def analyze_journal():
    R, pairs, monthly, emotions = load_journal_data()

    if len(R) == 0:
        print("❌ No trades found")
        return

    metrics = calculate_metrics(R)

    equity_curve, max_drawdown, max_loss_streak = calculate_risk_stats(R)

    draw_equity_curve(equity_curve)

    print("\n===== JOURNAL ANALYSIS =====")
    print(f"Total Trades     : {metrics['total_trades']}")
    print(f"Winrate          : {metrics['winrate']:.2f}%")
    print(f"Expectancy       : {metrics['expectancy']:.2f}")
    print(f"Avg Win          : {metrics['avg_win']:.2f}")
    print(f"Avg Loss         : {metrics['avg_loss']:.2f}")
    print(f"Profit Factor    : {metrics['profit_factor']:.2f}")
    print(f"Std Dev          : {metrics['std_dev']:.2f}")
    print(f"Sharpe Ratio     : {metrics['sharpe']:.2f}")
    print(f"Max Drawdown     : {max_drawdown:.2f}")
    print(f"Max Loss Streak  : {max_loss_streak}")

    show_pair_analysis(pairs)
    show_monthly_report(monthly)
    show_emotion_analysis(emotions)

    if metrics['winrate'] < 40:
        print("⚠️ Warning: Low winrate")

    if max_loss_streak >= 5:
        print("⚠️ Warning: Losing streak too high")


# =========================
# MAIN LOOP
# =========================
def main():
    initialize_file()

    while True:
        show_menu()

        choice = input("Choose (1/2/3): ")

        if choice == "1":
            add_trade()

        elif choice == "2":
            analyze_journal()

        elif choice == "3":
            print("👋 Good trading bro")
            break

        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main()
