import random



def guessgame(x):
    low  = 1
    high = x
    myguess = ''


    randomnumber =  random.randint(low,high)
    while myguess != randomnumber:
        myguess = int(input(f'guess a number between 1 and {x}!'))
        if myguess > randomnumber:
            print(f'{myguess} is too big, try again')

        elif myguess < randomnumber:
            print(f'{myguess} is too small, try again')

    print(f'Congrats! your {myguess} is correct!')

guessgame(10)
