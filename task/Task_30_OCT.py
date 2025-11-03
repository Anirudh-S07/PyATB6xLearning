"""

Q - Create a function which will take a positive number from the user and perform square of the number?

"""


def positive_number_square(input_num):

    if input_num > 0:
        print(input_num**2)
    else:
        print("Please enter input in positive number")


positive_number_square(input_num=int(input("Please enter the number you want to square")))

"""
Q - Create a function which will take the 3 values from the user, which are length of the triangle.  side1, side2, side2
i/p - int side1 == side2 =side3 → isosceles 
o/p = result in string - iso, eq, scalene

"""


def classify_triangle(side1, side2, side3):

    if side1 > 0 and side2 > 0 and side3 > 0:
        if side1 + side2 > side3 and side3 + side2 > side1 and side1 + side3 > side2:
            if side1 == side2 == side3:
                print("Equilateral")
            elif side1 == side2 or side1 == side3 or side2 == side3:
                print("Isosceles")
            else:
                print("Scalene")

        else:
            print("Not a triangle")
    else:
        print("Please enter positive values")


side1 = float(input("Please enter the side 1 :\n"))
side2 = float(input("Please enter the side 2 :\n"))
side3 = float(input("Please enter the side 3 :\n"))


classify_triangle(side1, side2, side3)



