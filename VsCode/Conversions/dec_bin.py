def dec_bin(decimal):
    decimal = int(decimal)
    binary = ''

    def divideByTwo(num,binary):
        result = num // 2
        remainder = num % 2

        binary = binary + str(remainder)

        if result >= 2:
            divideByTwo(result,binary)
        elif result < 2:
            binary = binary + str(result)
            return binary[-1::-1]

    val = divideByTwo(decimal,binary)
    return val


if __name__ == '__main__':
    val = dec_bin(16)
    print(val)