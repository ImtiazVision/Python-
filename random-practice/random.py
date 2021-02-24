def nonConstructibleChange(coins):
	coins.sort()

	currentChangeCreated = 0

	for coin in coins:
	    if coin > currentChangeCreated + 1:
		    return currentChangeCreated + 1

	    currentChangeCreated += coin

	return currentChangeCreated + 1

coins = [1,3,5]
nonConstructibleChange(coins)