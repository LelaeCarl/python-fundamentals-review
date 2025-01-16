print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
eachPayment = ((tip/100) * bill)/people
round(eachPayment, 2)
finalTotal = round(bill+eachPayment, 2)

print(f"Each person should pay ${eachPayment} tip, and the total"
      f"bill is {finalTotal}")


