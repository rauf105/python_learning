def main():
    x = int(input("x is what ? "))
    if is_even(x):
        print("Even")
    else:
        print("odd")

    name = input("what is your name ? ")
    house(name)

def is_even(n):
    return n % 2 ==0

def house(name):
    match name:
        case "rauf":
            print("airport")
        case "probal" | "nahian":
            print("uttara")
        case _:
            print("unknown")
    
main()