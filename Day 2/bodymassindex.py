weight = int(input("enter Your Weight"))
height = int(input("enter Your Hieght"))
bmi = weight / (height * height)
print(bmi)
if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal")
elif bmi < 30:
    print("overweight")
elif bmi < 35:
    print("obese")
else:
    print("extremely obese")