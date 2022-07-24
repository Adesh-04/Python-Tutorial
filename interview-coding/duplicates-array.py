
def duplicates(arr):
    
    doubles = []

    for i in arr:
        count = 0
        for j in arr:
            if i == j:
                count += 1
        if count > 1 and i not in doubles: 
           doubles.append(i) 

    return doubles



if __name__ == '__main__':
    value = duplicates(  [1,3,2,4,1,5,7,3,7,2,0]  )
    print( 'duplicates are', value)