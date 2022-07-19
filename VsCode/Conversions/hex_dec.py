def hex_dec(hex):
    hexadecimal = str(hex)
    decimal = 0

    for index,element in enumerate(hexadecimal[-1::-1]):
        decimal = decimal + (16**index)*int(element)

    return decimal

if __name__ == '__main__':
    val = hex_dec(11)
    print(val)