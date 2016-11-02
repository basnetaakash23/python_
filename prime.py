def prime1():
    i=0
    for x in range(3,100):
        for i in range(2,x-1):
            if(x%i==0):
                break
            '''while(i<=number-1): #the i function will reach all the way upto 1 below the given number
            if(number%i==0):
                return False
            i=i+1             #if the modulo of number when divided by i is not 0 the i will increase to next number
            if(i==number-1):   #if the number reached all the way upto the given number, then i am assuming that the given number is prime
                return True'''
            if(i==x//2):
                prime=x
                new_prime=''
                prime=str(prime)
                length=len(prime)-1
                while(length>=0):
                    new_prime=new_prime+prime[length]
                    #print(new_prime)
                    length=length-1
            if(int(new_prime)==prime):
                print(prime)

prime1()

                
                

            
                
