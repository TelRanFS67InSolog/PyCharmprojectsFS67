from L19_Inheritance.Food_product import Food_Product
from L19_Inheritance.NotFood_product import NotFood_Product
from L19_Inheritance.milk_food_product import Milk_Food_Product
#from product import Product

f_p1 = Food_Product("Ketchup", "223ffg", 7.89, 10, "26-09-28",
                  "26-10-28", 5)
print(f_p1)

n_f_p1 = NotFood_Product("Pillow", "322tro", 69.9, 4, "50 : 25 : 10", 0.7)

print(n_f_p1)

m_f_p1 = Milk_Food_Product("Milk", "123ghj", 14.07, 4, "26-09-09", "26-10-10", 5, 28, "cow", "False")
print(m_f_p1)