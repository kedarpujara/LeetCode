def bulls_and_cows(secret, guess):
	secret_map = []
	for i in range(len(secret)):
		if secret[i]