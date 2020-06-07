# exercise source: https://www.w3resource.com/python-exercises/python-basic-exercises.php
# circle calculator with math.pi function

import math
loopcontrol = 0

while loopcontrol != 1:
    menuinput = input('please enter the unit to calculate the circle \n [1] Radius || [2] Diameter || [0] to exit program\n your input: ')
    if menuinput == '1':
        inputradius = (input('please enter the radius of the circle (in cm): '))
        typetestradius = type(inputradius) == float
        typetestradius2 = type(inputradius) == int
        if typetestradius == True or typetestradius2 == False:
            r=float(inputradius)
            print('=======================================================')
            print('the area of your circle is',(math.pi*r**2), 'cm')
            print('the circumference of your circle is',(2*math.pi*r), 'cm')
            print('=======================================================')
        else:
            print('wrong input')
    elif menuinput == '2':
        inputdiameter = input('please enter the diameter of the circle (in cm): ')
        typetestdiameter = type(inputdiameter) == float
        typetestdiameter2 = type(inputdiameter) == int
        if typetestdiameter == True or typetestdiameter2 == False:
            d=float(inputdiameter)
            print('=======================================================')
            print('the area of your circle is',(math.pi*(d/2)**2), 'cm')
            print('the circumference of your circle is', (2*math.pi*(d/2)), 'cm')
            print('=======================================================')
        else:
            print('wrong input')
    elif menuinput == '0':
        print('program ended')
        break
    else:
        print('wrong input')