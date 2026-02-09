num=(1,2,4,5,2,1,4,)
x = 4
idx=0
for value in num:
    idx +=1
    if(value == x):
        print("value 4 found at index",idx)
        break
else:
    print("end iteration")