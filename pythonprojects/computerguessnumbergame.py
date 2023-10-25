import random



def guessgame(x):
    low  = 1
    high = x
    feedback = ''


    while feedback != 'c':
        if low == high:
            guess = low
        randomnumber =  random.randint(low,high)
        feedback = input(f'is {randomnumber} too big(b)? too small(s)? or correct(c)?')
        if feedback == 'b':
            print(f'{randomnumber} is too big, try again')
            high = randomnumber -1
        elif feedback == 's':
            print(f'{randomnumber} is too small, try again')
            low = randomnumber +1
    print(f'Congrats! your {guess} is correct!')

guessgame(10)
