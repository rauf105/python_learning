# print 1 to 100
# i=1
# while i<=100:
#     print(i)
#     i +=1

# print 100 to 1
# i=100
# while i>=1 :
#     print(i)
#     i -=1

#multiplecation table of number n
# x=int(input("enter a number: "))
# i=1
# while i<=10:
#     print(x,"*",i,"=",x*i,"\n")
#     i +=1

#print element of following list using loop
# num=[1,4,9,16,25,36,49,64,81,100]
# i=0
# while i<10:
#     print(num[i])
#     i +=1

#search a number n in this tuple using loop
num=(1,4,9,16,25,36,49,64,81,100)
print(num)
n=int(input("enter a number you want to search: "))
idx=0
while idx < len(num):
    if (num[idx]==n):
        print(n," this number found at index: ",idx)
    idx +=1