debit = input()
total = 0
while True:
    if debit == "NoMoreMoney":
        break
# while debit != "NoMoreMoney":
    debit = float(debit)
    if debit < 0:
        print("Invalid operation!")
        break
    total += debit
    print(f"Increase: {debit:.2f}")
    debit = input()
print(f"Total: {total:.2f}")

