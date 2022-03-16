Decision=""
Started = False
while True:
    Decision = input('>').lower()
    if Decision == 'start':
        if Started :
            print('The car is already started!')
        else:
            Started = True
            print('The car has started...')
    elif Decision == 'stop':
        if not Started:
            print('The car is already stopped!')
        else:
            Started = False
            print('The car has been stopped...')
    elif Decision == 'help':
        print('''
Start - To start the car
Stop - To stop the car
Exit - To exit the car''')
    elif Decision == 'exit':
        print('Thank you! for playing')
        break
    else :
        print ("I don't understand that")