def Printer(word):
    print(word)
    index=0
    while index<len(word):
        char=word[index]
        index+=1
        if char=='G':
            print('Stop')
            break
        if char=='P':
            continue
            print('Continuing')

        if char=='S':
            print('Noope')
            return
        print(char)

    print('End')

Printer('GAP')
Printer('APED')
Printer('WE')
Printer('CAST')
