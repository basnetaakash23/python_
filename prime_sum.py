num=1
time=0
sumi=0

while(time<=1000):
    for num in range(2,999999999999):
        for i in range(2,num):
            if(num%i==0):
                break
        
            if(i==num//2):
                prime=num
                sumi=sumi+prime
                time=time+1
    if(time==1000):
        break
                     
                     
                
    
                
print(sumi)


                
                



