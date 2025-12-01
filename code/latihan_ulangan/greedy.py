def greedyAlgorithm(coins, amount):
    coins.sort(reverse=True)

    change = {}
    for coin in coins:
        if amount <= 0:
            break
        num_coins = amount // coin
        if num_coins > 0:
            change[coin] = num_coins
            amount -= coin * num_coins

    if amount > 0:
        return "Change cannot be made with the given coin denominations."

    return change

coin = [100, 50, 20, 10, 5, 2, 1]
amount = 289
print(greedyAlgorithm(coin, amount))