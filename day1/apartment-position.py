### Problem ###
'''
Part 2

Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1). The first character in the instructions has position 1, the second character has position 2, and so on.

For example:

    ) causes him to enter the basement at character position 1.
    ()()) causes him to enter the basement at character position 5.

What is the position of the character that causes Santa to first enter the basement?

'''

### Code ###

# Get input instructions
instructions = raw_input('Instructions: ')

# Variable to keep track of which floor Santa is on
floor = 0

for x in xrange(0,len(instructions)):
	# Get char at index 'x'
	s = instructions[x]

	# Print and return when Santa reaches the 'basement'
	if floor <= -1:
		print x
		break

	# Test for parenthesis
	if s == '(':
		floor += 1
	elif s == ')':
		floor -= 1



# Print out final floor count
print floor
