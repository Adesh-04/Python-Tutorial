import time

start = time.time()

def prime(data):
    for i in data:
        for j in data:
            value = 10 * i + j
            
            # print(value)
            primes = [1,2,3,5,7]

            global Primes
            

            if value%2 == 0 or value%3 == 0 or value%5 == 0 or value%7 == 0:
                continue
            elif value in primes:
                Primes +=1
            else :
                Primes +=1
    # print(Primes)
                
    yield Primes
            
global Primes
Primes = 0

insert = prime([1,2,1,3])
for nums in insert:
    print(nums)


end = time.time()

print(end-start)