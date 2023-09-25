#Question 2: Read python.txt file and print total lines and words in it.
filename="c://sqlite3//python.txt"
line_count=0
word_count=0
with open(filename,"r")as read_file:
    for i in read_file:
        #it count the line
        line_count+=1
        
        list1=i.split()
        #it count the word
        word_count+=len(list1)
        
print(f'Total line:{line_count}')
print(f'Total Word:{word_count}')

