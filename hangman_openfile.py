def read_words():
    open_file = open('C:/python/hangman_english_words','r')
    words_list =[]
    contents = open_file.readlines()
    for i in range(len(contents)):
         words_list.extend(contents[i].split())
    print(words_list)
    
    open_file.close()

read_words()
    
