# find the factorial of n using funclion. n is the parameter
def factorial(a):
    fact=1
    for el in range(1,a+1):
        fact *=el
    print(fact)

factorial(5)
factorial(7)


#write a function to convert usd to bd taka
def usdTobdt (a):
    bdt = a*130
    print("USD:",a," = BDT:",bdt)

usdTobdt(1)
usdTobdt(5)

#odd even checker function
def cheacker(n):
    if(n%2 == 0):
        print(n," even number")
    else:
        print(n," odd number")

cheacker(9)
cheacker(10) 