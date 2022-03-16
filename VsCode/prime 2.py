# input any number of one digit number to get number of possible two digit prime numbers

# Enter Y or N for stoping entering;
import time



def prime(data) :
    global Primes
    Primes = 0

    def iter(elements):
            # index = 0-n : len = 1-n
        for i in range(len(elements)):
            for j in range(len(elements) - 1):
                if j >= len(elements):
                    break
                else:
                    value = ( 10 * elements[i] ) + elements[j]
                    # checks 
                    if value%2 == 0 or value%3 == 0 or value%5 == 0 or value%7 ==0 or value == 7 or value == 2 or value == 3 or value == 5 :
                        isCont=False     # does nothing just here for fun
                    else :
                        global Primes 
                        Primes +=1
        return Primes  


    iter(data)
    data.reverse()
    iter(data)

    print(Primes)
    

start = time.time()

list = []
isCont=True    # is continued

def iteration():

    for i in range (5):
        try:
            value = int(input('Enter: '))
            
            if value >= 10:
                print('Enter only 1 digit')
            else:
                list.append(value)
            
        except TypeError :
            print('Enter only numbers')
        except ValueError :
            print('Enter only numbers')
        
    return list

iteration()


while isCont :
    choose = input('Do You Want To Continue Y or N: ')

    if choose.upper() == 'Y':
        iteration()
    elif choose.upper() == 'N':
        isCont = False
        
prime(list)
        
        
end = time.time()

print('time taken:',end-start,'sec')



