import random 
game = True
while game == True:
    attempts = 0
    guessed = False
    Random = int(100*(random.random()))
    numbers = input('Select random generation (Random) or manual (Manual): ')
    if numbers == 'Manual':
        number = int(input('Picker, please select a secret number between 1 and 100: '))
        print('Guesser, try to guess the secret number between 1 and 100.')
    else:
        number = Random
        print('Guesser, try to guess the secret number between 1 and 100.')

    while guessed == False:
        guess = int(input('Enter your guess: '))
        attempts += 1
    
        if guess == number:
            print('Correct! You won!!')
            guessed = True
            print('You took ' + str(attempts) + ' attempts')
            game = input('Do you want to play the game again?(True/False) ')
        elif(number - 2) < guess < (number + 2):
            print('Burning')
        elif(number - 10) < guess < (number + 10):
            print('Hot')
        elif (number - 20) < guess < (number + 20):
            print('Warm')
        elif (number - 30) < guess < (number + 30):
            print('Cold')
        elif (number - 100) < guess < (number + 100):
            print('Freezing')
