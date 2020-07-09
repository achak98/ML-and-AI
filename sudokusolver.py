def isEmpty(a, emptySpaces):
	for row in range(3):
		for col in range(3):
			if(a[row][col] == 0):
				emptySpaces[0] = row
				emptySpaces[1] = col
				return True
	return False

def uRow(a, row, num):
	for i in range(3):
		if(a[row][i] == num):
			return True
	return False

def uCol(a, col, num):
	for i in range(3):
		if(a[i][col] == num):
			return True
	return False

def isSafe(a, row, col, num):

	return not uRow(a, row, num) and not uCol(a, col, num) 

def printSol(a):
	for i in range(3):
		for j in range(3):
			print (a[i][j], end='  ')
		print('\n')

def solv(a):

	emptySpaces = [0, 0]

	if(not isEmpty(a, emptySpaces)):
		return True

	row = emptySpaces[0]
	col = emptySpaces[1]

	for num in range(1, 4):

		if(isSafe(a, row, col, num)):

			a[row][col] = num

			if(solv(a)):
				return True

			a[row][col] = 0
	return False

if __name__ == "__main__":

	grid = [[0 for i in range(3)] for j in range(3)]

	if(solv(grid)):
		printSol(grid)
	else:
		print ("No solution exists")

