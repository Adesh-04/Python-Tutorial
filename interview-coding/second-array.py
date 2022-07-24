
def OrderBySize(arr):
    # Remove Duplicate Values    
    set_arr = set(arr)
    arr = list(set_arr)

    # Sort the Array
    arr.sort(reverse=True)

    print('\nThe Highest to Smallest \n\t--> ', end=''  )
    for i in arr:
        print(i,end = ' - ')

    return 'End'


if __name__ == '__main__':
    value = OrderBySize( [1,2,4,90,65,334,1,23,313] )
    print(value)