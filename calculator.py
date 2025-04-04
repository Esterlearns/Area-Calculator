#Area Calculator

import math

1 == 'Triangle'
2 == 'Rectangle'
3 == 'Square'
4 == 'Circle'

answer = int(input('Which shape: '))

if answer == 1:
    base = int(input('Base: '))
    height = int(input('Height: '))
    area = 1/2*base*height
    print('The area is ', area)
elif answer == 2:
    length = int(input('Length: '))
    width = int(input('Width: '))
    area = length*width
    print('The area is ', area)
elif answer == 3:
    side = int(input('Side: '))
    area = side**2
    print('The area is ', area)
elif answer == 4:
    radius = int(input('Radius: '))
    area = math.pi*radius**2
    print('The area is ', area)
else:
    print('Quit')