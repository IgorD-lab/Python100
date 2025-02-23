print("Welcome to the tip calculator.")
bill = float(input("Total bill: "))
people = int(input("Number of people: "))
tip = int(input("What tip percentage: "))

bill_with_tip = round(bill * (1 + tip / 100), 2)
split = round(bill_with_tip / people, 2)
print(f"Total: {bill_with_tip}\nSplit: {split}")