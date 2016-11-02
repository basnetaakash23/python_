x=0
list=''
import string
for i in range(1,10):
    for j in range(0,i):
        x=x+1
        #print(str(x))
        list=list+str(x)
    print(list)
    list=''
        
    
