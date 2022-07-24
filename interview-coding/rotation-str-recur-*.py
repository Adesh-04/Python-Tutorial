
def isRotationMutual( string , result ):
    turn = len(string)

    if len(string) != len(result) :
        return False

    for i in range(0,turn):
        left = string[i]
        print(left,end =' . ')
        string2 = string
        string2 = string2.removeprefix(left) + left 
        print(string2)
        if string2 == result :
            return True

    return False
        



if __name__ == '__main__':
    value = isRotationMutual( 'abcd' , 'dabc' )
    print(value)