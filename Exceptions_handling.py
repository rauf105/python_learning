def main():
    x=get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("what is x? "))

        except ValueError:
            print(f"x in not a intger")
            #pass
            
        else:   #after try else will run. 
            return x

main()