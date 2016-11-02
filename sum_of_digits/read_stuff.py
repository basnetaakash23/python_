def read_stuff():
    total=0
    for line in open("c://users/Aakash Basnet/Documents/python/sum_of_digits/stuff.txt"):
        #print(line)
        line=line.rstrip()
        for digit in line:
            total=total+int(digit)

        print('The total is',total)

read_stuff()
        
    
