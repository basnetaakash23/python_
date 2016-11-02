
def sum_prime_numbers():
    
    sum=2
    for num in range(3,2000000,2):
        for x in range(2,num):
            if(num%x==0):
                break
            if(num<x*x):
                prime=num
                #print(prime)
                sum=sum+prime
                break
    return sum

ans=sum_prime_numbers()
print(ans)

        
        
    
