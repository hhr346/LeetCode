'''
给你一个正整数 k 。最初，你有一个数组 nums = [1] 。
你可以对数组执行以下 任意 操作 任意 次数（可能为零）：
选择数组中的任何一个元素，然后将它的值 增加 1 。
复制数组中的任何一个元素，然后将它附加到数组的末尾。
返回使得最终数组元素之 和 大于或等于 k 所需的 最少 操作次数。
示例 1：
输入：k = 11
输出：5
解释：
可以对数组 nums = [1] 执行以下操作：
将元素的值增加 1 三次。结果数组为 nums = [4] 。
复制元素两次。结果数组为 nums = [4,4,4] 。
最终数组的和为 4 + 4 + 4 = 12 ，大于等于 k = 11 。
执行的总操作次数为 3 + 2 = 5 。
示例 2：
输入：k = 1
输出：0
解释：
原始数组的和已经大于等于 1 ，因此不需要执行操作。
提示：
1 <= k <= 105

增加1和自我复制之间有一个平衡点
'''
import math

class Solution:
    def minOperations(self, k: int) -> int:
        m = math.sqrt(k)
        if int(m)**2 == k:
            return int(2*m-2)
        else:
            top = math.ceil(m)
            floor = math.floor(m)
            if floor*top >= k:
                return int(floor+top-2)
            else:
                return int(top*2-2)
