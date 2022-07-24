
def fact(num,val):
    if num == 1:
        return val

    return fact(num-1,val*num)
    


if __name__ == '__main__':
    value = fact(5,1)
    print(value)