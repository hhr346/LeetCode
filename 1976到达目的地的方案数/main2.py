'''
你在一个城市里，城市由 n 个路口组成，路口编号为 0 到 n - 1 ，某些路口之间有 双向 道路。输入保证你可以从任意路口出发到达其他任意路口，且任意两个路口之间最多有一条路。

给你一个整数 n 和二维整数数组 roads ，其中 roads[i] = [ui, vi, timei] 表示在路口 ui 和 vi 之间有一条需要花费 timei 时间才能通过的道路。你想知道花费 最少时间 从路口 0 出发到达路口 n - 1 的方案数。

请返回花费 最少时间 到达目的地的 路径数目 。由于答案可能很大，将结果对 10^9 + 7 取余 后返回。

输入：n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
输出：4
解释：从路口 0 出发到路口 6 花费的最少时间是 7 分钟。
四条花费 7 分钟的路径分别为：
- 0 ➝ 6
- 0 ➝ 4 ➝ 6
- 0 ➝ 1 ➝ 2 ➝ 5 ➝ 6
- 0 ➝ 1 ➝ 3 ➝ 5 ➝ 6

示例 2：
输入：n = 2, roads = [[1,0,10]]
输出：1
解释：只有一条从路口 0 到路口 1 的路，花费 10 分钟。
 

提示：
1 <= n <= 200
n - 1 <= roads.length <= n * (n - 1) / 2
roads[i].length == 3
0 <= ui, vi <= n - 1
1 <= timei <= 109
ui != vi
任意两个路口之间至多有一条路。
从任意路口出发，你能够到达其他任意路口。

The first one is OOM when the roads are too much, so we need to cut down unnecessary stuff
use dfs to get a single path, then we can throw away anyone which is greater than that
IF it's deep, use bfs
IF it's wide, use dfs
'''
from typing import List
from collections import deque

def bfs(graph, start, end):
    queue = deque([(start, [start], 0)])
    paths = []
    while queue:
        vertex, path, price = queue.popleft()
        if vertex == end:
            paths.append((path, price))
        else:
            for neighbor, cost in graph[vertex]:
                if neighbor not in path:
                    queue.append((neighbor, path + [neighbor], price + cost))
    print(paths)

def dfs(graph, start, end, path=None, price=None):
    if path is None:
        path = []
        price = 0
    path.append(start)
    if start == end:
        return path, price
    for neighbor, cost in graph[start]:
        if neighbor not in path:
            price += cost
            new_path, price = dfs(graph, neighbor, end, path, price)
            if new_path:
                return new_path, price

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # First create the adjacency matrix
        set = {}
        for vertex in range(n):
            set[vertex] = []
            for path in roads:
                if path[0] == vertex:
                    set[vertex].append([path[1], path[2]])
                elif path[1] == vertex:
                    set[vertex].append([path[0], path[2]])
                # print(vertex)
                # print(set)

        paths = dfs(set, 0, n-1)
        paths_sorted = sorted(paths, key=lambda x:x[1])
        print(paths_sorted)
        num_least = sum(1 for path in paths_sorted if path[1]==paths[0][1])
        print(num_least)
        return num_least

if __name__ == '__main__':
    solution = Solution()
    solution.countPaths(7, [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]])
    solution.countPaths(2, [[0,1,10]])
    solution.countPaths(18, [[0,1,3972],[2,1,1762],[3,1,4374],[0,3,8346],[3,2,2612],[4,0,6786],[5,4,1420],[2,6,7459],[1,6,9221],[6,3,4847],[5,6,4987],[7,0,14609],[7,1,10637],[2,7,8875],[7,6,1416],[7,5,6403],[7,3,6263],[4,7,7823],[5,8,10184],[8,1,14418],[8,4,11604],[7,8,3781],[8,2,12656],[8,0,18390],[5,9,15094],[7,9,8691],[9,6,10107],[9,1,19328],[9,4,16514],[9,2,17566],[9,0,23300],[8,9,4910],[9,3,14954],[4,10,26060],[2,10,27112],[10,1,28874],[8,10,14456],[3,10,24500],[5,10,24640],[10,6,19653],[10,0,32846],[10,9,9546],[10,7,18237],[11,7,21726],[11,2,30601],[4,11,29549],[11,0,36335],[10,11,3489],[6,11,23142],[3,11,27989],[11,1,32363],[11,8,17945],[9,11,13035],[5,11,28129],[2,12,33902],[5,12,31430],[6,12,26443],[4,12,32850],[12,3,31290],[11,12,3301],[12,1,35664],[7,13,28087],[13,8,24306],[6,13,29503],[11,13,6361],[4,13,35910],[13,12,3060],[3,13,34350],[13,5,34490],[13,2,36962],[10,13,9850],[9,13,19396],[12,14,8882],[8,14,30128],[14,6,35325],[14,5,40312],[1,14,44546],[11,14,12183],[15,12,13581],[2,15,47483],[4,15,46431],[15,10,20371],[15,14,4699],[15,6,40024],[15,7,38608],[1,15,49245],[11,15,16882],[8,15,34827],[0,15,53217],[5,15,45011],[15,3,44871],[16,2,53419],[16,9,35853],[1,16,55181],[16,7,44544],[8,16,40763],[0,16,59153],[15,16,5936],[16,10,26307],[16,6,45960],[12,16,19517],[17,2,57606],[17,3,54994],[17,14,14822],[17,11,27005],[0,17,63340],[17,7,48731],[8,17,44950],[17,16,4187],[5,17,55134],[17,10,30494],[17,9,40040],[17,12,23704],[13,17,20644],[17,1,59368]])
