list=[1, 2, 3, 4, 3, 2, 1]
listCopy=list.copy() #make a copy
listCopy.reverse() #than reverse it
print("original: ",list)
print("reverse: ",listCopy)
if(list == listCopy): #at the end compare both
    print("both are palindrome")
else:
    print("not palindrome")