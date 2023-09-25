#Program 3: Read Python.txt file and Print unique word with its count.
filename="c://sqlite3//python.txt"
#read the python.txt file
with open(filename,"r")as read_file:
    read=read_file.read()

#split the data of the text file and store in 'word' variable
words=read.split()

#create the empty dictionary to store count 
word_count={}
for word in words:
    word=word.lower()
    word_count[word]=word_count.get(word,0)+1

'''
here word_count[word] is a key for the word_count dictionary
.get(word,0) is use to identify the value of the word key
if it is occur second time than increment by 1
or it occur first time than it is start from 0
'''

for word,count in word_count.items():
    print(f'{word}:{count}')
