def nonrepeat(word):
    length=len(word)
    index=length-1
    for i in range(0,index):
        for j in range(0,index):
            if(word[i]==word[j]):
                word[i]=word[i]+1
                









nonrepeat('pppqr')
