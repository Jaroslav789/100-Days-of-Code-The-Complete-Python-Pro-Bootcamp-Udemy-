import random

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random()
print(random_float)

number = round(float(random_integer + random_float), 2)
print(number)