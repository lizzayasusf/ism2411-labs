# Self-Assessment Questions
# 1. The first bug I spotted was the missing colon. I found it from a print() statement, and I understood the other two after
# asking AI. Based on this, I would say my current debugging instincts are not that good.
# 2. The apply_discount(price, tier) function takes the original price of an item and the customer's tier as inputs. It uses
# the tier to determine the discount that should be applied to the original price and returns the price after the discount. In
# my opinion, a colleague could understand how to use the function without reading its body if they understood what wach input
# represents and what the function returns.
# 3. Possible AI Disclosure: I used ChatGPT to help me understand Python error messages and debugging concepts. I used it as a
# guide and made the corrections myself.
# Reflection: Using AI helped me build my understanding because it explained what the error messages meant and why the bugs 
# occurred. Instead of just copying the corrections, I learned how syntax errors, index errors, and logic errors affected the
# program.

# --- Exercise 1 ---

# Define calculate tax function

def calculate_tax(price, rate):
    return price * rate

# Calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}")
print(f"Tax on $250 at 8%: ${tax2:.2f}")
print(f"Another Tax: ${calculate_tax(150, 0.05):.2f}")

# --- Exercise 2 ---

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

# Calling the function

price = 200
tiers = ["gold", "silver", "bronze", "none"]

for tier in tiers:
    print(f"{tier}: ${apply_discount(price, tier):.2f}")

# --- Exercise 3 ---

# Write it out manually first, then refractor into a function

discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"After gold discount: ${discounted:.2f}")
print(f"After tax; ${after_tax:.2f}")

# Refactor into a function

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

print(f"Final price: ${final_price(200, 'gold', 0.07):.2f}")

# --- Exercise 4 ---

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price:.2f}, Tier: {tier}, Final: ${total:.2f}")


# --- Exercise 6 ---

x = 100  # variable # Global

def double_it():
    x = 999   # another variable (not the same variable as above)
    return x * 2

print(x)
print(double_it)
print(x)