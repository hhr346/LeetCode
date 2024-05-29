'''
给你一个字符串 s ，请找出满足每个字符最多出现两次的最长子字符串，并返回该子字符串的 最大 长度。
示例 1：
输入： s = "bcbbbcba"
输出： 4
解释：
以下子字符串长度为 4，并且每个字符最多出现两次："bcbbbcba"。
示例 2：
输入： s = "aaaa"
输出： 2
解释：
以下子字符串长度为 2，并且每个字符最多出现两次："aaaa"。
提示：
2 <= s.length <= 100
s 仅由小写英文字母组成。

一眼贪心就行啦，不断向后查，不断进行更新

'''
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans = 2
        ans_now = 2
        store = s[0:2]
        start = 0

        for i in range(2, len(s)):
            letter = s[i]
            if store.count(letter) == 2:
                index = store.index(letter)+start+1
                start = index
                store = s[index:i+1]
                ans_now = len(store)
                ans = max(ans_now, ans)
            else:
                store += letter
                ans_now += 1
                ans = max(ans_now, ans)
        return ans
