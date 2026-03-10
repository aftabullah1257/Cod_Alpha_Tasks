def stock_tracker():
    # Hardcoded stock prices
    prices = {"AAPL": 180, "TSLA": 250, "GOOG": 150, "MSFT": 400}
    portfolio = {}
    total_value = 0

    print("Stock Portfolio Tracker")
    count = int(input("How many different stocks do you own? "))

    for _ in range(count):
        name = input("Enter stock name (e.g., AAPL): ").upper()
        if name in prices:
            qty = int(input(f"Enter quantity for {name}: "))
            portfolio[name] = qty
            total_value += qty * prices[name]
        else:
            print("Stock price not found in our system.")

    print("\n--- Portfolio Summary ---")
    for stock, qty in portfolio.items():
        print(f"{stock}: {qty} shares")
    
    print(f"Total Investment Value: ${total_value}")

stock_tracker()