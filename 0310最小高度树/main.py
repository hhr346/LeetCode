'''
树是一个无向图，其中任何两个顶点只通过一条路径连接。 换句话说，一个任何没有简单环路的连通图都是一棵树。
给你一棵包含 n 个节点的树，标记为 0 到 n - 1 。给定数字 n 和一个有 n - 1 条无向边的 edges 列表（每一个边都是一对标签），其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间存在一条无向边。
可选择树中任何一个节点作为根。当选择节点 x 作为根节点时，设结果树的高度为 h 。在所有可能的树中，具有最小高度的树（即，min(h)）被称为 最小高度树 。
请你找到所有的 最小高度树 并按 任意顺序 返回它们的根节点标签列表。
树的 高度 是指根节点和叶子节点之间最长向下路径上边的数量。

示例 1：
输入：n = 4, edges = [[1,0],[1,2],[1,3]]
输出：[1]
解释：如图所示，当根是标签为 1 的节点时，树的高度是 1 ，这是唯一的最小高度树。
示例 2：
输入：n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
输出：[3,4]

提示：
1 <= n <= 2 * 104
edges.length == n - 1
0 <= ai, bi < n
ai != bi
所有 (ai, bi) 互不相同
给定的输入 保证 是一棵树，并且 不会有重复的边

最直接的方法尝试一下，就是遍历所有节点，对每个节点作为根来返回最深的深度作为树的高度，最后返回取得最好的结果的几个节点即可
'''
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        depth_list = []
        for i in range(n):
            # 注意要传递一个新的内存，不然就只有一个对象
            edges_now = edges[:]

            print('Processing ', i, edges_now)

            depth = self.findDepth(i, edges_now)
            depth_list.append(depth)
            print('\n')
        
        # 先找最大值，再遍历一次找索引，似乎更直接，否则要对列表进行比较麻烦的处理

        print('depth list is', depth_list)

        min_num = min(depth_list)
        min_idx = []
        # 对每一个节点作为根的情况进行遍历
        for i in range(n):
            if depth_list[i] == min_num:
                # 返回符合最小值的所有的下标
                min_idx.append(i)
        return min_idx

    def findDepth(self, root: int, edges_now):
        depth_list = [1]
        print(edges_now)
        edges_now_cp = edges_now[:]

        for edge in edges_now_cp:
            print(edge)
            depth = 1
            if root == edge[0]:
                # 移掉相应的节点来防止倒退，并且只需要用这一次
                edges_now.remove(edge)
                depth += self.findDepth(edge[1], edges_now)
            elif root == edge[1]:
                edges_now.remove(edge)
                depth += self.findDepth(edge[0], edges_now)
            depth_list.append(depth)
        # 找到最深的一个节点作为高度（最大的里面的最小）
        return max(depth_list)

if __name__ == '__main__':
    solution = Solution()
    n, edges = 4, [[1,0],[1,2],[1,3]]
    n, edges = 6, [[3,0],[3,1],[3,2],[3,4],[5,4]]
    answer = solution.findMinHeightTrees(n, edges)
    print(answer)
