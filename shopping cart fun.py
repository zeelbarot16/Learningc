# ----------------- MAIN PROGRAM -----------------
# Customer shopping cart
customer_cart = [
    ("Milk", 50, 2, 0),           # 2 liters, no discount
    ("Bread", 40, 1, 10),         # 10% discount
    ("Eggs", 5, 12, 0),           # 12 eggs
    ("Butter", 150, 1, 5),         # 5% discount
    ("Dove Shampoo", 200, 1, 0),   # no discount
    ("Lee T-Shirt", 1200, 1, 15),    # 15% discount
    ("CocoNut Oil", 250, 1, 1),     # 1% discount
    ("Apples", 120, 1, 1),          # 1% discount
    ("Bananas", 60, 1, 0),              # no discount
    ("Tomatoes", 30, 1, 2),         # 2% discount
    ("Onions", 25, 1, 1),           # 1% discount
    ("Garlic", 80, 1, 2),               # 2% discount
]

def calculate_item_total(price_per_unit, quantity):
    
    total = price_per_unit * quantity
    return total


def apply_discount(total_amount, discount_percent=0):
    # Discount is optional, default 0%
    discounted_amount = total_amount * (1 - discount_percent / 100)
    return discounted_amount


def add_gst(amount, gst_percent=5):
    # Add 5% GST by default
    total_with_gst = amount * (1 + gst_percent / 100)
    return total_with_gst

# 4. FUNCTION TO PRINT BILL
def print_bill(items_list):
    # items_list = list of dictionaries with name, quantity, price, total
    grand_total = 0
    print("=== Grocery Shop Bill ===")
    for item in items_list:
        print(f"{item['name']} x {item['quantity']} @ ₹{item['price']} = ₹{item['total']:.2f}")
        grand_total += item['total']
    grand_total_with_gst = add_gst(grand_total)
    print("----------------------------")
    print(f"Subtotal: ₹{grand_total:.2f}")
    print(f"Total after GST: ₹{grand_total_with_gst:.2f}")
    return grand_total_with_gst

# 5. FUNCTION TO PROCESS CUSTOMER BILL
def process_customer_bill(cart):
    # cart = list of tuples: (item_name, price_per_unit, quantity, discount_percent)
    items_list = []
    for item in cart:
        name, price, qty, discount = item
        total = calculate_item_total(price, qty)
        total_after_discount = apply_discount(total, discount)
        items_list.append({"name": name, "quantity": qty, "price": price, "total": total_after_discount})
    final_amount = print_bill(items_list)
    return final_amount



# Process the bill
total_bill = process_customer_bill(customer_cart)
print(f"\nGrand Total to pay: ₹{total_bill:.2f}")