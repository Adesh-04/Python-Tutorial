
def dec_oct(decimal):
    octal = ''

    def divideByEight(num,octal):
        result = num//8
        remainder = num%8

        octal = octal + str(remainder)

        # print(result,remainder,octal)

        if result > 8:
            divideByEight(result)
        elif result <= 8:
            octal = octal + str(result)
            return octal[-1::-1]

        return divideByEight(num,octal)
    val = divideByEight(decimal,octal)

    return val

if __name__ == '__main__':
    oct = dec_oct(9)
    print(oct)