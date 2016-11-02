def Recurse(x):
    if(x%2==0):
        x-=1
    print(x)
    if(x<=1):
        return 1
    return x + Recurse(x-2)

print(Recurse(6))
