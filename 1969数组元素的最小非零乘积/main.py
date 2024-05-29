'''
给你一个正整数 p 。你有一个下标从 1 开始的数组 nums ，这个数组包含范围 [1, 2**p - 1] 内所有整数的二进制形式（两端都 包含）。你可以进行以下操作 任意 次：
从 nums 中选择两个元素 x 和 y  。
选择 x 中的一位与 y 对应位置的位交换。对应位置指的是两个整数 相同位置 的二进制位。
比方说，如果 x = 1101 且 y = 0011 ，交换右边数起第 2 位后，我们得到 x = 1111 和 y = 0001 。
请你算出进行以上操作 任意次 以后，nums 能得到的 最小非零 乘积。将乘积对 109 + 7 取余 后返回。
注意：答案应为取余 之前 的最小值。

示例 1：
输入：p = 1
输出：1
解释：nums = [1] 。
只有一个元素，所以乘积为该元素。

示例 2：
输入：p = 2
输出：6
解释：nums = [01, 10, 11] 。
所有交换要么使乘积变为 0 ，要么乘积与初始乘积相同。
所以，数组乘积 1 * 2 * 3 = 6 已经是最小值。

示例 3：
输入：p = 3
输出：1512
解释：nums = [001, 010, 011, 100, 101, 110, 111]
- 第一次操作中，我们交换第二个和第五个元素最左边的数位。
    - 结果数组为 [001, 110, 011, 100, 001, 110, 111] 。
- 第二次操作中，我们交换第三个和第四个元素中间的数位。
    - 结果数组为 [001, 110, 001, 110, 001, 110, 111] 。
数组乘积 1 * 6 * 1 * 6 * 1 * 6 * 7 = 1512 是最小乘积。

提示：
1 <= p <= 60

所谓的交换实际上在做什么？感觉用贪心就可以？
交换是在重组乘积的因子，根据基本不等式，我们应该尽可能的让数远离相等的点，同时避免0值
所以进行迭代变化？

整体来统筹0和1的分布，不需要用贪心就能解决，但是感觉不好实现，怎么确定让谁是强让谁弱？
从最高位开始，尽可能把所有的1都给高位，只有到最后一位的时候考虑一下0的问题（还是最后解决0的问题吧）
刷题见识多，思考得多的联系，死记硬背的文科和逻辑？

感觉这个就是纯粹的数学问题了
给定一个正整数，那所有的1的个数也都确定了，只需要进行一点点计算就行
很多问题只有编程才能发现啊，以为自己会了

官方题解贪心和快速幂是什么？
不出所料又超出时间限制啦，指数级上升的就是不行？
'''
import math
import numpy as np

class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        self.p = p
        upper = 2**p-1
        self.digits = math.floor(math.log(upper, 2))+1
        # digits = math.ceil(math.log(p)+1)
        self.maximum = 2 ** self.digits - 1
        print(self.digits)
        print(self.maximum)

        num1_list = []
        num0_list = []
        # 对每一位都进行计算0和1的个数，同时按照低位到高位排好
        for digit in range(self.digits, 0, -1):
            num1, num0 = self.defineNums(upper)
            print(num1, num0)
            upper = 0
            num1_list.insert(0, num1)
            num0_list.insert(0, num0)
        print(num1_list)
        print(num0_list)

        # 将01重新进行排列
        remix_all = np.zeros(2**p-1, dtype=int)
        remix = []
        care4zero = 2**p-1-min(num1_list)

        for digit in range(self.digits, 0, -1):
            for i in range(2**p-1):
                index = self.digits-digit
                if index == 0 and care4zero != 0:
                    remix.append(1)
                    # one fewer to care
                    care4zero -= 1
                    # one zero to push forward
                    num0_list[0] += 1
                    continue

                if i < num0_list[index]:
                    remix.append(0)
                else:
                    remix.append(2**(index))
            print('remix is ', remix)
            remix_all += np.array(remix)
            remix = []
        return self.multiplyAll(remix_all)
    
    def defineNums(self, num):
        # 这里要经过一点点数学计算，返回1的数目和0的数目
        if num == 2**self.p-1:
            # 首位需要麻烦一点的计算
            return (int(num+(1-self.maximum)/2), int((self.maximum-1)/2))
        else: 
            return (int(2**(self.p-1)), int(2**(self.p-1)-1))

    def multiplyAll(self, all):
        # 因为数太大了，所以必须要进行取余！！！每步都取余才能避免溢出！
        outcome = 1
        for each in all:
            outcome *= each
            outcome = outcome%(1e9+7)
        return int(outcome)

if __name__ == "__main__":
    solution = Solution()
    p = 22
    answer = solution.minNonZeroProduct(p)
    print(answer)
