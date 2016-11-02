def dec_bin(dec):
    mul=1
    no=0
    while dec>0:
        rem=dec%2
        dec=dec//2
        no=no+rem*mul
        mul=mul*10
    return no
dec=int(input("Enter a decimal number " ))
print(dec_bin(dec))
