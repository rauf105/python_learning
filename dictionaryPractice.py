'''wap to enter marks of 3 subject from the User and store them in a dictionary. start with
an empty dictionary and add one by one. use subject name as key and mark as value.'''
dictionary={}
x=int(input("mark of phy: "))
dictionary.update({"phy":x})

x=int(input("mark of math: "))
dictionary.update({"math":x})

x=int(input("mark of che: "))
dictionary.update({"che":x})

print(dictionary)