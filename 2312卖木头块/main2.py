'''
给你两个整数 m 和 n ，分别表示一块矩形木块的高和宽。同时给你一个二维整数数组 prices ，其中 prices[i] = [hi, wi, pricei] 表示你可以以 pricei 元的价格卖一块高为 hi 宽为 wi 的矩形木块。

每一次操作中，你必须按下述方式之一执行切割操作，以得到两块更小的矩形木块：
沿垂直方向按高度 完全 切割木块，或
沿水平方向按宽度 完全 切割木块
在将一块木块切成若干小木块后，你可以根据 prices 卖木块。你可以卖多块同样尺寸的木块。你不需要将所有小木块都卖出去。
你 不能 旋转切好后木块的高和宽。

请你返回切割一块大小为 m x n 的木块后，能得到的 最多 钱数。
注意你可以切割木块任意次。

示例 1：
输入：m = 3, n = 5, prices = [[1,4,2],[2,2,7],[2,1,3]]
输出：19
解释：上图展示了一个可行的方案。包括：
- 2 块 2 x 2 的小木块，售出 2 * 7 = 14 元。
- 1 块 2 x 1 的小木块，售出 1 * 3 = 3 元。
- 1 块 1 x 4 的小木块，售出 1 * 2 = 2 元。
总共售出 14 + 3 + 2 = 19 元。
19 元是最多能得到的钱数。

示例 2：
输入：m = 4, n = 6, prices = [[3,2,10],[1,4,2],[4,1,3]]
输出：32
解释：上图展示了一个可行的方案。包括：
- 3 块 3 x 2 的小木块，售出 3 * 10 = 30 元。
- 1 块 1 x 4 的小木块，售出 1 * 2 = 2 元。
总共售出 30 + 2 = 32 元。
32 元是最多能得到的钱数。
注意我们不能旋转 1 x 4 的木块来得到 4 x 1 的木块。

提示：
1 <= m, n <= 200
1 <= prices.length <= 2 * 104
prices[i].length == 3
1 <= hi <= m
1 <= wi <= n
1 <= pricei <= 106
所有 (hi, wi) 互不相同 。

想办法优化吧，这个动态规划没那么直接，测试用例太变态了，7k的价格组合

'''
from typing import List
import numpy as np
class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        # 存储重要的变量，就可以在对象里公用，也不用传来传去
        self.prices = prices
        self.solve_o = np.zeros((m+1, n+1), dtype=int)

        # 首先是确定你这个子问题的扩张，应该是两维度同时扩张
        # 对于每一个扩增的维度，都要解决当前的方阵和每个维度扩增一个的可能性
        # 错啦！要考虑所有的情况！
        for i in range(1, m+1):
            for j in range(1, n+1):
                self.updateSolve(i, j)
                print(self.solve_o)
        return self.solve_o[m, n]

    def updateSolve(self, m, n):
        q_x = -1
        q_y = -1
        # 横切一刀，竖着切一刀的结果要分开，只计算一步操作
        for i in range(1, m+1):
            q_x = max(q_x, self.searchPrice(i, n)+self.solve_o[m-i, n])
            
        for j in range(1, n+1):
            q_y = max(q_y, self.searchPrice(m, j)+self.solve_o[m, n-j])
        self.solve_o[m, n] = max(q_x, q_y)
        
        # 一定注意要对已有价格进行更新，这样在查找的时候才可以放心用search来做，而避免两次的查找！或许可以两次查找取最大 取两种情况？不知道官方是怎么说的，理论上递归两次
        # self.prices.append([m, n, self.solve_o[m, n]])
        self.prices.insert(0, [m, n, self.solve_o[m, n]])
        print(f'{m, n} is updated to {max(q_x, q_y)}')

    def searchPrice(self, m, n):
        # 注意！需要查找最大的！！！或者说是直接找最前面的？因为后来的总是更好？
        # 即使输入无重复，后续也可能有更优解
        # 查找的效率太低？
        # price_re = 0
        for price in self.prices:
            if price[0] == m and price[1] == n:
                # price_re = max(price_re, price[2])
                return price[2]
        return 0

if __name__ == '__main__':
    solution = Solution()
    m, n, prices = 3, 5, [[1,4,2],[2,2,7],[2,1,3]]
    m, n, prices = 10, 2, [[2,2,8],[8,2,9],[10,2,8],[2,1,5],[4,1,14],[10,1,28],[5,2,14],[1,1,24],[7,1,5],[3,2,17],[9,2,2],[6,1,5],[3,1,11],[1,2,15],[6,2,3],[9,1,30]]
    answer = solution.sellingWood(m, n, prices)
    print(answer)
