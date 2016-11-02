'''-----------------------------------------------------------
Exercise 1:
Throughout play of Hangman, your program will display to the user
what letters in a word they've uncovered and what's still hidden.
This function should return back a new string where all hidden
letters are converted to an underscore.

Example:
answer --> 'welcome'
letters_guessed --> 'mel'
Return value --> '_el__me'

Notice that even though the user guessed 'e' once, all
occurrences of 'e' in the answer word are revealed to the user.
'''

def GetAnswerWithUnderscores(answer, letters_guessed):
    new_answer = ''
    for list in answer:              #list as variable and will loop in individual elements of 'answer'
        if list in letters_guessed:
                new_answer = new_answer+list
        else:
            new_answer += '_'
                
    return new_answer
            
                
answer = GetAnswerWithUnderscores('welcome', 'mel')
print('GetAnswerWithUnderscores #1: expected _el__me, got', answer)
answer = GetAnswerWithUnderscores('quick', 'rstlne')
print('GetAnswerWithUnderscores #2: expected _____, got', answer)



'''-----------------------------------------------------------
Exercise 2:
Take a look again at the Exercise 1's example. Notice how in some
fonts, it's difficult to visually differentiate between a single
underscore and two underscores next to each other? Write a function
that takes in a string and returns a new string with a single space
between each letter.
'''

def GetWordSeparatedBySpaces(word):
    ans = ''
    for items in word:
        if(items == word[-1]):    #if last letter of the word
            ans = ans + items
        else:
            ans = ans + items + ' '
        
    return ans


answer = GetWordSeparatedBySpaces(' plane')
print('GetWordSeparatedBySpaces #1: expected p l a n e, got', answer)
answer = GetWordSeparatedBySpaces('to')
# Don't worry about the hasattr function, the if statement, or what they
# do: it's not required for this Hangman assignment.
if hasattr(answer, 'strip') and answer.strip() == answer:
    text = 'PASS'
else:
    text = 'FAIL'
print('GetWordSeparatedBySpaces #2: expected no spaces at the beginning or end,', text)




'''------------------------------------------------------
Exercise 3:
The user wins at Hangman once they've guessed all letters
in the answer word. This function should return True if
the user has won, and False otherwise.
'''


def IsWinner(answer, letters_guessed):

    new_answer = ''
    for list in answer:
        if list in letters_guessed:
                new_answer = new_answer+list
                
        else:
            new_answer += '_'               #basically do the same as in question 1 
            
    if(new_answer == answer):
        return True

    else:
        return False


answer = IsWinner('plane', 'ranedlp')
print('IsWinner #1: expected True, got', answer)
answer = IsWinner('plane', 'plan')
print('IsWinner #2: expected False, got', answer)




'''------------------------------------------------------
Exercise 4:
When playing Hangman, a user should be guessing one unique
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
    
    if not current_guess.isalpha():
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




'''-----------------------------------------------------------
Exercise 5:
As the user plays Hangman, the program should ask for a
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
    
    guess = input('Guess the letter!')   #variable guess will contain the guessed character
    
    if IsLegalGuess(guess,letters_guessed): #calls function in question number 4
        return guess
    
    else:
        print('You made an illegal guess, please type in a character again')
        return GetLegalGuess(letters_guessed)
    
answer = GetLegalGuess('abc')
print(answer)


'''-----------------------------------------------------------
Exercise 6:
If the answer is 'welcome' and the user guesses 'c', this
helps the user win at Hangman. Write a function that returns
True if the user's guess reveals a letter in the answer, or False
if not. This function can assume the user's guess is legal.
'''


def IsGuessRevealing(answer, legal_letter_guess):
    
    if legal_letter_guess in answer:  #I assumed that the user would input only legal guess 
        return True
    
    else:
        return False


answer = IsGuessRevealing('welcome', 'c')
print('IsGuessRevealing #1: expected True, got', answer)
answer = IsGuessRevealing('quick', 'z')
print('IsGuessRevealing #1: expected False, got', answer)

