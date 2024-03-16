import time
from collections import defaultdict


def with_timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Час виконання: {end_time - start_time} секунд")
        return result
    return wrapper


@with_timer
def find_coins_greedy(amount, coins):
    if amount <= 0:
        return {}

    sorted_coins = sorted(coins, reverse=True)
    greedy_dict = defaultdict(int)

    for coin in sorted_coins:
        while amount >= coin:
            greedy_dict[coin] += 1
            amount -= coin

    return dict(greedy_dict)


@with_timer
def find_min_coins(amount, coins):
    if amount <= 0:
        return {}

    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    prev = [-1] * (amount + 1)

    for i in range(1, amount + 1):
        for j, coin in enumerate(coins):
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                prev[i] = j

    coin_count = {}
    current = amount
    while current > 0:
        if current < 0 or prev[current] == -1:
            return "Неможливо сформувати дану суму з вказаних монет."
        coin = coins[prev[current]]
        if coin in coin_count:
            coin_count[coin] += 1
        else:
            coin_count[coin] = 1
        current -= coin

    return coin_count


if __name__ == '__main__':
    coins = [150, 50, 25, 10, 5, 2, 1, 2000, 10000]
    print(find_coins_greedy(87654334, coins))
    print(find_min_coins(87654334, coins))