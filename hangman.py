def GetAnswerWithUnderscores(answer):
    mistakes=0
    allowed=6
    new_answer =list(len(answer)* '_')
    while(mistakes<allowed):
        guess=input('Guess the letter?')
        for position, letter in enumerate(answer):
             if letter == guess:
                 new_answer[position] = letter
                 
                 
             :
                 mistakes+ =1
        print(' '.join(new_answer))
        
                
    return new_answer
            
                
answer=GetAnswerWithUnderscores('potato')
print(answer)
