sum = 0
for s in ['the', 'quick', 'brown', 'fox', 'jumped']:
    if s.find('o') >= 0:
        sum += 1
print('There are', sum, 'words containing \'o\'')
