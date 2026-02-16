#mode = 'r'
# file = open("demo.txt",mode = 'r')
# read_data = file.read()
# print(read_data)
# file.close()


# file = open("demo.txt",mode = 'r')
# read_data = file.readline()
# print(read_data)
# file.close()


# file = open("demo.txt",mode = 'r')
# read_data = file.readlines()
# print(read_data)
# file.close()


# read---> total data
# readline --> single line(first  line)
# readlines --> total data in list format( list of substrings)


# mode = 'a'
# file = open("demo.txt",mode = 'a')
# write_data = file.write("\nappend operation performed by using mode a")
# file.close()

# file = open("sampledemo.txt",mode = 'a')
# write_data = file.write("\nappend operation performed by using mode a")
# file.close()


# mode = 'w'
# file = open("demo.txt",mode = 'w')
# write_data = file.write("new data performed by using mode w")
# file.close()


# file = open("sample.txt",mode = 'w')
# write_data = file.write("welcome to pythonlife")
# file.close()

# voter_list = ["vaishnavi\n","prasada\n","srikar\n","mukesh\n","rakesh"]
# file = open("demo.txt",mode = 'w')
# write_data = file.writelines(voter_list)
# file.close()



# mode = 'w+'
# file = open("testcase.txt",mode = 'w+')
# write_data = file.write("new data some information \n new data")
# print(file.tell())
# file.seek(0)
# read_data = file.readline()
# print(read_data)
# file.close()

# information

#rename 
# import os
# fn = "testcase.txt"
# nn = "demo.txt"
# os.rename(fn,nn)


# import os
# os.remove("demo.txt")

# file = open("C:\Users\dddev\OneDrive\Desktop\hello.txt", mode = 'r') #not working
# file = open("C:\\Users\\dddev\\OneDrive\\Desktop\\hello.txt", mode='r') #it is working
# file = open("C:/Users/dddev/OneDrive/Desktop/hello.txt", mode='r') #it is working
# read_data = file.read()
# print(read_data)
# file.close()


file = open("C:\\Users\\dddev\\OneDrive\\Desktop\\python123456789.txt",mode = 'a') #it is working
write_data = file.write("\nwelcome to pythonlife filehandlingconcept")
file.close()





# import csv


# file = open("newfile.csv",mode = 'w')
# file.close()



# pypdf2
# gtts

