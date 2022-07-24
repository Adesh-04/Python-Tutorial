
def numberof(string):
    vowels = [ 'a' , 'e' , 'i' , 'o', 'u' ]
    vowels_count = 0
    consonent_count = 0
    string = string.lower()
    string = string.replace(' ', '')

    for i in string:
        if i in vowels:
            vowels_count += 1
        else:
            consonent_count +=1

    return( 'vowel count is', vowels_count, 'consonent count is', consonent_count)

        




if __name__ == '__main__':
    value = numberof('Hello World')
    print(value)