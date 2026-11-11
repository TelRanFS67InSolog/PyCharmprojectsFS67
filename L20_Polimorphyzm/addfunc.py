
def input_sides_of_triangle():
    side1 = float(input("Enter length of side 1 of triangle>> "))
    side2 = float(input("Enter length of side2 of triangle>> "))
    while True:
        try:
            side3 = float(input("Enter length of side3 of triangle>> "))
            if (side1 + side2) <= side3:
                raise ValueError("This is not triangle this is a line!!")
            else:
                break
        except ValueError as e:
            print(e)
            continue
    return side1,side2,side3

def input_side_for_square():
    return float(input("Enter length of square side>>"))

def input_radius_of_circle():
    return float(input("Enter radius of circle>>"))

def input_number_of_shapes_all_types():
    return int(input("Enter number of shapes of triangle, square, circle (1-5)>>>"))
