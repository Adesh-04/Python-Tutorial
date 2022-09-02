import time

start = time.time()

def fibo(prev,val,times):
    if times > 0:
        nxt = prev + val
        # print(prev)
        return fibo(val,nxt,times-1)
    else:
        True

fibo(0,1,500)

end = time.time()

print('time taken: %.5f sec'%(end-start))

