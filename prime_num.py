num=1
palindrome=0
for num in range(1,1000):
    for i in range(2,num):
            if(num%i==0):
                break
            '''while(i<=number-1): #the i function will reach all the way upto 1 below the given number
            if(number%i==0):
                return False
            i=i+1             #if the modulo of number when divided by i is not 0 the i will increase to next number
            if(i==number-1):   #if the number reached all the way upto the given number, then i am assuming that the given number is prime
                return True'''
            if(i==num//2):
                prime=num
                #print(prime)
                prime=str(prime)
                new_prime=prime[::-1]
                new_prime=int(new_prime)
                if(new_prime==int(prime)):
                    hold=new_prime
                    if(hold>palindrome):
                        palindrome=hold
                        continue

print(palindrome)
                
                



