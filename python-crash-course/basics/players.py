# Slicing a list

players =['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) # Slice
print(players[1:4]) # Slice
print(players[:4])  # Slice were we omit the firts index
print(players[2:])  # Slice were we omit the second index
print(players[-3:]) # Slice with the last three players on the roster

# Looping through a slice

print("Here are the first three players on my team: ")
for player in players[:3]:
    print(player.title())
