
def pal(string):
    string = string.lower()
    isPal = True
    for i in range(0,len(string)):
        if string[i] == string[-(i+1)]:
            continue

        else :
            isPal = False
            print('Not a Palindrome')

    return isPal



if __name__ == '__main__':
    value = pal('racecar')
    print(value)