
def reverse_array(arr):
    arr = reversed(arr)
    reverse = []
    for i in arr:
        reverse.append(i)

    return reverse




if __name__ == '__main__':
    value = reverse_array( [ 'a' , 'e' , 'i' , 'o', 'u' ] )
    print(value)