def DoSomethingFantastic(word,something):
    if something:
        index=0

    else:
        index=1
    answer=''
    while index<len(word):
        answer=answer+word[index]
        index+=2
    return answer

answer=DoSomethingFantastic('hungary',True)
print(answer)
answer=DoSomethingFantastic('',false)
print(answer)
answer=DoSomethingFantastic('s',False)
print(answer)
answer=DoSomethingFantastic('hungary',False)
print(answer)
