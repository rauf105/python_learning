#file write
# name = input("What is yout name? ")

# with open("names.txt" , "a") as file:
#     file.write(f"{name}\n")


#read existing file
# with open("names.txt" , "r") as file:
#     lines = file.readlines() #we can not sort hera because it read file line by line and print, so that there is no option for sort
#     #if we want to sort by name than we have to first read all file at onces

# for line in lines:
#     print("hello, ", line.rstrip())

#   read file and sort them

names = []
with open("names.txt" , "r") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")  