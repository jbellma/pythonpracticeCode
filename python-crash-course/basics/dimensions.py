#  Using tuples.
# Size of rectangle. Size does not change.

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Looping thrpugh all values in a tuples

for dimension in dimensions:
    print(dimension)

# Writing over a tuple

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
