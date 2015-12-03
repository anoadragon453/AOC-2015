### Problem ###

'''

--- Part Two ---

The elves are also running low on ribbon. Ribbon is all the same width, so they only have to worry about the length they need to order, which they would again like to be exact.

The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.

For example:

    A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.
    A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14 feet.

How many total feet of ribbon should they order?


'''

### Code ###

# Store instructions in an array
instructions = []

with open("wrapping_instructions.txt") as f:
    instructions = list(f)

ribbonLength = 0

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

	# Calculate volume of rectangle
	ribbonLength += l*w*h
	print "L: " + str(l) + ", W: " + str(w) + ", H: " + str(h)
	print "Volume is " + str(l*w*h)

	# Determine smallest side
	lowestValue = min(float(s) for s in dimensionsNumber)

	secondLowestArray = dimensionsNumber.remove(lowestValue)

	secondLowestValue = min(float(s) for s in dimensionsNumber)

	print "Our lowest and secondLowest Values were " + str(lowestValue) + ", " + str(secondLowestValue)

	# Multiply second and lowest values to get ribbon length
	ribbonPerimeter = 2.0 * (lowestValue + secondLowestValue)

	print "\nThus our rP is " + str(ribbonPerimeter) + "\n"

	# Add to total ribbon length
	ribbonLength += ribbonPerimeter

print "Total ribbon length needed in Ft is " + str(ribbonLength)