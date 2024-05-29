'''
给你一个下标从 0 开始、由正整数组成的数组 nums 。
你可以在数组上执行下述操作 任意 次：
选中一个同时满足 0 <= i < nums.length - 1 和 nums[i] <= nums[i + 1] 的整数 i 。将元素 nums[i + 1] 替换为 nums[i] + nums[i + 1] ，并从数组中删除元素 nums[i] 。
返回你可以从最终数组中获得的 最大 元素的值。

示例 1：
输入：nums = [2,3,7,9,3]
输出：21
解释：我们可以在数组上执行下述操作：
- 选中 i = 0 ，得到数组 nums = [5,7,9,3] 。
- 选中 i = 1 ，得到数组 nums = [5,16,3] 。
- 选中 i = 0 ，得到数组 nums = [21,3] 。
最终数组中的最大元素是 21 。可以证明我们无法获得更大的元素。

示例 2：
输入：nums = [5,3,3]
输出：11
解释：我们可以在数组上执行下述操作：
- 选中 i = 1 ，得到数组 nums = [5,6] 。
- 选中 i = 0 ，得到数组 nums = [11] 。
最终数组中只有一个元素，即 11 。

提示：
1 <= nums.length <= 105
1 <= nums[i] <= 106

看起来就必须要用特殊的数据结构来解决问题
右侧对我来说越大越好，或许可以用贪心算法？
不知道如何严密的证明右侧更大对我总没有坏处，并且迭代做总能获得最大值

递归也是一种循环，巧妙利用自身的结构进行循环，并传入不同的参数
'''

from typing import List
class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        length = len(nums)
        for count in range(length-1):
            if nums[length-1-count] >= nums[length-2-count]:
                pop1 = nums.pop(length-1-count)
                pop2 = nums.pop(length-2-count)
                print(pop1, pop2)
                nums.insert(length-2-count, pop1 + pop2)
                print(nums)
        return max(nums)

if __name__ == '__main__':
    nums = [5,3,3]
    solution = Solution()
    answer = solution.maxArrayValue(nums)
    print(answer)