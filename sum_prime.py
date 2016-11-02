def sum_prime():
    number=0
    total=2
    count=0
    for num in range(3,10):
        while(count<=2):
            for i in range(2,num):
                if(num%i==0):
                    break
                elif(i==num//2):
                    count=count+1
                    total=total+num
                    print(total)
    return total


answer=sum_prime()
print(answer)

        
        
        
