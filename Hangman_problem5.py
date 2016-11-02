'''As the user plays Hangman, the program should ask for a
new letter to guess. This function should prompt the user
for a letter using the 'input' function. If the guess
is not legal (hint: use your IsLegalGuess function), ask again
for a new letter. Only after the user makes a legal guess
should this function return the legal guess.

Example:
1. letters_guessed --> 'abc'
2. Program asks user for a letter
3. User types in 'c'
4. The program should state to only make unique guesses and
   prompt again for a letter
5. Program asks user for a letter
6. User types in 'd'
7. Since this is a legal guess, the function should return 'd'
'''
def GetLegalGuess(letters_guessed):
    guess = input('Guess the letter!')
    if IsLegalGuess(guess,letters_guessed):
        
        return guess
    else:
        print('You made an illegal guess, please type in a character again')
        return GetLegalGuess(letters_guessed)
    

def IsLegalGuess(current_guess, guessed):
    if(len(current_guess) > 1):
        return False
    if not current_guess.isalpha():
        return False
    if current_guess in guessed:
        return False
    else:
        return True

answer = GetLegalGuess('abc')
print(answer)
