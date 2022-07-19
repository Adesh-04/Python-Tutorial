def oct_dec(octal):
    octal = str(octal)
    decimal = 0

    for index,element in enumerate(octal[-1::-1]):
        decimal = decimal + (8**index)*int(element)

    return decimal

if __name__ == '__main__':
    val = oct_dec(11)
    print(val)