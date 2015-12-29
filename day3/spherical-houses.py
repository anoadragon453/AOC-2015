### Problem ###

'''
--- Day 3: Perfectly Spherical Houses in a Vacuum ---

Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

        > delivers presents to 2 houses: one at the starting location, and one to the east.
        ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
        ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

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
currentCoords = [0,0]

# Append first house
santaCoords.append(currentCoords)

# Loop through instructions

for x in range(0,len(instructions)):
    # Update coords and add to array
    s = instructions[x]
    if s == "^":
        currentCoords = [currentCoords[0],currentCoords[1]+1]
    elif s == ">":
        currentCoords = [currentCoords[0]+1,currentCoords[1]]
    elif s == "v":
        currentCoords = [currentCoords[0],currentCoords[1]-1]
    elif s == "<":
        currentCoords = [currentCoords[0]-1,currentCoords[1]]
    
    santaCoords.append(copy.copy(currentCoords))

# Remove duplicates from coords array
visited = []
for i in santaCoords:
    if i not in visited:
        visited.append(i)

# Print visited houses count
visitedCount = len(visited)
print("Visited Houses: " + str(visitedCount))
