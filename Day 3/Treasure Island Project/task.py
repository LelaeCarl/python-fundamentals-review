print(r'''
*******************************************************************************
 .---.
             (_,/\ \
            (`a a(  )
            ) \=  ) (
           (.--' '--.)
           / (_\_/_) \
          | / \   / \ |
           \\ / . \ //
            \/\___/\/
            |  \_/  |
             \  /  /
              \/  /
               ( (
               |\ \
         jgs   | \ \
              /_Y/_Y
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("You are at a crossroads. Where do you wanna go, left or right?").lower()

if direction == "left":
    decision = input('You\'ve arrived at a lake, and need to get to the island on the other side. '
          'Type "swim" to swim or "wait" to wait for a boat\n').lower()
    if decision == "wait":
        door = input("You've made it. You've arrived at a house  with three doors:"
                     "Red, Blue and Yellow. Which one do you wanna open?\n")

        if door == "red":
            print("Burnt by fire, game over.")
        elif door == "yellow":
            print("Treasure is here. You win")
        elif door == "blue":
            print("Eaten by beasts, game over.")
        else:
            print("Door doesn't exist. Game over")



    else:
        print("You got attacked by Aquaman.")

else:
    print("Game over. You fell into a hole")




