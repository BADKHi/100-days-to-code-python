print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
people = int(input("How many people split the bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
tip_decimal = ((tip/100) +1)

final_pay = ((total_bill*tip_decimal) / people)

rounded_final_pay = round(final_pay, 2)
print(f"Each person should pay: ${rounded_final_pay}")