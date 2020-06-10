# exercise source: https://www.w3resource.com/python-exercises/python-basic-exercises.php
# Write a Python program to check whether a specified value is contained in a group of values.

sample_list = [1,3,4,5,7,6,8,9,23,15,17,19,20,24,23,26,27]
def checklist (sample_list, n):
    for value in sample_list:
        if n == value:
            return True
    return False

print(checklist(sample_list,1))
print(checklist(sample_list,2))
print(checklist(sample_list,3))


# Write a Python program to print all even numbers from a given numbers list in the same order and stop the pri6nting
# if any numbers that come after 237 in the sequence.
numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]
for i in numbers:
    if i == 237:
        print (i)
        break
    elif i %2 == 0:
        print(i)

# Write a Python program that will accept the base and height of a triangle and compute the area.

b = int(input('what is the base length of your triangle: '))
h = int(input('what is the height length of your triangle: '))

area = 0.5 * b * h

print('the area of your triangle is: ',area,'cm')
