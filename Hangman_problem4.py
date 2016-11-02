'''When playing Hangman, a user should be guessing one unique
letter at a time: let's call those 'legal guesses'. When a
user guesses a number, symbol, or two-letter guess, let's
call those 'illegal guesses'. Based on the newly guessed
letter and a string of all previously guessed letters,
write a function that returns True if the newly guessed
letter is legal. If the guess is illegal, print why the guess
is illegal and return False.
'''
def IsLegalGuess(current_guess, letters_guessed):
    if(len(current_guess) > 1):
        print('Please type one character only')
        return False
    if(False == current_guess.isalpha()):
        print('The character you typed is not alphabet')
        return False
    if current_guess in letters_guessed:
        print('You already typed that character')
        return False
    else:
        return True


answer = IsLegalGuess('g', '')
print('IsLegalGuess #1: expected True, got', answer)
answer = IsLegalGuess('g', 'rstle')
print('IsLegalGuess #1: expected True, got', answer)
answer = IsLegalGuess('bb', 'cat')
print('IsLegalGuess #1: expected False, got', answer)
answer = IsLegalGuess('p', 'yzpr')
print('IsLegalGuess #1: expected False, got', answer)
