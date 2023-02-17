shopping_list = {
    'pierkarnia': ['chleb', 'bułki', 'pączek'],
    'warzywniak': ['marchew', 'seler', 'rukola']
}
for shop, products in shopping_list.items():
    print('Idę do', shop.capitalize(), 'i kupuję tam', [product.capitalize() for product in products])

sum = 0
for value in shopping_list.values():
    sum += len(value)
print(f'W sumie kupuję {sum} produktów.')

print('Zmiana kodu')
print('Dodaję commit')

#qweiuasabsfkuasifjkban
