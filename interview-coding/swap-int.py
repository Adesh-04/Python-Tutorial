
def swap(a,b):
    a = a + b   # a = 8 b = 5
    b = a - b   # a = 8 b = 3
    a = a - b   # a = 5 b = 3

    return ( a , b)



if __name__ == '__main__':
    value = swap( 3 , 5 )
    print(value)