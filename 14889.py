n = int(input())

scores = []
visit = [[] * n for _ in range(n)]
for i in range(n):
	for j in range(j):
		if (i < j):
			visit[i][j] = 1

def visitCheck(i, j, visit):
	for k in range(n):
		visit[i][k] = 0
		visit[k][j] = 0

def recur(i, j, temp):
	temp 

for i in range(n):
	scores.append(tuple(map(int, input().split())))
for i in range(n):
	for j in range(j):
		if (i < j):
			scores[i][j] += scores[j][i]
		else:
			scores[i][j] = 0
summation = 0
for i in range(n):
	summation += sum(scores[i])

result = summation
for i in range(n):
	for j in range(j):
		if (i < j):
			if (visit[i][j] == 1):





