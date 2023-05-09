# დავალება #14 - Coke Machine
amount_due = 50

while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    cents = int(input("Insert Coin: "))
    if cents == 5 or cents == 10 or cents == 25:
      amount_due = amount_due - cents
    else:
      print("Wrong amount. Insert correct coin")


if amount_due == 0:
    print("Change Owed: 0")
elif amount_due < 0:
    print(f"Change Owed: {amount_due * - 1}")
