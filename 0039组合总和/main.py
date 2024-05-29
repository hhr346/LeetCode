'''
给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。

candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 

对于给定的输入，保证和为 target 的不同组合数少于 150 个。

 

示例 1：

输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
解释：
2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
7 也是一个候选， 7 = 7 。
仅有这两种组合。
示例 2：

输入: candidates = [2,3,5], target = 8
输出: [[2,2,2,2],[2,3,3],[3,5]]
示例 3：

输入: candidates = [2], target = 1
输出: []
 

提示：

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
candidates 的所有元素 互不相同
1 <= target <= 40

感觉这个就是改进之后的背包问题？区别就在于一个元素可以使用多次，所以每次拿完一个元素之后还是有机会可以继续拿的
可以用动态规划来实现
还是有区别的，这个要求价值恰好符合总数，并且还有问题是使用多次的话这个次数怎么确定？用最小的物体来衡量？
你这有最优子结构吗？要求的也不是极值啊，而是总数？
精确的算法要求高效的搜索，近似的算法就需要了解合适的特征分布

试试看穷举吧，用树来实现？题解也是这么写的
对于需要所有的结果的相对来说就没有什么太好的方法了，求极值和遍历还是有很大区别的
'''
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 对候选数组进行排序
        candidates.sort()
        # 用于存储结果的列表
        result = []
        # 用于存储当前组合的栈
        stack = []
        # 用于存储当前组合的和
        current_sum = 0
        # 当前遍历的索引
        index = 0
        
        while True:
            # 如果当前和等于目标和，则找到一个组合
            if current_sum == target:
                result.append(list(stack))
            
            # 如果当前和大于等于目标和，或者已经遍历完所有元素，则回溯
            if current_sum > target:
                index += 1
                # 回溯，弹出栈顶元素，并从当前和中减去其值
                current_sum -= stack.pop()
            if index == len(candidates):
                # 如果栈为空，则表示已经回溯完所有组合，结束循环
                if not stack:
                    return result
            
            # 将当前索引对应的元素加入栈中，并更新当前和
            stack.append(candidates[index])
            current_sum += candidates[index]
