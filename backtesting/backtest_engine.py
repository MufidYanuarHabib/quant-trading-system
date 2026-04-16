# =========================
# LOAD CSV SIMPLE (NO LIBRARY)
# =========================
def load_data(path):
    data = []

    with open(path, "r") as file:
        lines = file.readlines()

        for i in range(1, len(lines)):  # skip header
            row = lines[i].strip().split(",")

            data.append({
                "time": row[0],
                "open": float(row[1]),
                "high": float(row[2]),
                "low": float(row[3]),
                "close": float(row[4]),
                "volume": float(row[5])
            })

    return data


# =========================
# INPUT TRADE MANUAL
# =========================
def input_trades():
    trades = []
    n = int(input("How many trades?: "))

    for i in range(n):
        print(f"\nTrade {i+1}")
        t = input("Type (buy/sell): ").lower()
        entry = float(input("Entry: "))
        sl = float(input("SL: "))
        tp = float(input("TP: "))

        trades.append({
            "type": t,
            "entry": entry,
            "sl": sl,
            "tp": tp
        })

    return trades


# =========================
# BACKTEST ENGINE
# =========================
def backtest(data, trades):
    balance = 10000
    initial_balance = balance
    results = []

    for trade in trades:
        entry = trade["entry"]
        sl = trade["sl"]
        tp = trade["tp"]
        ttype = trade["type"]

        hit = None

        for c in data:
            high = c["high"]
            low = c["low"]

            if ttype == "buy":
                if low <= sl:
                    hit = "sl"
                    break
                if high >= tp:
                    hit = "tp"
                    break

            elif ttype == "sell":
                if high >= sl:
                    hit = "sl"
                    break
                if low <= tp:
                    hit = "tp"
                    break

        risk = balance * 0.01

        if hit == "tp":
            profit = risk * 2
            balance += profit
        elif hit == "sl":
            profit = -risk
            balance += profit
        else:
            profit = 0

        results.append({
            "type": ttype,
            "entry": entry,
            "sl": sl,
            "tp": tp,
            "result": hit,
            "profit": profit
        })

    return results, balance, initial_balance


# =========================
# ANALYZE
# =========================
def analyze(results, final, initial):
    wins = 0
    losses = 0

    for r in results:
        if r["result"] == "tp":
            wins += 1
        elif r["result"] == "sl":
            losses += 1

    total = len(results)
    winrate = (wins / total * 100) if total > 0 else 0

    print("\n===== RESULT =====")
    print(f"Final Balance : {final}")
    print(f"Profit        : {final - initial}")
    print(f"Trades        : {total}")
    print(f"Winrate       : {winrate:.2f}%")

    print("\n=== TRADE DETAILS ===")
    for r in results:
        print(r)


# =========================
# MAIN LOOP (MENU SYSTEM)
# =========================
def main():
    print("=== BACKTEST ENGINE ===")

    path = input("Enter data file (example: data.csv): ")
    data = load_data(path)

    while True:
        print("\n===== MENU =====")
        print("1. Manual trade input")
        print("2. Exit")

        choice = input("Select (1/2): ")

        if choice == "1":
            trades = input_trades()
            results, final, initial = backtest(data, trades)
            analyze(results, final, initial)

        elif choice == "2":
            print("Exiting engine... 👋")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
