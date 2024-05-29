'''
给你一个字符串 title ，它由单个空格连接一个或多个单词组成，每个单词都只包含英文字母。请你按以下规则将每个单词的首字母 大写 ：
如果单词的长度为 1 或者 2 ，所有字母变成小写。
否则，将单词首字母大写，剩余字母变成小写。
请你返回 大写后 的 title 。

示例 1：
输入：title = "capiTalIze tHe titLe"
输出："Capitalize The Title"
解释：
由于所有单词的长度都至少为 3 ，将每个单词首字母大写，剩余字母变为小写。
示例 2：

输入：title = "First leTTeR of EACH Word"
输出："First Letter of Each Word"
解释：
单词 "of" 长度为 2 ，所以它保持完全小写。
其他单词长度都至少为 3 ，所以其他单词首字母大写，剩余字母小写。
示例 3：

输入：title = "i lOve leetcode"
输出："i Love Leetcode"
解释：
单词 "i" 长度为 1 ，所以它保留小写。
其他单词长度都至少为 3 ，所以其他单词首字母大写，剩余字母小写。
 

提示：
1 <= title.length <= 100
title 由单个空格隔开的单词组成，且不含有任何前导或后缀空格。
每个单词由大写和小写英文字母组成，且都是 非空 的。
'''

from curses.ascii import islower, isupper

class Solution:
    def convertSmall(self, str_in: str) -> str:
        if str_in.islower():
            str_out = str_in
        else:
            str_out = str_in.lower()
        return str_out
    
    def convertBig(self, str_in: str) -> str:
        if str_in.isupper():
            str_out = str_in
        else:
            str_out = str_in.upper()
        return str_out

    def capitalizeTitle(self, title: str) -> str:
        str_list = title.split(' ')
        convert_list = []
        for word in str_list:
            word_convert = ''.join(self.convertSmall(i) for i in word)
            # 尽可能的统一逻辑，两种情况可以都先全部转为小写，然后再去对特殊的第一个字母更改
            # 清晰的逻辑要比没必要的奇技淫巧更好，理解也是有成本的
            # 如果可能性少就完全可以遍历来做，一个带一个
            if len(word) >= 3:
                word_convert = self.convertBig(word_convert[0]) + word_convert[1:]
            convert_list.append(word_convert)
        title_convert = ' '.join(i for i in convert_list)
        return title_convert
        