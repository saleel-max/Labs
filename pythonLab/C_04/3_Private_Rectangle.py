class Rectangle:
    def __init__(a, length, width):
        a.__length = length
        a.__width = width

    def area(a):
        return a.__length * a.__width

    def __lt__(a, b):
        return a.area() < b.area()


l1 = int(input("Enter length of Rectangle 1: "))
w1 = int(input("Enter width of Rectangle 1: "))

l2 = int(input("Enter length of Rectangle 2: "))
w2 = int(input("Enter width of Rectangle 2: "))

r1 = Rectangle(l1, w1)
r2 = Rectangle(l2, w2)

if r1 < r2:
    print("Rectangle 1 has smaller area.")
else:
    print("Rectangle 1 does not have smaller area.")
