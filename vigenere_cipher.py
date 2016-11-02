def VigenereCipher():
    sentence='zzzz'
    sentence=sentence.lower()
    sentence="".join(sentence.split())
    sentence=list(sentence)
    length_sentence = len(sentence)
    key='b'
    key=key.lower()
    key=list(key)
    length_key=len(key)
    expand_key = (length_sentence//length_key) + 1
    new_key =key * expand_key
    
    new_sentence=''
    
    for word in range(0,length_sentence):
        shift_key = ord(sentence[word])+(ord(new_key[word])-96)
        print(shift_key)
        
        if(shift_key > 122):
            shift = shift_key-122
            change = 122 - ord(sentence[word])
            new_shift = shift - change
            shift_key = (ord('a') + new_shift)-1
            new_sentence=new_sentence+chr(shift_key)

        else:
            new_sentence=new_sentence+chr(shift_key)

    print(new_sentence)
    

        
            

            
            
                                                    
        
    
















VigenereCipher()
