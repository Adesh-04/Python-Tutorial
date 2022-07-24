
def isPrime(val,prime):
    

    if val not in prime:
        for i in prime:
            if val%i == 0:
                return False
        prime.append(val)
    else:
        return True

    return isPrime(val,prime)




if __name__ == '__main__':

    num = 19

    value = isPrime(num,[ 2 , 3 , 5 , 7 ])
    print(f'The {num} is Prime => {value}')