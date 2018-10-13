def besttime(a):
	if len(a) <= 1:
		return 0

	profit = [0 for x in range(len(a))]
	max_profit = -12312412412
	for i in range(1,len(a)):
		if a[i]-a[i-1] >= a[i] - a[i-1] + profit[i-1]:
			profit[i] = a[i]-a[i-1]
		else: 
			profit[i] = a[i] - a[i-1] + profit[i-1]
		#print profit[i]
		max_profit = max(max_profit, profit[i])
		# if profit[i] > max_profit:
		# 	max_profit = profit[i]

	return max_profit


a = [7,1,5,3,6,4]
#a = [1,2]
print(besttime(a))