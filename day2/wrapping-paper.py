### Problem ###

'''

The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.

Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.

For example:

    A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
    A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.

All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?

'''

### Code ###

# Store instructions in an array
instructions = []

with open("wrapping_instructions.txt") as f:
    instructions = list(f)

wrappingSquareFeet = 0

print "Our instructions array is " + str(instructions)

# Loop through each new command in the array
for x in xrange(0,len(instructions)):
	d = instructions[x]

	# Split line into l,w,h
	dimensionsString = d.split('x')

	# Convert array of strings to array of integers
	dimensionsNumber = [0,0,0]
	for i in xrange(0,len(dimensionsString)):
		dimensionsNumber[i] = int(dimensionsString[i])

	# Put the dimensions in individual variables
	l = dimensionsNumber[0]
	w = dimensionsNumber[1]
	h = dimensionsNumber[2]

	wrappingSquareFeet += 2*l*w + 2*w*h + 2*h*l

	# Determine smallest side
	lowestValue = min(float(s) for s in dimensionsNumber)

	secondLowestArray = dimensionsNumber.remove(lowestValue)

	secondLowestValue = min(float(s) for s in dimensionsNumber)

	print "Our lowest and secondLowest Values were " + str(lowestValue) + ", " + str(secondLowestValue)

	# Multiply second and lowest values to get extra wrapping paper
	extraPaper = lowestValue * secondLowestValue

	# Add to total wrapping paper
	wrappingSquareFeet += extraPaper

print "Total wrapping paper needed in Sq Ft is " + str(wrappingSquareFeet)