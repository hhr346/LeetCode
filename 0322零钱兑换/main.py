'''
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
你可以认为每种硬币的数量是无限的。

示例 1：
输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1
示例 2：
输入：coins = [2], amount = 3
输出：-1
示例 3：
输入：coins = [1], amount = 0
输出：0

提示：
1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104

第一反应是贪心，但是估计不太行，因为需要恰好组成总金额，所以估计会有特殊情况导致不行
那就试试看贪心加上栈的结构，新压入的都不行就弹出一个，然后再重来，
从枚举的角度看最多也是用最小金额来选择，那就是可以每一步都进行一个分支，从最大金额开始选择用或者不用
'''

from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        # 排序之后找到最大的塞进去
        coins = sorted(coins)
        combi = [coins[-1]]
        index_last = len(coins)-1

        while combi:
            sum_all = sum(combi)
            if sum_all == amount:
                return len(combi)
            elif sum_all < amount:
                combi.append(coins[index_last])
            else:
                # 塞进来的太多了必须要弹出
                combi.pop()
                # 进行最后一个的降级替代
                if index_last > 0:
                    index_last -= 1
                    combi.append(coins[index_last])

                # 已经是最小的那个了，那就需要再对下一个下刀了，同时更新（这个逻辑写麻烦了）
                else:
                    # 已经空了，越界的问题是需要格外注意的
                    if len(combi) == 0:
                        break
                    popcorn = combi.pop()
                    if coins.index(popcorn) > 0:
                        index_last = coins.index(popcorn)-1
                    else:
                        break
        return -1
