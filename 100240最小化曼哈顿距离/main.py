'''
给你一个下标从 0 开始的数组 points ，它表示二维平面上一些点的整数坐标，其中 points[i] = [xi, yi] 。

两点之间的距离定义为它们的曼哈顿距离。

请你恰好移除一个点，返回移除后任意两点之间的 最大 距离可能的 最小 值。

 

示例 1：

输入：points = [[3,10],[5,15],[10,2],[4,4]]
输出：12
解释：移除每个点后的最大距离如下所示：
- 移除第 0 个点后，最大距离在点 (5, 15) 和 (10, 2) 之间，为 |5 - 10| + |15 - 2| = 18 。
- 移除第 1 个点后，最大距离在点 (3, 10) 和 (10, 2) 之间，为 |3 - 10| + |10 - 2| = 15 。
- 移除第 2 个点后，最大距离在点 (5, 15) 和 (4, 4) 之间，为 |5 - 4| + |15 - 4| = 12 。
- 移除第 3 个点后，最大距离在点 (5, 15) 和 (10, 2) 之间的，为 |5 - 10| + |15 - 2| = 18 。
在恰好移除一个点后，任意两点之间的最大距离可能的最小值是 12 。
示例 2：

输入：points = [[1,1],[1,1],[1,1]]
输出：0
解释：移除任一点后，任意两点之间的最大距离都是 0 。
 

提示：

3 <= points.length <= 105
points[i].length == 2
1 <= points[i][0], points[i][1] <= 108

这个还算比较显然，找出所有点的最大距离，然后对这个最大距离的点对下的两个点返回最小值
但是可能会有重复的最大距离！
不重复就是找到最小工作量的本质，每一步的操作都是决出可能性的必要的
同时也有时空的权衡，不过时空的权衡不是最小工作量的问题了
还有思考的权衡，穷举不是都是不好的方法，直线的穷举
有时候适当的记住可以减少工作量，和时空观有什么关系吗？
都是关于极值或者极值的极值
vim输入的撤销是按照操作来的
'''

from typing import List
class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        max_distance = 0
        max_ij = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                now_dis = calMan(points[i], points[j])
                if  now_dis >= max_distance:
                    max_distance = now_dis
                    max_ij.append([i,j])
        
        min_distance_list = []
        for m,n in max_ij:
            for remove in [m, n]:
                max_distance = 0
                now_points = points[:]
                now_points.remove(points[remove])
                for i in range(len(now_points)):
                    for j in range(i+1, len(now_points)):
                        now_dis = calMan(now_points[i], now_points[j])
                        if  now_dis >= max_distance:
                            max_distance = now_dis
                min_distance_list.append(max_distance)
        return min(min_distance_list)
        
def calMan(point1, point2):
    return abs(point1[0]-point2[0])+abs(point1[1]-point2[1])
