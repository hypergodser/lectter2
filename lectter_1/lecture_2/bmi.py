weight = int (input("Enter your weight in pounds: "))
hight = float (input("Enter your height in inches: "))
bmi = (weight / (hight ** 2  ))
print("Your BMI is: " , format(bmi, "2f"))