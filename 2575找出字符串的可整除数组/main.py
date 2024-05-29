'''
给你一个下标从 0 开始的字符串 word ，长度为 n ，由从 0 到 9 的数字组成。另给你一个正整数 m 。
word 的 可整除数组 div  是一个长度为 n 的整数数组，并满足：
如果 word[0,...,i] 所表示的 数值 能被 m 整除，div[i] = 1
否则，div[i] = 0
返回 word 的可整除数组。

示例 1：
输入：word = "998244353", m = 3
输出：[1,1,0,0,0,1,1,0,0]
解释：仅有 4 个前缀可以被 3 整除："9"、"99"、"998244" 和 "9982443" 。
示例 2：

输入：word = "1010", m = 10
输出：[0,1,0,1]
解释：仅有 2 个前缀可以被 10 整除："10" 和 "1010" 。

提示：
1 <= n <= 105
word.length == n
word 由数字 0 到 9 组成
1 <= m <= 10
'''

from typing import List
import sys
# 设置整数转换为字符串的最大位数
sys.set_int_max_str_digits(10000)

class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        # Create a list of elements in the WORD
        word_list = []
        for i in word:
            if len(word_list) == 0:
                word_list.append(i)
            else:
                word_list.append(word_list[-1]+i)
        
        output = []
        for ascend in word_list:
            ascend = int(ascend)
            if ascend%m == 0:
                output.append(1)
            else:
                output.append(0)
        
        return output


if __name__ == '__main__':
    import sys
    word = sys.argv[1]
    m = int(sys.argv[2])
    solution = Solution()
    answer = solution.divisibilityArray(word, m)
    print(answer)
