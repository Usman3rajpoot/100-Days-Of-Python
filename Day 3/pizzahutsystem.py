#Pizza Ordering System
print("welcome In Pizza Hut")
size = input("Enter size of pizza (S/M/L): ")
toppings = input("Enter toppings (Y/N): ")
cheese = input( "Enter cheese (Y/N): ")
if size == "S" or size == "s":
  cost = 15
elif size == "M" or size == "m":
 cost  = 20

else:
  cost = 25
if toppings == "Y" or toppings == "y":
  cost = cost + 2
else:
  cost = cost
if cheese == "Y" or cheese == "y":
  cost = cost + 3
else:
  cost = cost
print("Your total cost is: ", cost)