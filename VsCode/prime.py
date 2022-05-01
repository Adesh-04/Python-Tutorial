# prime are not divisible by any number except 1 and itself

number =  4  #int(input('Enter : '))
list=[2,3,5,7,11,13,17,19]

def isprime():
    for item in list:
        if number // item == 0:
            print(f'{number} {item} ')
            print('not')
        else:
            list.append(number)
    
isprime()