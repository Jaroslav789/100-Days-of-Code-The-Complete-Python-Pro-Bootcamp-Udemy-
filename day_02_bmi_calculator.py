height = input("What is your height in meters?\n")
weight = input("What is your weight in kilograms?\n")

weight_as_int = int(weight)
height_as_bloat = float(height)

bmi = round(weight_as_int / (height_as_bloat ** 2), 2)
print(f"Your BMI is {bmi}")