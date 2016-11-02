def isPrime(number):

    for n in range (2,number):
        if number%n == 0:
            return False
    return True

result = 2

for k in range (3,2000000,2):
    if isPrime(k):
        result += k
        #print(result,"     ",k)

print("The total is" ,result)
