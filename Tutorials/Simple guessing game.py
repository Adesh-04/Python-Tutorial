i=1
print('Guess from 1-9 ')
while i<=3:
    b=int(input("Guess: "))
    if b==8:
        print('You Won!')
        break;
    i+=1
else:
    print('You Lost!')