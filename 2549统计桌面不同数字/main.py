'''
给你一个正整数 n ，开始时，它放在桌面上。在 109 天内，每天都要执行下述步骤：
对于出现在桌面上的每个数字 x ，找出符合 1 <= i <= n 且满足 x % i == 1 的所有数字 i 。
然后，将这些数字放在桌面上。
返回在 109 天之后，出现在桌面上的 不同 整数的数目。
注意：
一旦数字放在桌面上，则会一直保留直到结束。
% 表示取余运算。例如，14 % 3 等于 2 。

示例 1：
输入：n = 5
输出：4
解释：最开始，5 在桌面上。
第二天，2 和 4 也出现在桌面上，因为 5 % 2 == 1 且 5 % 4 == 1 。
再过一天 3 也出现在桌面上，因为 4 % 3 == 1 。
在十亿天结束时，桌面上的不同数字有 2 、3 、4 、5 。
示例 2：
输入：n = 3
输出：2
解释：
因为 3 % 2 == 1 ，2 也出现在桌面上。
在十亿天结束时，桌面上的不同数字只有两个：2 和 3 。

提示：
1 <= n <= 100

10亿天是什么水平？在一次没有新增数字之后就可以放弃了
实际上就是对每一个数求其减一之后的非1因子（包括自身）
用一个集合来进行存储吧

每次的更新只需要更新上一次新增的就好了，不要重复劳作

对啊，如果说比自己小一个的一定会放到桌面上，迭代去看，那重复时间足够长之后不都进去了吗？
直接推导的结果，不注意过程就可以直接得到一个数字了，多关注一下过程也很容易发现
需要过程就不行了
'''

class Solution:
    def distinctIntegers(self, n: int) -> int:
        self.restore = {n}
        self.restore_before = set()

        for day in range(10**9):
            restore_before = self.restore.copy()
            # 三个变量跟踪状态，注意在循环的时候不能改变！！！
            for num in restore_before:
                if num not in self.restore_before:
                    self.updateFactor(num)
            # 也可以考虑用一个差集变量嘛
            for num in self.restore-self.restore_before:
                self.updateFactor(num)
            self.restore_before = restore_before.copy()
            
            if len(restore_before) == len(self.restore):
                break
        return len(self.restore)
    
    def updateFactor(self, num):
        num -= 1 
        for i in range(2, num+1):
            if num%i == 0:
                self.restore.add(i)
