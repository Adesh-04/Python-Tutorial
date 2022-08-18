#Time Complexiy = O(n**2) and Omega(n)
#Space Complexity = O(1)

import time

arr = []
with open('1000.txt','r') as f:
    var = f.read()
var = var.replace('[',' ').replace(']',' ')
arr = var.split(',')
arr.pop()

def insertionSort(arr):
    for i in range(1, len(arr)):
        tmp = int(arr[i])
        j = i - 1
        
             
        while j >= 0 and tmp < int(arr[j]):
            arr[j + 1] = arr[j]
            j = j - 1
        
        arr[j + 1] = tmp
        
            

                




    return arr



var1 = time.time()
sorted_arr = insertionSort(arr)
var2 = time.time()



print(sorted_arr,'\n\ttime taken {} for {} elements'.format(var2-var1,len(arr)))