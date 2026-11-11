# 1A
class Car:
    pass


c1 = Car()
c1.brand = "Skoda"
c1.model = "Kamiq"
c1.year = 2025
c1.color = "White"

c2 = Car()
c2.brand = "Toyota"
c2.model = "Yaris"
c2.year = 2024
c2.color = "White"

c3 = Car()
c3.brand = "BMW"
c3.model = "X5"
c3.year = 2025
c3.color = "Black"

garage = [c1, c2, c3]
print("--- Garage ---")
for car in garage:
    print(f"Car: {car.brand}, {car.model} | Year: {car.year} | Color: {car.color}")
print()


# 1B with prices
class Car:
    pass


c1 = Car()
c1.brand = "Skoda"
c1.model = "Kamiq"
c1.year = 2025
c1.color = "White"

c2 = Car()
c2.brand = "Toyota"
c2.model = "Yaris"
c2.year = 2024
c2.color = "White"

c3 = Car()
c3.brand = "BMW"
c3.model = "X5"
c3.year = 2025
c3.color = "Black"

garage = {}  # price in shekels
garage[c1] = 140000
garage[c2] = 160000
garage[c3] = 260000

print("--- Garage ---")
for car in garage:
    price = garage[car]
    print(f"Car: {car.brand}, {car.model} | Year: {car.year} | "
          f"Color: {car.color} | Price: {price}")
print()


# 2

class Book:
    pass


b1 = Book()
b1.title = "1Q84"
b1.author = "Харуки Мураками"
b1.year = "2009"
b1.genre = "Магический реализм"

b2 = Book()
b2.title = "Последний сон разума"
b2.author = "Дмитрий Липскеров"
b2.year = "2000"
b2.genre = "Современная проза"

b3 = Book()
b3.title = "Ананасная вода для прекрасной дамы"
b3.author = "Виктор Пелевин"
b3.year = "2010"
b3.genre = "Постмодернизм"

library = (b1, b2, b3)
print("--- My Library ---")
for book in library:
    print(f"Book: {book.title} | Author: {book.author} | "
          f"Year: {book.year} | Genre: {book.genre}")
print()


# 3

class Product:
    pass


p1 = Product()
p1.name = "Kiwi"
p1.variety = "Gold"
p1.country = "Israel"
p1.delivery_date = "17.08.2025"
p1.expiry_date = "17.09.2025"
p1.organic = True

p2 = Product()
p2.name = "Mango"
p2.variety = "Maya"
p2.country = "Spain"
p2.delivery_date = "20.08.2025"
p2.expiry_date = "10.09.2025"
p2.organic = False

p3 = Product()
p3.name = "Grape"
p3.variety = "Muscat"
p3.country = "Italy"
p3.delivery_date = "22.08.2025"
p3.expiry_date = "22.09.2025"
p3.organic = False

p4 = Product()
p4.name = "Strawberry"
p4.variety = "Great"
p4.country = "Greece"
p4.delivery_date = "25.08.2025"
p4.expiry_date = "05.09.2025"
p4.organic = True

fruit_shop = {}  # weight of product in kg
fruit_shop[p1] = 15.7
fruit_shop[p2] = 14
fruit_shop[p3] = 23.8
fruit_shop[p4] = 34

print("---- FRUIT Shop: Inventory ----")
for product in fruit_shop:
    weight = fruit_shop[product]
    print(f"{product.name} ({product.variety}) = {weight} kg")

print("-" * 31)

for product in fruit_shop:
    if product.organic == True:
        print(product.name, "- Organic")
    else:
        print(product.name, "- Standart")
