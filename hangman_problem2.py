def GetWordSeparatedBySpaces(word):
    ans = ''
    for items in word:
        if(items == word[-1]):
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
