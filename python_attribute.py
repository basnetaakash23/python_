def f(x):
    f.counter = getattr(f, "counter", 0) + 1
    return "Monty Python"
        

for i in range(2,10):
    f(i)
    
print(f.counter)
