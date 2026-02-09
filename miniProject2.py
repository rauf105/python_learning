# random password generator

import random
import secrets
import string

pass_length =12
charValue = string.ascii_letters + string.digits + string.punctuation

#way 1
password = ""
for i in range(pass_length):
    password += random.choice(charValue)

print("your random password is: ",password)

password2 = ""
for i in range(pass_length):
    password2 += secrets.choice(charValue)

print("your secrets password is: ",password2)

#way2
password3 = "".join(random.choice(charValue) for i in range(pass_length))

print("Your random way2 password is:", password3)
 