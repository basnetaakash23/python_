'''The user wins at Hangman once they've guessed all letters
in the answer word. This function should return True if
the user has won, and False otherwise.
'''
def IsWinner(answer, letters_guessed):
    new_answer = ''
    for list in answer:
        for items in letters_guessed:
            if items in list:
                new_answer = new_answer+items
                break
        if items not in list:
            new_answer+ = '_'
    if(new_answer == answer):
        return True
    else:
        return False


answer = IsWinner('plane', 'ranedlp')
print('IsWinner #1: expected True, got', answer)
answer = IsWinner('plane', 'plan')
print('IsWinner #2: expected False, got', answer)
