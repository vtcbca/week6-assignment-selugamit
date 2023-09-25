#Following is reverses all words of text file
file="c://sqlite3//python.txt"
reverse_file="c://sqlite3//reverse_python.txt"
with open(file,"r")as read_file,open(reverse_file,"w",newline="")as write_file:
    r=read_file.read()
    data=r[::-1]
    write_file.writelines(data)

with open(reverse_file,"r")as read_fi:
    read_f=read_fi.read()
    print('\nPrint Reverse of a word in a text file\n')
    print()
    for i in read_f:
        print(i,end="")
        
#optional
#folling is reverses only lines
with open(file,"r")as read_file,open(reverse_file,"w",newline="")as write_file:
    r1=read_file.readlines()
    data1=r1[::-1]
    write_file.writelines(data1)

with open(reverse_file,"r")as read_fi:
    read_f=read_fi.read()
    print()
    print('\nprint Reverse of a line in a text file\n')
    for i in read_f:
        print(i,end="")        
