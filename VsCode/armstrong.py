# sum of cubes of the digits of a number is equal to the number

number = int(input('Enter : '))

str = str(number)
length = len(str)

list =[]

def isArmstrong(number):
    for i in range(1,length+1):

        var= (number %( 10 ** i ))  // ( 10 ** (i-1))  # General formula for finding digits
        var = var ** 3 
        list.append(var)

    if sum(list) == number:
        print(f'{number} is an armstrong number ')
    else:
        print(f'{number} is not an armstrong number ')

isArmstrong(number)
    



#     digit1= num%10 // 1
#     digit2= (num%100) //10
#     digit3= (num%1000) //100

#     cubing = digit1**3 + digit2**3 + digit3**3
   
#     if cubing == num:
#         print('given number is armstrong')
#     else:
#         print('given number is not an armstrong')



   

# isArmstrong(number)

