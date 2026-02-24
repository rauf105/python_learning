# x, y, z = "hel", "lo wo","rld"
# print(x)
# print(y)
# print(z)

# x = 'awesome'
# def myfunc():
#   global x
#   x = 'fantastic'
# myfunc()
# print('Python is ' + x)

# carname = "Volvo"
# print(carname)

# txt = "Hello World"
# print(txt[0])

# a = 330
# b = 330
# print("A") if a > b else print("=") if a == b else print("B")

day = "bal"
match day:
  case "bal":
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")