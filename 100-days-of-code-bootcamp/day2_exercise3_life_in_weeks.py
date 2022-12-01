# Life in weeks
age = input("What is your current age? ")
age_int = int(age)
years_left = 90 - age_int
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12

message = f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left."
print(message)
