'''
给你一个下标从 0 开始、大小为 m x n 的矩阵 grid ，矩阵由若干 正 整数组成。
你可以从矩阵第一列中的 任一 单元格出发，按以下方式遍历 grid ：
从单元格 (row, col) 可以移动到 (row - 1, col + 1)、(row, col + 1) 和 (row + 1, col + 1) 三个单元格中任一满足值 严格 大于当前单元格的单元格。
返回你在矩阵中能够 移动 的 最大 次数。

示例 1：
输入：grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
输出：3
解释：可以从单元格 (0, 0) 开始并且按下面的路径移动：
- (0, 0) -> (0, 1).
- (0, 1) -> (1, 2).
- (1, 2) -> (2, 3).
可以证明这是能够移动的最大次数。

示例 2：
输入：grid = [[3,2,4],[2,1,9],[1,1,7]]
输出：0
解释：从第一列的任一单元格开始都无法移动。
 
提示：
m == grid.length
n == grid[i].length
2 <= m, n <= 1000
4 <= m * n <= 105
1 <= grid[i][j] <= 106

感觉就是用图搜索算法遍历以下就行了？每个扩展有限，所以用广度优先算法吧
这些需要根据具体数据结构来设计的算法，掌握思想然后去直接设计不混乱是最好的
不对，感觉更像是树呐，不过节点之间有公用罢了
写个遍历过程描述罢了，也不难 也没有思维挑战和实现挑战，但是要优化就难了
先搭好框架然后填充就行了，有个思想指导，但不是空洞的，而是实际的，细节依然重要

比如递归实际上和数学归纳法一致
聪明但基本不学习 不努力？
'''

from typing import List
import numpy as np

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        store_moves = []
        self.grid = np.array(grid)
        self.line_len = len(grid)
        self.col_len = len(grid[0])

        for count in range(self.line_len):
            # 对每个元素使用广度优先算法进行遍历
            # 算了，用深度优先更方便
            move = self.dfs(count, 0)
            store_moves.append(move)
        return max(store_moves)

    def dfs(self, line, col):
        if col == self.col_len-1:
            return col

        if line == 0:
            line_search = [0, 1]
        elif line == self.line_len-1:
            line_search = [line-1, line]
        else:
            line_search = [line-1, line, line+1]
        
        search_outcome = []
        for search in line_search:
            if self.grid[search, col+1] > self.grid[line, col]:
                out = self.dfs(search, col+1)
                search_outcome.append(out)
            else:
                search_outcome.append(col)
        return max(search_outcome)
