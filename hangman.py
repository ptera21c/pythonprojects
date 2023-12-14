from words import words
import random
import string



def get_valid_word(words):
    word=random.choice(words)
    while '-' in word or ' ' in word:
        word=random.choice(words)
    return word.upper()


def hangman():
    word=get_valid_word(words)
    word_letters=set(word)
    alphabet =set(string.ascii_uppercase)
    used_letters=set()
    
    lives=7
    
    while len(word_letters) > 0 and lives > 0:
        print('you have', lives,'left and you have used these letters ', ' '.join(used_letters))
        word_list= [letter if letter in used_letters else '-' for letter in word]
        print('current word: ',' '.join(word_list))
        
        user_letter= input('guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                print('\n your guess', user_letter,' is not in the word')
                lives=lives -1
        elif user_letter in used_letters:
            print('you already used ', user_letter)
        else:
            print('that is not a valid number')
            
    if lives == 0:
        print('you have no lives left')
    else:
        print('you won!')

hangman()