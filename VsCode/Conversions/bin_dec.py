
def bin_dec(binary):
    binary = str(binary)
    decimal = 0

    binary_rev = binary[-1::-1]

    for index,element in enumerate(binary_rev):
        decimal = decimal + (2**index)*int(element)

    return decimal

if __name__ == '__main__':
    dec = bin_dec(1001)
    print(dec)
