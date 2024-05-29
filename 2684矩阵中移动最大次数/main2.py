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

烦死了，又要优化了，时间太长了？
如果有一个到头了，那么其他的行元素就没必要跑了！
真的是很多奇技淫巧的细节上的优化啊

md 故意设计一个来恶心你，只有最后一个数不对，然后让你每个都遍历到倒数第二个
这里如果用递归的方式穷举所有的路径实际上没有必要，因为重复的路径是不会对最大结果产生影响
所以可以直接省去重复的节点，变成节点遍历，将遍历过的节点设置为0就自动会跳过了，也不需要再重新设置新的数组来判断是否遍历
设置一层屏障，让其无法突破，也没必要突破，都是重复的内容（没必要和重复）
或者可以记录下每个节点的最终长度，让其变成负数，从而获得结果
'''

from typing import List
import numpy as np
import sys
sys.setrecursionlimit(2000)

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        store_moves = []
        self.grid = np.array(grid)
        self.line_len = len(grid)
        self.col_len = len(grid[0])

        for count in range(self.line_len):
            print('Processing ', count)
            # 对每个元素使用广度优先算法进行遍历
            # 算了，用深度优先更方便
            move = self.dfs(count, 0)
            store_moves.append(move)
            if move == self.col_len:
                break
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
                self.grid[search, col+1] = 0
                if out == self.col_len-1:
                    break
            else:
                search_outcome.append(col)
        return max(search_outcome)

solution = Solution()
grid = [[1]]
answer = solution.maxMoves(grid)
print(answer)
