


def reverse_str(string):
    for i in range (1,len(string)+1):
        print(string[-i], end='')

def reverse_str2(string):
    val = string[-1::-1]
    print(val)





if __name__ == '__main__':
    reverse_str('Hello World')
    print(' ')
    reverse_str2('Hello World')