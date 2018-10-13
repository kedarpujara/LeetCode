def cutoff(forest):
	visited = [[False for y in range(len(forest))] for x in range(len(forest[0]))]
	print visited
	
	canVisit = True
	i = 0
	j = 0
	while canVisit:
		if visited[i][j] == False:
			visited[i][j] = True

		else:
			#skip to another one 

	#for tree in forest:
def get_min(i,j,forest):
	val1 = val2 = val3 = val4 = val5 = 0
	min_val = 0
	if forest[i-1][j]:
		if visited[i-1][j] == False and forest[i-1][j] != 0:
			val1 = forest[i-1][j]
	if forest[i][j-1]:
		if visited[i][j-1] == False and forest[i][j-1] != 0:
			val2 = forest[i][j-1]
	if forest[i][j+1]:
		if visited[i][j+1] == False and forest[i][j+1] != 0:
			val3 = forest[i][j+1]
	if forest[i+1][j]:
		if visited[i+1][j] == False and forest[i+1][j] != 0:
			val4 = forest[i+1][j]	
	if forest[i+1][j+1]:
		if visited[i+1][j+1] == False and forest[i+1][j+1] != 0:
			val5 = forest[i+1][j+1]

forest = [
 [1,2,3],
 [0,0,4],
 [7,6,5]
]

print(cutoff(forest))