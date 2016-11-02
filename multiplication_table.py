def multiplication_table():
    
    new_list=[]
    for i in range(1,13):
        for j in range(1,11):
            new_list.append(i*j)
        print(new_list)
        del new_list[:]

multiplication_table()


    
        
