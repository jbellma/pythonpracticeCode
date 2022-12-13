# Accessing values in a dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just have earned {new_points} points!")

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

# Adding key-value pairs to the dictionary
alien_0['x_postion'] = 0
alien_0['y_postion'] = 25

print(alien_0)

# Starting with an empty dictionary
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# Modifying values in a dictionary
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")
