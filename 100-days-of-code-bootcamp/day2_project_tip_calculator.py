# Tip calculator
print("Welcome to the tip calculator")

bill = float(input("What was the total bill? "))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))

split = (bill + ((tip/100) * bill)) / num_people
final_split = round(split,2)

message = f" Each person should pay: {final_split}"
print(message)
