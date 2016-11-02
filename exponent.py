def exponentiation(base,exponent):
    n=1
    total=1
    while n<=exponent:
        total=total*base
        n=n+1

    return total

answer=exponentiation(2,4)
print(answer)
