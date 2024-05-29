'''
Hercy 想要为购买第一辆车存钱。他 每天 都往力扣银行里存钱。

最开始，他在周一的时候存入 1 块钱。从周二到周日，他每天都比前一天多存入 1 块钱。在接下来每一个周一，他都会比 前一个周一 多存入 1 块钱。

给你 n ，请你返回在第 n 天结束的时候他在力扣银行总共存了多少块钱。

 

示例 1：

输入：n = 4
输出：10
解释：第 4 天后，总额为 1 + 2 + 3 + 4 = 10 。
示例 2：

输入：n = 10
输出：37
解释：第 10 天后，总额为 (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37 。注意到第二个星期一，Hercy 存入 2 块钱。
示例 3：

输入：n = 20
输出：96
解释：第 20 天后，总额为 (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96 。
 

提示：
1 <= n <= 1000

直接用公式来计算即可，可以先对天数的7取余，得到周数
周数乘以1+...7是基础
然后对周数和余数进行多余的计算，第一周的多余是0，第二周是7...
'''

from typing import List
class Solution:
    def totalMoney(self, n: int) -> int:
        num_week = n//7
        day_remain = n%7
        outcome = 0

        outcome += num_week*28
        for i in range(num_week):
            outcome += 7*i
        outcome += day_remain*num_week
        for i in range(day_remain):
            outcome += (i+1)
        return outcome
