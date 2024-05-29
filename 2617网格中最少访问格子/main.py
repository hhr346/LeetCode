'''
给你一个下标从 0 开始的 m x n 整数矩阵 grid 。你一开始的位置在 左上角 格子 (0, 0) 。
当你在格子 (i, j) 的时候，你可以移动到以下格子之一：
满足 j < k <= grid[i][j] + j 的格子 (i, k) （向右移动），或者
满足 i < k <= grid[i][j] + i 的格子 (k, j) （向下移动）。
请你返回到达 右下角 格子 (m - 1, n - 1) 需要经过的最少移动格子数，如果无法到达右下角格子，请你返回 -1 。

示例 1：
输入：grid = [[3,4,2,1],[4,2,3,1],[2,1,0,0],[2,4,0,0]]
输出：4
解释：上图展示了到达右下角格子经过的 4 个格子。
示例 2：
输入：grid = [[3,4,2,1],[4,2,1,1],[2,1,1,0],[3,4,1,0]]
输出：3
解释：上图展示了到达右下角格子经过的 3 个格子。
示例 3：
输入：grid = [[2,1,0],[1,0,0]]
输出：-1
解释：无法到达右下角格子。

提示：
m == grid.length
n == grid[i].length
1 <= m, n <= 105
1 <= m * n <= 105
0 <= grid[i][j] < m * n
grid[m - 1][n - 1] == 0

感觉就是普通的图搜索算法
根据这个要求是返回最小的路径长，那或许用广度优先算法很好
并且并不需要所有的，而只是最小的，所以我可以舍弃所有后来到达同一个节点的路径，因为之前有更好的来过
'''

from typing import List
from collections import deque
import numpy as np

class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        self.grid = np.array(grid)
        self.line = np.shape(self.grid)[0]
        self.col = np.shape(self.grid)[1]

        outcome = self.bfs()
        return outcome
    
    def bfs(self):
        # Store as [axis_line, axis_col, num]
        queue = deque()
        queue.append([0, 0, 1])
        while queue:
            vertex = queue.popleft()

            if vertex[0]+1 == self.line and vertex[1]+1 == self.col:
                return vertex[2]
            num_jump = self.grid[vertex[0]][vertex[1]]

            # 将访问过的节点赋0，这样我们就可以减少很多可能性
            self.grid[vertex[0]][vertex[1]] = 0

            for i in range(num_jump):
                # 边界检查很重要！
                if vertex[0]+i+1 < self.line:
                    queue.append([vertex[0]+i+1, vertex[1], vertex[2]+1])

                if vertex[1]+i+1 < self.col:
                    queue.append([vertex[0], vertex[1]+i+1, vertex[2]+1])
        # Find nothing
        return -1
