print("=========== food delivery ============")
# food delivery ke liye = menu create ,menu show, discount kitna hoga, fir gst kitna hoga 
#fir kitne order chahiye ,final price
 
# 1. menu create
menu={
     "pizza":200,
     "burger":99,
     "pasta":250,
     "coke":50,
     "garlic bread": 100
}
# 2. menu show 
def show_menu():
    print("----zometo menu----")
    for item,price in menu.items():
        print(f"{item} : {price}")
#3.discount
def apply_discount(bill_amount):
    if bill_amount > 500:
        discount = bill_amount * 0.10  # 10% Discount
        print(f"congratulation!! Aapko {discount} ka discount mila!")
        return bill_amount - discount
    else:
        print("Tip: 500 se upar ki shopping par 10% discount milta hai.")
        return bill_amount  
# 4. GST lagake final bill
def generate_bill(final_amount):
    gst = final_amount * 0.05  # 5% GST
    total = final_amount + gst
    print(f"GST (5%): ₹{gst}")
    print(f" TOTAL PAYABLE: ₹{total}")


# 5.--- Main Program ---
show_menu()


order_item = input("Kya khana chahenge? (Menu se naam likhein): ").lower()

if order_item in menu:
    quantity = int(input(f"Kitne {order_item} chahiye? : "))
    initial_bill = menu[order_item] * quantity
    print(f"Order: {order_item} * {quantity}")
    print(f"Initial Price: ₹{initial_bill}")

    # Discount apply karna
    after_discount = apply_discount(initial_bill)
    
    # Final Bill dikhana
    generate_bill(after_discount)
else:
    print("sorry !!, ye item menu mein nahi hai.")
