#welcome
print("Welcome to the tip calculator!")

#input date, str(data type)->error, use float or int
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
people = int(input("Hot many people to split the bill?"))

#calculator
bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill_with_tip / people
final_amount = round(bill_per_person, 2)

#print
print(f"Each person should pay: ${final_amount}")