from array import *
arr = array('s',[16 * (10 ** 307),1233,0]) 

## insertion
arr.insert(1,3)

## deletion
arr.pop() or arr.remove(3.0)

## search
print(arr.index(1233))

## updation
arr[0] = 12

## traversing
for i in arr:
    print(i)


# range of int 
    # b ==> -127 to 127
    # B ==> 0 to 127
    # i ==> -(2**31) to (2**31)
    # I ==> 0 to (2**31)
    # f ==> 1.2E-38 to 3.4E+38  i.e. [-12 * (10 ** 37)] to [34 * (10 ** 37)]
    # d ==> 2.3E-308 to 1.7E+308 i.e [-23 * (10 ** 307)] to [17 * (10 ** 307)]
