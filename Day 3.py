#exercise source: https://www.w3resource.com/python-exercises/python-basic-exercises.php
#Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them

first = (input('please enter your first name: '))
last = (input('please enter your last name: '))
print(last,' ',first)

#Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
data = 3,5,7,23
print(list(data))
print(tuple(data))

#Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
#Sample filename : abc.java
#Output : java

filename = input('please enter your filename: ')
splitname = filename.split('.')
print(splitname[-1])

#Write a Python program to display the first and last colors from the following list. Go to the editor
color_list = ["Red","Green","White" ,"Black"]
print(color_list[0], color_list[3])

#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
#Sample value of n is 5
#Expected Result : 615

n = int(input('please enter the number to run n+nn+nnn: '))
print(f'the result of {n}+{n}{n}+{n}{n}{n} is: ')
n1 = int('%s'%n)
n2 = int('%s%s'%(n,n))
n3 = int('%s%s%s'%(n,n,n))
print(n1+n2+n3)