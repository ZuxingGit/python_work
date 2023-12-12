players=['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:3])
print(players[:4])
print(players[2:])
# output the last three players on the roster
print(players[-3:])
# with a tird value
print(players[0::2])
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())