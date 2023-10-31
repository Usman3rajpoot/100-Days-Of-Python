# CALCULATER
print("Welcome To Tip Calculater")
bill = float(input("Enter Your Bill Amount:$"))
tip = int(input("Enter Your Tip Percentage\n 1.10%: \n 2.20% : \n Enter Percentage:"))
people = int(input("Enter Your Number Of People:"))
total = bill + (bill * tip / 100)
print("Each Person Should Pay:", total / people)