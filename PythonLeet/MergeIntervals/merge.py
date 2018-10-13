def merge_intervals(interval):
	interval.sort()
	curr_min = interval[0][0]
	curr_max = interval[0][1]
	intervals = []
	i = 1
	while i < len(interval):
		if interval[i][0] <= curr_max:
			if interval[i][1] > curr_max:
				curr_max = interval[i][1]
		else:
			intervals.append([curr_min, curr_max])
			curr_min = interval[i][0]
			curr_max = interval[i][1]			
		i += 1
		if i == len(interval):
			intervals.append([curr_min, curr_max])
	return intervals

a1 = [[1,3],[2,6],[8,10],[15,18]]
a2 = [[1,4], [4,5]]
print(merge_intervals(a1))
