'''
你的笔记本键盘存在故障，每当你在上面输入字符 'i' 时，它会反转你所写的字符串。而输入其他字符则可以正常工作。

给你一个下标从 0 开始的字符串 s ，请你用故障键盘依次输入每个字符。

返回最终笔记本屏幕上输出的字符串。

 

示例 1：

输入：s = "string"
输出："rtsng"
解释：
输入第 1 个字符后，屏幕上的文本是："s" 。
输入第 2 个字符后，屏幕上的文本是："st" 。
输入第 3 个字符后，屏幕上的文本是："str" 。
因为第 4 个字符是 'i' ，屏幕上的文本被反转，变成 "rts" 。
输入第 5 个字符后，屏幕上的文本是："rtsn" 。
输入第 6 个字符后，屏幕上的文本是： "rtsng" 。
因此，返回 "rtsng" 。
示例 2：

输入：s = "poiinter"
输出："ponter"
解释：
输入第 1 个字符后，屏幕上的文本是："p" 。
输入第 2 个字符后，屏幕上的文本是："po" 。
因为第 3 个字符是 'i' ，屏幕上的文本被反转，变成 "op" 。
因为第 4 个字符是 'i' ，屏幕上的文本被反转，变成 "po" 。
输入第 5 个字符后，屏幕上的文本是："pon" 。
输入第 6 个字符后，屏幕上的文本是："pont" 。
输入第 7 个字符后，屏幕上的文本是："ponte" 。
输入第 8 个字符后，屏幕上的文本是："ponter" 。
因此，返回 "ponter" 。
 

提示：
1 <= s.length <= 100
s 由小写英文字母组成
s[0] != 'i'

直接进行模拟就行吧

然而字符串反转需要 O(l)O(l)O(l) 的时间，其中 lll 是当前 ans\textit{ans}ans 的长度，这样做的时间复杂度较高。事实上，当字符串进行反转后，在末尾添加字符等价于「不对字符串进行反转，并且在开头添加字符」。因此，我们可以使用一个双端队列和一个布尔变量 head\textit{head}head 来维护答案：

当遇到非 “i”\text{``i''}“i” 的字符时，如果 head\textit{head}head 为真，就在队列的开头添加字符，否则在队列的末尾添加字符；

当遇到 “i”\text{``i''}“i” 时，将 head\textit{head}head 取反。

head\textit{head}head 的初始值为假。这样一来，每一个字符只需要 O(1)O(1)O(1) 的时间进行处理。

真聪明啊，可以从另一边来进行插入，减少了翻转的时间
'''
from typing import List
class Solution:
    def finalString(self, s: str) -> str:
        self.now_str = ''
        for i in range(len(s)):
            if s[i] == 'i':
                self.turnAround()
            else:
                self.now_str += s[i]
        return self.now_str
    
    def turnAround(self):
        self.now_str = ''.join(self.now_str[i] for i in range(len(self.now_str)-1, -1, -1))
