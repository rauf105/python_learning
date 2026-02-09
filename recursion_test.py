def show(a):
    if(a == 0):     #condition to stop repeted call function
        return
    print(a, end=" ")    #work perform
    show(a-1)   #updated function called
show(10)