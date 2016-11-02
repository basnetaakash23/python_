def GetSum(nums):
    """Sum a sequence of numbers."""
    sum = 0
    for num in nums:
        sum += num
    return sum

nums = []

while True:
    snum = input('Enter number: ')
    if len(snum) == 0:
        break
    
    nums += [int(snum)]

print('The sum of', nums, 'is', GetSum(nums))



