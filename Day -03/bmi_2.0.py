height = input("enter your height in m : ")
weight = input("enter your weight in kg : ")

h = float(height)
w = int(weight)

bmi = round(w/(h**2))


if bmi < 18.5:
    print(f"The Bmi is {bmi}, you are slightly underweight.")
elif bmi < 25:
    print(f"The Bmi is {bmi}, you are normal weight.")
elif bmi < 30:
    print(f"The Bmi is {bmi}, you are overweight.")
elif bmi < 35:
    print(f"The Bmi is {bmi}, you are obese.")
else:
    print(f"The Bmi is {bmi}, you are clinically obese.")
