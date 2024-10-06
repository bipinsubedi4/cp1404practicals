total_price = 0
items = int(input("Number of items: "))
while items < 0:
    print("Invalid number of items: ")
    items = int(input("Number of items: "))
for i in range(0, items, 1):
    price = float(input(f"Price of item {i+1}: "))
    total_price += price
if total_price > 100:
    discount = total_price * 0.10
    total_price = total_price - discount

print(f"Total price for {items} items is ${total_price:.2f}")