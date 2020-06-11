#exercise source: https://www.w3resource.com/python-exercises/python-basic-exercises.php
#write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years. Go to the editor
#Test Data : amt = 10000, int = 3.5, years = 7

loopcontrol = ''
while loopcontrol != 1:
    userinput = input('please enter the investment amount ')
    testtype = userinput.isnumeric()
    if userinput == 'exit':
        break
    elif testtype == False:
        print('incorrect input')
    else:
        investment = int(userinput)
        inputinterest = input('please enter the interest rate: ')
        testtype1 = inputinterest.isnumeric()
        if inputinterest == 'exit':
            break
        elif testtype1 == False and '.' not in inputinterest:
            print('incorrect input')
        else:
            inputyears = input('please enter the number of years: ')
            interest = float(inputinterest)
            testtype3 = inputyears.isnumeric()
            if inputyears == 'exit':
                break
            elif testtype3 == False:
                print('incorrect input')
            else:
                years = int(inputyears)
                FV  = investment*((1+(0.01*interest)) ** years)
                print(round(FV,2))