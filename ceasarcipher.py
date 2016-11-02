import string
def ceasarcipher(word):
    
    print(word)
    word=word.rstrip(' ')
    key=3
    if(key>26):
        key=key%26
    
    length=len(word)
    print(length)
    required_word=loops(length,key,word)
    return required_word

def loops(length,key,word):
    i=0
    new_word=''
    new_num=0
    while(i<=(length-1)):
        print(word[i])
        new_num=ord(word[i])+key
        if(new_num>122):
            new_num=96+(new_num-122)
        new_word=new_word+chr(new_num)
        i=i+1

    return new_word

answer=ceasarcipher('mynameisaakash')
print(answer)
answer=ceasarcipher('my name is aakash')
print(answer)

    
