def reverse_string(word):
    word=word.split()
    index=len(word)-1
    new_list=''
    while(index>=0):
        if(index==0):
            new_list=new_list+word[index]
            index=index-1
        else:
            new_list=new_list+word[index]+' '
            index=index-1
        

    return new_list
    
answer=reverse_string("Hello World")
print(answer)
answer1=reverse_string("Hello CodeEval")
print(answer1)

