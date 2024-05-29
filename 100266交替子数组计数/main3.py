'''
给你一个二进制数组 nums 。

如果一个子数组中 不存在 两个 相邻 元素的值 相同 的情况，我们称这样的子数组为 交替子数组 。

返回数组 nums 中交替子数组的数量。

 

示例 1：

输入： nums = [0,1,1,1]

输出： 5

解释：

以下子数组是交替子数组：[0] 、[1] 、[1] 、[1] 以及 [0,1] 。

示例 2：

输入： nums = [1,0,1,0]

输出： 10

解释：

数组的每个子数组都是交替子数组。可以统计在内的子数组共有 10 个。

 

提示：

1 <= nums.length <= 105
nums[i] 不是 0 就是 1 。

应该不会允许跳跃式的选取吧
感觉可能可以用数学的方式算
首先是单个元素显然都是，然后每出现一对相同的，就会影响到上面所有的
所以维护一个不断变小的数组，1即为相邻不同，0为相同
每次向上就用与运算让他们减小一位
'''
from typing import List
class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 0
        count = 1  # 当前子数组长度
        prev = nums[0]  # 前一个元素

        for i in range(1, n):
            if nums[i] != prev:
                answer += count
                count = 1
            else:
                count += 1
            prev = nums[i]
        # 处理最后一个子数组
        answer += count
        return answer
