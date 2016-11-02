import time
start = time.time()

def pythagorean_triplet():

    for a in range(1,501):
        for b in range(a+1,501):
            c=1000-a-b
            if(a**2+b**2==c**2):
                '''print("a is",a)
                print("b is",b)
                print("c is",c)'''
                return a*b*c
                   
    

ans=pythagorean_triplet()
print(ans)
print("Elapsed Time:", (time.time() - start))

            
        
