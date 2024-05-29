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

正确的排序思路应该考虑最大值出现的情况，和其他依次递减的影响力
所以先将所有正数加起来，得到最大的数，再将其他数按照绝对值进行排序，来进行增殖
选择合适的基石

还是不对，对于单个是可以这么做，但是他们还可以排列组合啊，也就是说提前截断可能会影响之后的单个元素插入到之前的排列组合中
同时也可能是之后的排列组合插入到之前的组合中
需要考虑一个严格的截断点
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
        top_sum = sum(num for num in nums if num>0)
        # nums_sorted = sorted(nums, key=lambda x:abs(x))
        nums_sorted = sorted(nums, key=abs)
        print(nums_sorted)

        outcome = [top_sum]
        for count in range(math.ceil(math.log2(k))):
            outcome = self.multipleList(outcome, -abs(nums_sorted[count]))
            # print(outcome)
        outcome = sorted(outcome, reverse=True)
        # print(outcome)
        print(outcome[k-1])
        return outcome[k-1]

if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,3,4]
    nums = [1,-2,3,4,-10,12], 16
    nums, k = [2,4,-2], 5
    nums, k = [153123449,-974739108,-408679566,-996444415,-978921261,805907128,-102259288,-397930077,51033052,-193994032,158654659,-486195972,-294264190,-65262667,375941242,-890038230,315970860,403847239,-32469129,-350561293,192113942,794248972,-632675681,434029943,746632801,500370163,164413366,346449701,473890512], 1906
    solution.kSum(nums, k)
