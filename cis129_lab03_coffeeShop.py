# %%
# A simple coffee shop receipt 

# %%
print('***************************************')

# %%
print('My Coffee and Muffin Shop')

# %%
# c is coffee cost, m is muffin cost

# %%
c = 5.00

# %%
m = 4.00

# %%
# coffee is the number of coffees bought, muffin is the number of muffin(s) bought

# %%
coffee = int(input('Number of coffees bought?'))

# %%
muffin = int(input('Number of muffins bought?'))

# %%
coffee_total = int(c * coffee)

# %%
# I created an f-string so that the coffee and muffin prices actually come out as currency, I found this in Chapter 3!

# %%
formatted_coffee_total = f"{coffee_total:.2f}"

# %%
muffin_total = int(m * muffin)

# %%
formatted_muffin_total = f"{muffin_total:.2f}"

# %%
print('***************************************')

# %%
print()

# %%
print('***************************************')

# %%
print('My Coffee and Muffin Shop Receipt')

# %%
print(coffee, 'Coffee at $5 each:','$',formatted_coffee_total)

# %%
print(muffin, 'Muffins at $4 each:','$',formatted_muffin_total)

# %%
subtotal = int(coffee_total + muffin_total)

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

# %%
print('***************************************')


