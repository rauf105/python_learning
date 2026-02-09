class student:
    college  = "abc college" #class attribut same for all object so that we can store that only one time using class attribute

    def __init__(self,name,mark):
        self.name = name #object or instant attribute it is diffrent for all object it take diffrent memory for all object
        self.mark = mark
        print ("new student in database")

    def hello(self):
        print("hello", self.name)

ob1 = student("rauf",97)
print(ob1.name, ob1.mark)

ob2 = student("probal",83)
print(ob2.name, ob2.mark)
print(ob2.college)
ob2.hello()