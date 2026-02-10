import random

coin = random.choice(["HEAD", "TAILS"])
num = random.randint(1,10)
card = ["jack", "queen", "king"]
random.shuffle(card)
print(card)