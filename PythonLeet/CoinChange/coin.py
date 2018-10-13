def num_coins(n):
	total = 0
	n = int(n * 100)
	coins = [1,5,10,25]
	permutations(n,0,total, coins)
	return total



def permutations(n, curr, total, coins):
	print(curr)
	if curr == n:
		total += 1
		print("here")
		print(total)
	elif curr > n:
		return 
	else:
		for i in range(len(coins)):
			curr += coins[i]
			permutations(n,curr, total, coins)
			curr -= coins[i]

		
		

print(num_coins(0.05))
