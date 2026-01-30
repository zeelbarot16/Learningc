
# --------------------------------------------------------------------
# --------------------------------------------------------------------
# TOPIC: FUNCTIONS (SMALL BANKER / STOCK MANAGEMENT)
#---------------------------------------------------------------------
# A small banker is taking care - stock instructions.
# buy , sell , check stock portfolio
# using functions -- organize workflow and repeation code

# 1. func to buy a stock
# func to sell stocks
# func to short sell - 
# func to buy future stocks
# func to future contracts
# func to manage client instruction
# Then Build a Main program to run these...ease of banker

# Ye Buy wala func
def buy_stock(stock_name, quantity, price_per_stock):
    # Simulate buying stocks
    total_cost = quantity * price_per_stock
    print(f"Bought {quantity} stocks of {stock_name} at ₹{price_per_stock} each, total cost: ₹{total_cost}")
    return {"stock": stock_name, "quantity": quantity, "price": price_per_stock}

#buy_stock("dlf", 10, 122)

# ye Sell wala

def sell_stock(stock_name, quantity, price_per_stock):
    # Simulate selling stocks
    total_earnings = quantity * price_per_stock
    print(f"Sold {quantity} stocks of {stock_name} at ₹{price_per_stock} each, total earnings: ₹{total_earnings}")
    return {"stock": stock_name, "quantity": quantity, "price": price_per_stock}

#sell_stock("dlf", 10, 125)

# 3 Func short sell - 

def short_sell(stock_name, quantity, target_profit_percent, current_price):
    target_price = current_price * (1 - target_profit_percent / 100)
    print(f"Short Sold {quantity} stocks of {stock_name}, target exit price: ₹{target_price:.2f} for {target_profit_percent}% profit")
    return {"stock": stock_name, "quantity": quantity, "target_price": target_price}


#short_sell("DLF", 10, 1, 100)

# 5. buy future
def buy_future(stock_name, quantity, future_price):
    print(f"Bought FUTURE contract of {quantity} stocks of {stock_name} at ₹{future_price} per stock")
    return {"stock": stock_name, "quantity": quantity, "future_price": future_price}

# buy_future("DLF", 100, 195)

# 5. Func to manage Client instruction:
def manage_client_instructions(instructions):
    # Loop through all instructions and call relevant functions
    portfolio = []
    for instr in instructions:
        action = instr["action"]
        stock = instr["stock"]
        qty = instr.get("quantity", 0)
        price = instr.get("price", 100)  # default simulated price
        if action == "buy":
            portfolio.append(buy_stock(stock, qty, price))
        elif action == "sell":
            portfolio.append(sell_stock(stock, qty, price))
        elif action == "short_sell":
            portfolio.append(short_sell(stock, qty, instr.get("profit_percent", 0), price))
        elif action == "buy_future":
            portfolio.append(buy_future(stock, qty, price))
    return portfolio                       


print("===== Small banker management ====")

# clienr instr for session

client_management = [
     {"stock": "HDFC", "action": "short_sell", "quantity": 50, "profit_percent": 2, "price": 1600},
     {"stock": "ICICI", "action": "buy_future", "quantity": 50, "price": 900},
     {"stock": "TATA COFFEE", "action": "sell", "quantity": 30, "price": 1200},
     {"stock": "DLF", "action": "buy", "quantity": 100, "price": 350}
]

portfolio_after_morning = manage_client_instructions(client_management)

print("====Print the Portfolio ====")
for stock in portfolio_after_morning:
    print(stock)