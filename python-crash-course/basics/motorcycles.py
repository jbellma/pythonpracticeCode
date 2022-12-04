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

# Removing elements from a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[1]
print(motorcycles)
