n = int(input())

result = 0

visit = [] * n

def isValid():
	

def nqueen(row):
	if row == n:
		result += 1
	else:
		for col in range(n):
			visit[row] = col
			if (isValid()):
				nqueen(row + 1)

nqueen(0)