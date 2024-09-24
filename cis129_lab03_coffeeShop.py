# %%
# A simple coffee shop receipt 

# %%
print('***************************************')

# %%
print('My Coffee and Muffin Shop')

# %%
# c is coffee cost, m is muffin cost, b is bagel cost, t is tea cost

# %%
c = 5.00

# %%
m = 4.00

b = 3.00

t = 2.00

# %%
# coffee is the number of coffee bought, muffin is the number of muffin(s) bought, bagel is the number of bagels bought, tea is the number of tea bought

# %%
coffee = int(input('Number of coffees bought?'))

# %%
muffin = int(input('Number of muffins bought?'))

bagel = int(input('Number of bagels bought?'))

tea = int(input('Number of teas bought?'))

# %%
coffee_total = int(c * coffee)

# %%
# I created an f-string so that the coffee, muffin, bagel, and tea prices actually come out as currency, I found this in Chapter 3!

# %%
formatted_coffee_total = f"{coffee_total:.2f}"

# %%
muffin_total = int(m * muffin)

# %%
formatted_muffin_total = f"{muffin_total:.2f}"

bagel_total = int(b * bagel)

formatted_bagel_total = f"{bagel_total:.2f}"

tea_total = int(t * tea)

formatted_tea_total = f"{tea_total:.2f}"

# %%
print('***************************************')

# %%
print()

# %%
print('***************************************')

# %%
print('My Coffee and Muffin Shop Receipt')

# %%
print(coffee, 'Coffees at $5 each:','$',formatted_coffee_total)

# %%
print(muffin, 'Muffins at $4 each:','$',formatted_muffin_total)

print(bagel, 'Bagels at $3 each:','$',formatted_bagel_total)

print(tea, 'Teas at $2 each:','$',formatted_tea_total)

# %%
subtotal = int(coffee_total + muffin_total + bagel_total + tea_total)

# %%
print('6% tax: $', (subtotal * .06))

# %%
# tax is the calculated sales tax on the purchase, it will be added to the subtotal

# %%
tax = float(subtotal * .06)

# %%
print('---------')

# %%
print('Total: $', (subtotal + tax))  

print('Thank you so much for your purchase! We hope to see you again soon!')

# %%
print('***************************************')


