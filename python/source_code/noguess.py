import random

# this is our random number list between 1 to 50
no = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
ranno = random.choice(no) # this method  for computer random number
# print(ranno)

def game():
    print('\nChoose number between 1 to 50\n ')
    i = 1
    while i <= 10:
        a = int(input('number> ')) 
        if a == ranno:
            print('you win the game\n')
            print('\nThank you for playing game\n')
            main()
        elif a < ranno:
            print('plz enter greator number\n')
        elif a> ranno:
            print('plz enter lesser number\n')
        else:
            print('you loose the game\n')
            print('\nThank you for playing game\n')
            main()
        i+=1
    print('you lost your chance,\nbetter luck try next time😇😇😇')
    print('Thank you for playing game\n')
    print('\nWelcome to our game Number guessing game')
    print('game created by Pavan Coder\n\n')

# this is input system of user
def main():
    print('\nWelcome to our game Number guessing game')
    print('game created by Pavan Coder\n\n')
    print(f'plz enter Yes[y] to play game,No[n] to exit game')
    while True:
        m = input('task> ')
        if m == 'y' or m == 'yes':
            game()
        elif m=='n' or m=='no':
            exit()
        else:
            print('plz type correct cammand y or n ,yes or no\n')
main()
