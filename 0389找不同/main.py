'''
给定两个字符串 s 和 t ，它们只包含小写字母。
字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
请找出在 t 中被添加的字母。

示例 1：
输入：s = "abcd", t = "abcde"
输出："e"
解释：'e' 是那个被添加的字母。
示例 2：
输入：s = "", t = "y"
输出："y"

提示：
0 <= s.length <= 1000
t.length == s.length + 1
s 和 t 只包含小写字母

初看题目，我们可以想到的是，将两个字符串排序，然后比较，找到不同的字符即可。
'''
from typing import List

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_sort = sorted(s)
        t_sort = sorted(t)
        for i in range(len(s_sort)):
            if s_sort[i] != t_sort[i]:
                return t_sort[i]
        # 如果查到最后一个都一样，那就返回t的最后一个字符
        return t_sort[-1]

if __name__ == "__main__":
    solution = Solution()
    s = "abcd"
    t = "abcde"
    print(solution.findTheDifference(s, t))
