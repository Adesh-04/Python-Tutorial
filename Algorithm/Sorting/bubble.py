#Time Complexity == O(n**2) and Omega(n)
#Space Complexity == O(1)

import time
import random

arr = []

with open('1000.txt','r') as f:
    var = f.readline()

# print(type(var))
var = var.replace('[',' ').replace(']',' ')
arr = var.split(',')
arr.pop()
# print(arr)


def bubbleSort(arr):
    for i in range(len(arr)):
        swapped = False

        for index,ele in enumerate(arr):
            
            if index < len(arr)-1:
                if int(ele) > int(arr[index+1]) :
                    arr[index] = arr[index+1]
                    arr[index+1] = ele
                    swapped = True
                else:
                    continue
        if swapped == False:
            break;
            
                
            
    return arr

var1 = time.time()
sorted_arr = bubbleSort(arr)
var2 = time.time()



print(sorted_arr,'\n\ttime taken {}s for {} elements'.format(var2-var1, len(arr)))