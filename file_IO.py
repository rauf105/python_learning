# read file
# f = open("demo.txt","r")
# #data = f.read() #print hole file at e time
# line1 = f.readline()
# line2 = f.readline()
# print(line1)
# print(line2)
# #print(type(data))
# f.close()

#write file using python
# f = open("demo.txt","w") #overwrite the entire file
# f.write("tomorrow i will learn javascrept in apna college")
# f.close

f = open("demo.txt","a")  #append file
f.write("\nafter that i want to learn reactjs") #add this in exesting file
f.close

# r+, w+, a+