# factorial of a number n using for loop

n=int(input("give me a number: "))
num=range(1,n+1)
facto=1
for el in num:
    facto *= el
print("factorial of n is : ",facto)