def sort_numbers(s):
    for i in range(1, len(s)):
        val = s[i]
        j = i - 1
        while (j >= 0) and (s[j] > val):
            s[j+1] = s[j]
            j = j - 1
        s[j+1] = val
    print(s)

def main():
    x = [5,4,3,2,1]
    sort_numbers(x)
    
