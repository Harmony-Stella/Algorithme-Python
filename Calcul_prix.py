def calculateTotalPrice(prices, discount):
    max_price = max(prices)
    total_price = sum(prices)
    discount_amount = max_price * discount / 100
    total_price -= discount_amount
    return int(total_price)
prices = [50, 80, 30, 70, 60,100]
discount = 25
total_price = calculateTotalPrice(prices, discount)

print("Total price after discount: ", total_price)
