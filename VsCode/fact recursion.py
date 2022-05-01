import sys, time

start = time.time()


sys.setrecursionlimit(200)

factnumber = 1
def fact(number):
    global factnumber
    factnumber *= number 
    if number-1 == 0:
        print(factnumber)
        return 1

    fact(number-1)



user = int(input('Enter'))
fact(user)
end = time.time()

print('time taken:',end-start,'sec')