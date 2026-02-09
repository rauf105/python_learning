#concatination
str1="abdur"
str2="rauf"
str3=str1+" "+str2
print(str3)

#string leangth
print(len(str3)) #abdur rauf

#intexing - start with 0
print(str3[3]) #u

#slicing - startindex to endindex, here endindex do not slice
print(len(str3[2:5]))#dur r
print(str3[:7]) #abdur r
print(str3[2:]) #dur rauf

#endswith - check that if the string end with something
print(str3.endswith("uf"))
 
#capitalize - nake first letter capitalize
print(str3.capitalize())

#replace - old, new
print(str3.replace("a","R"))

#find - return valu of index
print(str3.find("u"))

#cout - any word or letter how many time use in this string
print(str3.count("r"))