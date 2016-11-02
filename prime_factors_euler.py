def primefactors(giv_prime):
    prime=findprimes(giv_prime)
    temp1=0
    if(giv_prime%prime==0):
        temp=prime
        if(temp>temp1):
            temp1=temp

    return temp1

def findprimes(giv_prime):
    for i in range(2,giv_prime//2):
        for x in range(2,i):
            if(i%x==0):
                continue

            elif(x==i//2):
                findprimes(giv_prime)
                return i
            
            


giv_prime=600851475143
answer=primefactors(giv_prime)
print(answer)

    
