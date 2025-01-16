print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

pizza = 0

if size=="S":
    pizza+=15
elif size=="M":
    pizza+=20
elif size=="L":
    pizza+=25
else:
    print("You typed the wrong inputs. ")

if pepperoni == "Y":
    if size == "S":
        pizza +=2
    else:
        pizza+=3


if extra_cheese == "Y":
    pizza +=1


print(f"Your final bill is: ${pizza}.")
