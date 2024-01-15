from Class_constructor import product

# Creating the products
product1 = product("Stanley Hammer", 9.99, 5)
product2 = product("Quartet Marker", 2.00, 4)

print('Product Data')
print(f'Product Name:\t\t {product1.name}')
print(f'Product price:\t\t {product1.price}')
print(f'Discount percent:\t {product1.discount:d}%')

print(f'Discount Amount:\t {product1.getDiscountAmount():.2f}')
print(f'Product Price:\t\t {product1.getDiscountPrice():.2f}')

