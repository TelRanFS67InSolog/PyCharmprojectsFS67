import sys

from L20_Polimorphyzm.addfunc import *

try:
    from L20_Polimorphyzm.Circle import Circle
    from L20_Polimorphyzm.Shape import Shape
    from L20_Polimorphyzm.Square import Square
    from L20_Polimorphyzm.Triangle import Triangle
except ModuleNotFoundError:
    from Circle import Circle
    from Shape import Shape
    from Square import Square
    from Triangle import Triangle


def menu():
    while True:
        print("Enter ***1*** if you want to create and operate with circle")
        print("Enter ***2*** if you want to create and operate with square")
        print("Enter ***3*** if you want to create and operate with triangle")
        print("Enter ***4*** if you want to find shape with biggest area and perimeter")
        print("Enter ***Q*** if you want to exit")

        choice = int(input("Enter your choice number:"))

        if choice==3:

            side1,side2,side3 = input_sides_of_triangle()
            print("What do you want to get: perimeter(enter 1) or area(enter 2)?")
            choice_operate = int(input("Enter your choice>>"))
            shape = Triangle(side1,side2,side3)
            if choice_operate == 1:
                print(shape.perimeter())
                sys.exit()
            elif choice_operate == 2:
                print(shape.area())
                sys.exit()
            else:
                sys.exit()

        if choice == 2:
            side = input_side_for_square()
            print(f"area of square is {Square(side).area()} and perimeter of square is {Square(side).perimeter()}")
            break

        if choice==1:
            radius=input_radius_of_circle()
            print(f"The perimeter of circle is {Circle(radius).perimeter():.2f}, the area of circle is {Circle(radius).area():.2f}")
            break

        if choice==4:
            n = input_number_of_shapes_all_types()
            shapes=[]
            for i in range(n):
                side1,side2,side3=input_sides_of_triangle()
                triangll=Triangle(side1,side2,side3)
                t = {"name":triangll.name, "sideA":triangll.side_of_triangle1,
                     "sideB":triangll.side_of_triangle2,
                     "sideC":triangll.side_of_triangle3,
                     "area":triangll.area(),
                     "perimeter":triangll.perimeter()}
                shapes.append(t)
                side_s=input_side_for_square()
                square=Square(side_s)
                s={"name":square.name, "side":square.side, "area": square.area(), "perimeter": square.perimeter()}
                shapes.append(s)
                radius=input_radius_of_circle()
                circle=Circle(radius)
                c={"name":circle.name, "radius":circle.radius, "area":circle.area(), "perimeter":circle.perimeter()}
                shapes.append(c)
            print(shapes)
            print(f"The shape with maximal area is: {max(shapes, key = lambda x: x['area'])}")
            print(f"The shape with maximal perimeter is: {max(shapes, key = lambda x: x['perimeter'])}")


        sys.exit()


if __name__ == "__main__":
    try:
        triangll = Triangle(5, 4, 8)
    except ValueError:
        print("Its a line, not triangle!!")
    menu()

