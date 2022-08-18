# Time Complexity = O(n+k)  
# Space Complexity = O(k)



def countingSort(arr):
    sl = []
    new = []
    maxi = arr[0]
    mini = arr[0]

    for i in arr:
        if int(i) > int(maxi):
            maxi = int(i)
        elif int(i) < int(mini):
            mini = int(i)
    
    if mini > 0 : range_val = maxi + 1
    else: range_val = maxi - mini + 1

    c_arr = [ [0]*range_val for m in range(1) ]
    c_arr = c_arr[0]

        

    for i in range(len(arr)):
        c_arr[int(arr[i])]+=1

    for index,i in enumerate(c_arr):
        if index > maxi:  # For negative Values
            while i > 0:
                new.append(index)
                i -= 1
        while i > 0:
            sl.append(index)
            i -= 1
    new = [(i-len(c_arr)) for i in new]  # Getting indexes of negative
    new.extend(sl)
            
    print(new)
    return new


if __name__ == '__main__':
    arr = [-1,-5,-19,-1000,-11,-1,-6,1,4,2,8,4,9,2,7,2]
    # with open('1000.txt','r') as f:
    #     val = f.read()
    # arr = val.split(',')
    # arr.pop()
    countingSort(arr)