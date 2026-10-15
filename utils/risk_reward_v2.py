def get_price(prompt):
    while True:
        try:
            price = float(input(prompt))

            if price <= 0:
                print("Price must be greater than 0!")
                continue

            return price

        except ValueError:
            print("Invalid number! Try again")


def calculate_risk_reward():
    print("\nSelect Position Type")
    print("1. BUY")
    print("2. SELL")

    while True:
        position = input("Choose (1/2): ").strip()

        if position in ("1", "2"):
            break

        print("Error: Choose 1 or 2!")

    entry = get_price("Entry price: ")
    stop_loss = get_price("Stop Loss: ")
    take_profit = get_price("Take Profit: ")

    if position == "1":
        position_name = "BUY"

        if not (stop_loss < entry < take_profit):
            print("Error: BUY requires SL < Entry < TP!")
            return

    elif position == "2":
        position_name = "SELL"

        if not (take_profit < entry < stop_loss):
            print("Error: SELL requires TP < Entry < SL!")
            return

    risk = abs(entry - stop_loss)
    reward = abs(take_profit - entry)

    rr = reward / risk
    breakeven = risk / (risk + reward) * 100

    print("\n" + "=" * 35)
    print("       RISK REWARD TOOL V2")
    print("=" * 35)
    print(f"Position Type       : {position_name}")
    print(f"Entry Price         : {entry:g}")
    print(f"Stop Loss           : {stop_loss:g}")
    print(f"Take Profit         : {take_profit:g}")
    print("-" * 35)
    print(f"Risk Distance       : {risk:g}")
    print(f"Reward Distance     : {reward:g}")
    print(f"Risk Reward Ratio   : 1 : {rr:.2f}")
    print(f"Breakeven Win Rate  : {breakeven:.2f}%")
    print("=" * 35)


print("=" * 30)
print("     RISK REWARD TOOL")
print("=" * 30)
print()

while True:
    print("1. Calculate Risk Reward")
    print("2. Exit")

    choice = input("Choose (1/2): ").strip()

    if choice == "1":
        calculate_risk_reward()

    elif choice == "2":
        print("See you matee!")
        break

    else:
        print("Error: Choose 1 or 2!")
