"""
给你一个整数数组 nums 和一个 正 整数 k 。你可以选择数组的任一 子序列 并且对其全部元素求和。
数组的 第 k 大和 定义为：可以获得的第 k 个 最大 子序列和（子序列和允许出现重复）
返回数组的 第 k 大和 。
子序列是一个可以由其他数组删除某些或不删除元素排生而来的数组，且派生过程不改变剩余元素的顺序。
注意：空子序列的和视作 0 。

示例 1：
输入：nums = [2,4,-2], k = 5
输出：2
解释：所有可能获得的子序列和列出如下，按递减顺序排列：
- 6、4、4、2、2、0、0、-2
数组的第 5 大和是 2 。

示例 2：
输入：nums = [1,-2,3,4,-10,12], k = 16
输出：10
解释：数组的第 16 大和是 10 。
 

提示：
n == nums.length
1 <= n <= 105
-109 <= nums[i] <= 109
1 <= k <= min(2000, 2n)

巧妙的利用数学归纳法的递推性质来思考问题，不要直接想处理所有的，而是找到上一个和这一个之间的联系，从而简化逻辑
但是这个问题的数目是指数上升的。
很多用例直接做的内存要求太高了，所以要想办法进行优化，或者想出更好的方法，让需求得到了满足，同时少一点不必要的中间步骤！
比如这里要用到k个最大的，我就没必要所有都算，而是排序之后求取前k个就好了（错误的 但是又很接近了！只需要改一下排序的方式）
进一步优化就是头尾，如果k很大我就从末端开始
我脑子还挺活啊，可以搞计算机？搞什么物理，搞创业！加油！

用栈和队列互相转化的直观思考
用低效的算法，是因为搜索的选择的问题？还是说不够高效？
自己思考的有趣的内容的对应
"""
from typing import List
import math

class Solution:
    def multipleList(self, before: List[int], add: int) -> List:
        after = before[:]
        for i in before:
            after.append(i+add)
        return after

    def kSum(self, nums: List[int], k: int) -> int:
        '''
        # Wrong thought
        if k > 2**(len(nums)-1):
            nums = sorted(nums)
        else:
            nums = sorted(nums, reverse=True)
        print(nums)

        outcome = [0]
        for count in range(math.ceil(math.log2(k))):
            outcome = self.multipleList(outcome, nums[count])
            print(outcome)
        outcome = sorted(outcome, reverse=True)
        print(outcome)
        return outcome[k-1]
        '''
        for count in range(len(nums)):
            outcome = self.multipleList(outcome, nums[count])
            print(outcome)
        outcome = sorted(outcome, reverse=True)
        print(outcome)
        return outcome[k-1]
 
if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,3,4]
    nums = [2,4,-2]
    nums = [1,-2,3,4,-10,12]
    k = 16
    solution.kSum(nums, k)
