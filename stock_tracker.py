stocks = {"AAPL": 180, "TSLA": 250, "GOOG": 140}
total = 0

while True:
    name = input("Enter stock name (or 'done'): ").upper()

    if name == "DONE":
        break

    if name not in stocks:
        print("Stock not found")
        continue

    # Quantity validation loop
    while True:
        try:
            qty = int(input("Enter quantity: "))
            if qty <= 0:
                print("Quantity must be greater than 0")
                continue
            break
        except ValueError:
            print("Please enter a valid number")

    total += stocks[name] * qty

print("Total Investment Value: $", total)

with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment: ${total}")
