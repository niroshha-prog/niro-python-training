order_amount = float(input("Enter amount: ")) 
print("Original order amount", order_amount)
total_bill_amount = order_amount

# To avoid double discounting
if order_amount >= 1000:
    discount = 0.10 * order_amount
    total_bill_amount = order_amount - discount
    print("After 10 % discount", total_bill_amount)
elif order_amount >= 500:
    discount = 0.05 * order_amount
    total_bill_amount = order_amount - discount
    print("After 5 % discount", total_bill_amount)
    # Customer type outside to add discount 
customer_type = input("Enter customer type: ")
print("customer_type", customer_type)

# Additional discount for prime member
if customer_type == "prime" and order_amount > 1000:
    prime_discount = 0.15 * order_amount
    total_bill_amount = total_bill_amount - prime_discount

# Delivery and payment details
delivery_distance = float(input("Enter distance: "))
payment_method = input("Choose delivery method: ")
if payment_method == "cod" and order_amount < 500:
    cod_add_amount = total_bill_amount + 25
    total_bill_amount = cod_add_amount
print("Final Bill Amount:", total_bill_amount)

