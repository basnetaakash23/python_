def reverse_string(lst):
    list1 = []
    x=len(lst)-1
    j=0
    while(x>=0):
        temp = lst[x]
        list1.append(temp)
        x = x-1
        

    print(list1)

lst = [0,1,2,3,4,5]
reverse_string(lst)
