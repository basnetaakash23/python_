def GetAnswerWithUnderscores(answer, letters_guessed):
    string = ''
    for chars in answer:
        if chars in letters_guessed:
            string += chars
        else:
            string += '_'
    return string
answer = GetAnswerWithUnderscores('welcome', 'mel')
print('GetAnswerWithUnderscores #1: expected _el__me, got', answer)
answer = GetAnswerWithUnderscores('quick', 'rstlne')
print('GetAnswerWithUnderscores #2: expected _____, got', answer)
