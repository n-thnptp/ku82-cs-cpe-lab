weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))

bmi = weight / (height**2)

print(f"BMI is {bmi:.1f}")

if bmi < 18.5:
    print("Underweight")
elif bmi <= 18.5 or bmi < 25:
    print("Normal weight")
elif bmi <= 25.0 or bmi < 30.0:
    print("Overweight")
elif bmi > 30.0:
    print("Obesity")
else:
    print("Error")