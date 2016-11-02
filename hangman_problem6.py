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
