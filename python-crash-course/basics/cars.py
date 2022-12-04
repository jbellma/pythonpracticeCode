# sorting a list permanently with sort() method
cars = ['bmw', 'audi', 'toyota', 'subaru',]
cars.sort()
print(cars)

# sorting a list permanently with sort() method in reverse order
cars = ['bmw', 'audi', 'toyota', 'subaru',]
cars.sort(reverse=True)
print(cars)

# sorting a list temporarily with the sorted() function
cars = ['bmw', 'audi', 'toyota', 'subaru',]

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)
