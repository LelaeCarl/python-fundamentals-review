import random

#random_int = print(random.randint(3,9))

#randomNo = print(random.random()*10)

randomNo = random.randint(0,1000)
print("Welcome to Heads&Tails\nYour random generated side is:")

if randomNo % 2 == 0:
    print("HEADS")
else:
    print("TAILS")