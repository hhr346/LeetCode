'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

 

示例 1：

输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶
示例 2：

输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶

经典的动态规划的问题，可以直接计算，那可以来公式解吗？
状态转移方程是
'''
from typing import List

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2

        out_mem1 = 1
        out_mem2 = 2
        for i in range(3, n+1):
            out_i = out_mem1 + out_mem2
            out_mem1 = out_mem2
            out_mem2 = out_i
        return out_i
