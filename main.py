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
