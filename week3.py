def calculate_discount(price,discount_percent):
    if discount_percent>20:
        return int(price-(price*discount_percent/100))
    return price
try:
    price=int(input("Input the Original Price of the object: "))
    discount=int(input("Input the Discount percentage(between 1-100): "))
    if discount < 1 or discount > 100:
        print("Please input a valid discount percentage")
    else:
        discounted_price=calculate_discount(price,discount)
        print (discounted_price)
except ValueError:
    print ("Enter A valid number")
