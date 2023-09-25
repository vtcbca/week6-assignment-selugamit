#Program 5: Read Python.txt file. Convert it into upper case and write into another file "Python_Upper.txt"
filename="c://sqlite3//python.txt"
upper_file="c://sqlite3//python_upper.txt"

with open(filename,"r")as read_file,open(upper_file,"w")as write_file:
    read=read_file.read()
    #content of python.txt file is save in read
    for i in read:
        data2=i.upper()
        write_file.write(data2)
    print("Success")

#read the upper file
with open(upper_file,"r")as read_file:
    read=read_file.read()
    for i in read:
        print(i,end="")
