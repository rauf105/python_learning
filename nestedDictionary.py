student={
    "name" : "Abdur rauf",
    "subject" :{           #nested dictionary
        "phy" :97,
        "che" :92,
        "math" :98,
    }
}

print(student) # print all information in dictionary
print(student["subject"]) #print only value of student key
print(student["subject"]["math"]) #print value of math
