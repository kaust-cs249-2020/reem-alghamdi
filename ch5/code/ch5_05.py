"""
@BY: Reem Alghamdi
@DATE: 02-10-2020
"""
from math import inf


def dp_change(money, coins):
    min_num_coins = [0]
    for m in range(1, money + 1):
        min_num_coins.append(inf)
        for coin in coins:
            if m >= coin:
                if min_num_coins[m-coin] + 1 < min_num_coins[m]:
                    min_num_coins[m] = min_num_coins[m-coin] + 1
    return min_num_coins[money]


if __name__ == "__main__":
    print(dp_change(18182, [14,12,11,10,5,3,1]))
