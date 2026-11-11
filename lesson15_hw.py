# ============ 1 ================

class Car:
    pass
c1 = Car()
c1.brand = "Toyota"
c1.model = "CH-R"
c1.number = "123-345-567"
c1.color = "blue"

c2 = Car()
c2.brand = "Audi"
c2.model = "A4"
c2.number = "678-567-345"
c2.color = "black"

c3 = Car()
c3.brand = "Jeep"
c3.model = "Wrangler"
c3.number = "345-678-234"
c3.color = "Yellow"

garage = [c1, c2, c3]
for car in garage:
    print(f"{car.brand}/ {car.model}/ {car.number}/ {car.color}")

# ================ 2 =================

class Book:
    pass

b1 = Book()
b1.name = "Idiot"
b1.autor = "Fedor Dostoevskiy"
b1.year = "1868"

b2 = Book()
b2.name = "Igra v biser"
b2.autor = "German Gesse"
b2.year = 1942

b3 = Book()
b3.name = "Buddenbroks"
b3.autor = "Tomas Mann"
b3.year = 1900

library = (b1,b2,b3)
years = []
for book in library:
    print(f"{book.name}/{book.year}/{book.autor}")
    years.append(int(book.year))

print(f"The earliest book was written in {min(years)}")

# ============== 3 ==================

class Room:
    pass

room1 = Room()
room1.dimensions = {"height": 2.6, "length": 3.57, "width": 2.77}
room1.name = "Children room 1"
room1.repair_cost = 100
room1.cost_of_furniture_and_accessories = 5000

room2 = Room()
room2.dimensions = {"height": 2.6, "length": 3.57, "width": 3.12}
room2.name = "Children room 2"
room2.repair_cost = 100
room2.cost_of_furniture_and_accessories = 4000

room3 = Room()
room3.dimensions = {"height": 2.6, "length": 3.57, "width": 2.77}
room3.name = "Parent's room"
room3.repair_cost = 200
room3.cost_of_furniture_and_accessories = 3500

apartment = {
    room1:room1.repair_cost+room1.cost_of_furniture_and_accessories,
    room2:room2.repair_cost+room2.cost_of_furniture_and_accessories,
    room3:room3.repair_cost+room3.cost_of_furniture_and_accessories,
}
budget = 0
for room in apartment:
    print(f"{room.name} with dimensions: {room.dimensions}"
          f" funds required for room renovation={apartment[room]}")
    budget+=apartment[room]

print(f"funds required is {budget} nis")



