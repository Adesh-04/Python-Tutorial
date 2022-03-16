import time

start = time.time()

def fibonacci(data):
    prev2 = 0
    prev = 1
    i=0
    while i <= data:
        print(prev2)

        fib = prev2 + prev
        prev2 = prev
        prev = fib
        i+=1
        


fibonacci(5) # no.of digits u want to get

end = time.time()

print('time taken: ', end-start , 'sec')
