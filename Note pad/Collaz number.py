def Collaz(number):
    try:
        number=input("Enter number: ")
    except NameError and TypeError:
        print ('Invalid value')
    
    while True:
        if number % 2 == 0:
            number = number // 2
        elif number % 2 == 1:
            number = 3 * number + 1
        print (number)
        if number == 1:
            break 
Collaz('number')
