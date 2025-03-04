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
需要考虑一个严格的截断点：新插入的数值即使是单个也无法影响到前k个数的时候就可以截断了（这个按影响力的排序很重要）
也就是说要解决问题并不要那么多的中间变量，其实很多物理规律也是这样的思路，找到关键点关键参数和关键变量就足够了，作为黑盒如何不断改进自身
如何找到关键变量也很重要，不影响全局的前提下进行变换来更方便的处理
按照事情的重要程度来排序和不断进行改进，从上一个到下一个的不断改进
性能要求太麻烦了，想优化要怎么做啊

还是需要优化？？？想不到了啊
可以只存储第k个数吗？相等的情况只有最开始会有！不是的，实际上还会有可能有相同的数！！？

实际上这些优化都是小大小闹
最重要的问题是指数上升的存储量
我这个本质上就还是要穷举，只是相对来说少了一点
所以要用算法进行优化，简直是降维打击
对于特殊的问题要用相应的最小的成本代价递增，没学过这些知识的压根就想不到，见识不到
你比之前的人厉害吗？你能独立发现吗？
"""
from typing import List

class Solution:
    def multipleList(self, before: List[int], add: int) -> List:
        after = before[:]
        for i in before:
            after.append(i+add)
        return after

    def kSum(self, nums: List[int], k: int) -> int:
        top_sum = sum(num for num in nums if num>0)
        nums = sorted(nums, key=abs)

        outcome = [top_sum]
        compare = None
        for count in range(len(nums)):
            compare_last = compare
            outcome = self.multipleList(outcome, -abs(nums[count]))
            outcome = sorted(outcome, reverse=True)
            compare = None if len(outcome)<k else outcome[k-1]

            if compare == compare_last and compare is not None:
                break
        return outcome[k-1]

if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,3,4]
    nums, k = [2,4,-2], 5
    nums, k= [1,-2,3,4,-10,12], 16
    nums, k = [153123449,-974739108,-408679566,-996444415,-978921261,805907128,-102259288,-397930077,51033052,-193994032,158654659,-486195972,-294264190,-65262667,375941242,-890038230,315970860,403847239,-32469129,-350561293,192113942,794248972,-632675681,434029943,746632801,500370163,164413366,346449701,473890512], 1906
    nums, k = [1000,1001,1002,1003,1004,1005,1006,1007,1008,1009], 10
    solution.kSum(nums, k)
