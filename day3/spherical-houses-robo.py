### Problem ###

'''
--- Part Two ---

The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

    ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
    ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
    ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.

'''

### Code ###

import copy # Used to copy coord array

# Get instructions from elf
instructions = []
with open("directions.txt") as f:
    instructions = list(f.read())

# Create array of santa's coordinates
santaCoords = []

# Track santa's current coordinates
currentSantaCoords = [0,0]
currentRoboCoords  = [0,0]

# Append first house
santaCoords.append([0,0])

# Loop through instructions

usingRobo = False

for x in range(0,len(instructions)):
    # Update coords and add to array
    s = instructions[x]
    if usingRobo:
        if s == "^":
            currentSantaCoords = [currentSantaCoords[0],currentSantaCoords[1]+1]
        elif s == ">":
            currentSantaCoords = [currentSantaCoords[0]+1,currentSantaCoords[1]]
        elif s == "v":
            currentSantaCoords = [currentSantaCoords[0],currentSantaCoords[1]-1]
        elif s == "<":
            currentSantaCoords = [currentSantaCoords[0]-1,currentSantaCoords[1]]

        santaCoords.append(copy.copy(currentSantaCoords))
    else:
        if s == "^":
            currentRoboCoords = [currentRoboCoords[0],currentRoboCoords[1]+1]
        elif s == ">":
            currentRoboCoords = [currentRoboCoords[0]+1,currentRoboCoords[1]]
        elif s == "v":
            currentRoboCoords = [currentRoboCoords[0],currentRoboCoords[1]-1]
        elif s == "<":
            currentRoboCoords = [currentRoboCoords[0]-1,currentRoboCoords[1]]

        santaCoords.append(copy.copy(currentRoboCoords))

    # Toggle between Robot and Santa
    usingRobo = not usingRobo

# Remove duplicates from coords array
visited = []
for i in santaCoords:
    if i not in visited:
        visited.append(i)

# Print visited houses count
visitedCount = len(visited)
print("Visited Houses: " + str(visitedCount))
