print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill ? $"))
percentage = int(input("What percentage tip would be like to give? 10, 12, or 15 ? "))
no_persons = int(input("How many people to split the bill? "))
total_amt = total_bill + (percentage / 100) * total_bill
each_amt = round(total_amt / no_persons,2)
print(f"Each person should pay: ${each_amt}")

