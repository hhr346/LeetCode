'''
给你一个仅由小写英文字母组成的字符串s。在一步操作中，你可以完成以下行为：
选择s的任一非空子字符串，可能是整个字符串，接着将字符串中的每一个字符替换为英文字母表中的前一个字符。例如，'b'用'a'替换，'a'用'z'替换。
返回执行上述操作恰好一次后可以获得的字典序最小的字符串。
子字符串是字符串中的一个连续字符序列。
现有长度相同的两个字符串x和字符串y，在满足x[i]!=y[i]的第一个位置i上，如果x[i]在字母表中先于y[i]出现，则认为字符串x比字符串y字典序更小。
示例1：
输入：s="cbabc"
输出："baabc"
解释：我们选择从下标0开始、到下标1结束的子字符串执行操作。
可以证明最终得到的字符串是字典序最小的。
示例2：
输入：s="acbbc"
输出："abaab"
解释：我们选择从下标1开始、到下标4结束的子字符串执行操作。
可以证明最终得到的字符串是字典序最小的。
示例3：
输入：s="leetcode"
输出："kddsbncd"
解释：我们选择整个字符串执行操作。
可以证明最终得到的字符串是字典序最小的。
提示：
1<=s.length<=3*105
s仅由小写英文字母组成

这个其实很直观，就是从头找到第一个a，然后把a之前的字母都向前推一位就行了
但如果a出现在开头的话，那就会有问题，开头是a的话直接跳过就好
用两个变量进行跟踪，第一个出现不是a的字母开始，再次遇到a则结束
还有一个特殊情况是全都是a，那么也必须要进行操作，这个判断的优先级先于正常情况

将字符串转为列表来单独一个个处理，效率应该更高
'''
from typing import List

class Solution:
    def smallestString(self, s: str) -> str:
        outcome = ""
        start = 0
        stop = 0
        for i, digit in enumerate(s):
            if digit == 'a':
                if start != 0:
                    stop = 1
            else:
                start = 1

            if i == (len(s)-1) and start == 0:
                outcome += self.shift_letter_forward(digit)
            elif (stop == 1) or (start == 0) :
                outcome += digit
            else:
                outcome += self.shift_letter_forward(digit)
        return outcome

    def shift_letter_forward(self, letter):
        if letter.isalpha():
            if letter == 'a':
                return 'z'
            # elif letter == 'A':
            #     return 'Z'
            else:
                return chr(ord(letter) - 1)
        else:
            return letter

if __name__=="__main__":
    solution = Solution()
    s = "aa"
    print(solution.smallestString(s))
