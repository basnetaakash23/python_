def highlydivisible_triangularnumbers():
    
    total=0
    count=0
    count1=0
    for n in range(0,100):
        for x in range(0,n+1):
            total=total+x
            print(total)
            for j in range(1,total+1):
                if(total%j==0):
                    count+=1
                    if(count>count1):
                        count1=count
                        count=0
                        print('The count is',count1)
        #if(count>=500):
            number=total
            print(number)
            break

highlydivisible_triangularnumbers()

        
