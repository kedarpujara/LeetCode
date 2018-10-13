Given a list of intervals A and one interval B, find the least
number of intervals from A that can fully cover B.

If cannot find any result, just return 0;

For example:
Given A=[[0,3],[3,4],[4,6],[2,7]] B=[0,6] return 2 since we can use [0,3] [2,7] to cover the B
Given A=[[0,3],[4,7]] B=[0,6] return 0 since we cannot find any interval combination from A to cover the B


def min_intervals(intervals,b):
	intervals.sort(key=lambda x: x[0])
	maxFirst = intervals[0][0]
	minEnd = intervals[0][1]
	num_intervals = 0
	curr_end, curr_max = minEnd, 0
	for i in range(len(intervals)):
		if intervals[i][0] <= curr_end:
			curr_max = intervals[i][1]
		else:
			num_intervals += 1
			curr_end = intervals[i][1]
	return num_intervals



A=[[0,3],[3,4],[4,6],[2,7]]
B=[0,6]
print(min_intervals(A,B))

