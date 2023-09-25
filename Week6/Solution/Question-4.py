#Programe 4:Read Python.txt file and Print largest and smallest word from it.
filename="c://sqlite3//python.txt"
with open(filename,"r")as read_file:
    read=read_file.read()

#it convert into the list and store into words
words=read.split()
#create largest_word and smallest_word
largest_word=""
smallest_word=None

for word in words:
    word = word.strip('.,!?').lower()
    #removes the punctuation using strip() method
    #strip() method is use to remove 
    if smallest_word is None:
        smallest_word=word

    #if length of word is grater than largest_word than save into the largest_word
    #otherwise goto the elif part
    if len(word)>len(largest_word):
        largest_word=word
    #same if the length of word is small than smallest_word than save into the smallest_word
    elif len(word)<len(smallest_word):
        smallest_word=word

#print the result
print(f'Larg word:{largest_word}')
print(f'Small word:{smallest_word}')
