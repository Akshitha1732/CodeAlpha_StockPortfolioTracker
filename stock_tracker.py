import csv

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}
total_value = 0

print("===== STOCK PORTFOLIO TRACKER =====")

while True:
    stock = input("Enter Stock Symbol (or 'done'): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available.")
        continue

    quantity = int(input("Enter Quantity: "))
    portfolio[stock] = quantity

print("\n----- PORTFOLIO SUMMARY -----")

for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    total_value += value
    print(f"{stock} | Quantity: {quantity} | Value: ${value}")

print(f"\nTotal Investment Value: ${total_value}")

with open("portfolio.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Stock", "Quantity", "Price", "Value"])

    for stock, quantity in portfolio.items():
        value = stock_prices[stock] * quantity
        writer.writerow([stock, quantity, stock_prices[stock], value])

print("Portfolio saved as portfolio.csv")