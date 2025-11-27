class Rectangle:
    def area(obj):
        return obj.length * obj.breadth

    def perimeter(obj):
        return 2 * (obj.length + obj.breadth)


r1 = Rectangle()
r1.length = int(input("Enter 1st rectangle length: "))
r1.breadth = int(input("Enter 1st rectangle breadth: "))

r2 = Rectangle()
r2.length = int(input("Enter 2nd rectangle length: "))
r2.breadth = int(input("Enter 2nd rectangle breadth: "))

if Rectangle.area(r1) < Rectangle.area(r2):
    print("Rectangle 1 has smaller area than Rectangle 2")
elif Rectangle.area(r1) == Rectangle.area(r2):
    print("Both rectangles have equal area")
else:
    print("Rectangle 1 has greater area than Rectangle 2")
