import random
def play():
    user = input("'r' for rock, 'p' for paper,'s' for sciossors" + '\n')
    computer = random.choice(['r','p','s'])
    
    if user == computer:
        
        return 'draw'
    
    if is_win(user,computer):
       
        return 'you won!'
    
    return 'you lost!'
#r > s, s>p, p>r    
def is_win(player,opponent):
    if (player =='r' and opponent=='s') or (player=='s' and opponent=='p') or(player=='p' and opponent=='r'):
        return True
    

print(play())
