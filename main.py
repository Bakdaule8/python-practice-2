# Task 1
customer_name = input('Enter your name: ')
a = ''
item = 0
total = 0
while a != 'done':
    a = input('Enter product name (or \'done\' to finish): ')
    if a == 'done':
        break
    b = int(input('Enter price: '))
    item += 1
    total += b

print('Customer: ' , customer_name.upper())
print('Items: ' , item)
print('Subtotal: ' , total , 'KZT')

# Task 2
print("------------------------------")

if total < 3000:
    discount_rate = 0
    tier = "No discount"
elif total < 7000:
    discount_rate = 0.05
    tier = "5% discount"
else:
    discount_rate = 0.15
    tier = "15% discount"

discount_amount = total * discount_rate
final_total = total - discount_amount

print("Discount tier :", tier)
print("Discount :", discount_amount, "KZT")
print("Total :", final_total, "KZT")

# Task 3
print("------------------------------")

print("Name uppercase :", customer_name.upper())
print("Name lowercase :", customer_name.lower())
print("Name length :", len(customer_name))

if len(customer_name) > 5:
    print("Long name")
else:
    print("Short name")
