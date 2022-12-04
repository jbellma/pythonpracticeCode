motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Modyfying elements in a list
motorcycles[0] = 'ducati'
print(motorcycles)

# Adding elements to a list
motorcycles.append('honda')
print(motorcycles)

# Adding elements to an empty list
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# Inserting elements into a list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

# Removing elements from a list with del statement
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[1]
print(motorcycles)

# Removing elements from a list with pop() method
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

last_owned = motorcycles.pop()
print(last_owned)
print(f"The last motorcycle I owned was a {last_owned.title()}.")

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

first_owned = motorcycles.pop(0)
print(first_owned)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# Removing an item by value with remove() method
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)
