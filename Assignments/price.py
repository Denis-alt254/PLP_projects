def calculate_discount(price, discount_percent):
    if discount_percent < 20:
        return f"Price = ${price}"
    else:
        return f"Price = ${price - (price * discount_percent / 100)}"

price = input("Enter the price: ")
discount_percent = input("Enter the discount percent: ")
price = float(price)
discount_percent = float(discount_percent)
print(calculate_discount(price, discount_percent))