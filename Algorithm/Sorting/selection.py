#Time Complexity = O(n**2) and Omege(n**2)
#Space Complexity = O(1)

import time

# arr = [1,4,2,6,10,23,3,98,5]
arr=[]
with open('1000.txt','r') as f:
    var = f.read()
arr = var.split(',')
arr.pop()

def selecSort(arr):
    for i in range(len(arr)):
        mini = i
        for j in range(i+1,len(arr)):
            if int(arr[mini]) > int(arr[j]):
                mini = j
        (arr[i] , arr[mini]) = (int(arr[mini]) , int(arr[i]))
    return arr

var1 = time.time()
sort_arr = selecSort(arr)
var2 = time.time()
print(arr,'\n\ttime taken {}s for {} elements'.format(var2-var1,len(arr)))