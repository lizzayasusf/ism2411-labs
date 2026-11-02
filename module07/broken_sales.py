# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale     # The = sign needs to be replaced with += so each new sale is added to the previous total
print(f"Total: ${total}")

count = 0
for sale in sales:     # Add colon in the for statement; without it Python reports a SyntaxError
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):     # We have to replace <= with < because the last valid index would be len(sales) - 1
    print(sales[i])
    i += 1

# 1) There is a problem with 'total = sale' because this would replace the total with each new sale.
# 2) I think the for statement is missing a colon.
# 3) As the the program runs, Python tries to access an index that doesn't exist.