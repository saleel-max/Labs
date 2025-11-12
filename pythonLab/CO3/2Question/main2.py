print('\n------ selective import method ----------')

from graphics.rectangle import area, perimeter
from graphics.circle import area as circle_area, perimeter as circle_perimeter

print("Rectangle area:", area(10, 5))
print("Rectangle perimeter:", perimeter(10, 5))
print("Circle area:", circle_area(7))
print("Circle perimeter:", circle_perimeter(7))
