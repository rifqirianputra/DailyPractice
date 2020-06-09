#excercise source: https://www.w3resource.com/python-exercises/python-basic-exercises.php

print('''
strings that makes
new lines
when i press enter on the code
without having to write print in
every line
''')


print('date calculator')
loopcontrol = ''
from datetime import date

while loopcontrol != 1:
    print('================================')
    print('================================')
    print('write "exit" to end program')
    print('================================')
    print("today is: ")    
    dd = int(input('please enter date digit: '))
    mm = int(input('please enter month digit: '))
    yyyy = int(input('please enter year digit: '))

    print("your next birthday is: ")
    dd2 = int(input('please enter date digit: '))
    mm2 = int(input('please enter month digit: '))
    yyyy2 = int(input('please enter year digit: '))

    if dd < 1 and dd >= 31 and dd2 < 1 and dd2 >= 31:
        print('invalid date')
    elif mm < 1 and mm >= 12 and mm2 < 1 and mm >= 12:
        print('invalid month')
    elif dd == 'exit' or dd2 == 'exit' or mm == 'exit' or mm2 == 'exit':
        break
    else:
        f_date = date(yyyy, mm, dd)
        l_date = date(yyyy2, mm2, dd2)
        delta = l_date - f_date
        print('your next birthday will be in', delta.days, 'days')
        