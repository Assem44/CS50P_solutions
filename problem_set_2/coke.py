amount_due = 50
while amount_due > 0:
    print(F"Amount Due: {amount_due}")
    get_coin = input("Insert Coin: ").strip()
    if get_coin in ["5", "10", "25"]:
        amount_due -= int(get_coin)
print(f"Change Owed: {abs(amount_due)}")
