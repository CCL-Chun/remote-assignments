def avg(data):
    if 'products' not in data or not data['products']:
        return "Please give at least one product and its price"
    price_sum = 0
    amount = 0
    price_avg = 0
    for product in data['products']:
        price_sum = price_sum + product['price']
        amount += 1
    price_avg = price_sum / amount
    return round(price_avg,3)

# test blank 1
print( avg({
"products": [] })
) 

# test blank 2
print( avg({})
) 

# test 1
print( avg({
"products": [ {
"name": "Product 1",
"price": 500 },
{
"name": "Product 2", "price": 700
}, {
"price": 400 }
] })
) 