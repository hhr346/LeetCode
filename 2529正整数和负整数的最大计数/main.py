'''
给你一个按 非递减顺序 排列的数组 nums ，返回正整数数目和负整数数目中的最大值。

换句话讲，如果 nums 中正整数的数目是 pos ，而负整数的数目是 neg ，返回 pos 和 neg二者中的最大值。
注意：0 既不是正整数也不是负整数。

 

示例 1：

输入：nums = [-2,-1,-1,1,2,3]
输出：3
解释：共有 3 个正整数和 3 个负整数。计数得到的最大值是 3 。
示例 2：

输入：nums = [-3,-2,-1,0,0,1,2]
输出：3
解释：共有 2 个正整数和 3 个负整数。计数得到的最大值是 3 。
示例 3：

输入：nums = [5,20,66,1314]
输出：4
解释：共有 4 个正整数和 0 个负整数。计数得到的最大值是 4 。

一眼二分，试试看
但是遍历肯定更简单一些，对于0的处理也更直接
因为有0，所以是可能三段，所以还是别二分了
'''
import math
from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        length = len(nums)
        num_neg = 0
        num_zero = 0
        for i in range(length):
            if nums[i] < 0:
                num_neg += 1
            elif nums[i] == 0:
                num_zero += 1
            else:
                break
        return max(num_neg, length-num_neg-num_zero)
