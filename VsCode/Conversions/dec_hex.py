def dec_hex(decimal):
    decimal = int(decimal)
    hexadecimal = ''

    def divideBySixteen(num,hexadecimal):
        result = num // 16
        remainder = num % 16

        hexadecimal = hexadecimal + str(remainder)

        if result > 16:
            return divideBySixteen(result,hexadecimal)
        elif result <= 16:
            hexadecimal = hexadecimal + str(result)
            return hexadecimal[-1::-1]

    val = divideBySixteen(decimal,hexadecimal)
    return val


if __name__ == '__main__':
    val = dec_hex(128)
    print(val)