# Author: Liz Zayas
#Reflection
#
#1. What surprised me most was that Python lists can hold multiple values while still allowing me to access and alter 
#individual items. I thought that it would be so much more difficult to work with several values at the same time.
#
#2. In accounting, a Python list could be useful when reviewing transactions that need further investigation during the 
#reconciliation process. For example, I could filter a list of recorded payments to identify unusual amounts or possible
#duplicates before comparing them with bank records.

print("--- Exercise 1: Build the List ---")

inventory = ['pen', 'notebook', 'stapler', 'tape', 'marker']
print(inventory)
print(len(inventory))


print("--- Exercise 2: Index Practice ---")
print(inventory[0]) # first item
print(inventory[-1]) # last item
middle = len(inventory) // 2 # calculate the index of the middle item
print(inventory[middle]) # middle item


print("--- Exercise 3: Slicing Practice ---")
print(inventory[:3]) # first three items
print(inventory[-2:]) # last two items
print(inventory[::2]) # every second item


print("--- Exercise 4: Modifying the List ---")
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)


print("--- Exercise 5: Tuple Comparison ---")
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError as error:
    print("TypeError caught:", error)
    print("Tuples protect coordinates: a location should never change by accident.")

print(coords)


print("--- Exercise 6: Average List of sales ---")
sales = [100, 250, 75, 480, 200]
total = sum (sales)
count = len(sales)
average = total / count

print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average}")
print(f"Best: {max(sales)}")
print(f"Worst: {min(sales)}")


print("--- Exercise 7: Accumulator pattern ---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discount = []
for price in prices:
    discount.append(round(price * .9, 2)) # 10% discount

print("Original prices:", prices)
print("Discounts:", discount)


print("--- Exercise 8: Filter above a threshold ---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []
for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print("High sales:", high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales):.2f}")