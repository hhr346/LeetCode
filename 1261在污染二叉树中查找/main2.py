'''
给出一个满足下述规则的二叉树：

root.val == 0
如果 treeNode.val == x 且 treeNode.left != null，那么 treeNode.left.val == 2 * x + 1
如果 treeNode.val == x 且 treeNode.right != null，那么 treeNode.right.val == 2 * x + 2
现在这个二叉树受到「污染」，所有的 treeNode.val 都变成了 -1。

请你先还原二叉树，然后实现 FindElements 类：

FindElements(TreeNode* root) 用受污染的二叉树初始化对象，你需要先把它还原。
bool find(int target) 判断目标值 target 是否存在于还原后的二叉树中并返回结果。
 
示例 1：
输入：
["FindElements","find","find"]
[[[-1,null,-1]],[1],[2]]
输出：
[null,false,true]
解释：
FindElements findElements = new FindElements([-1,null,-1]); 
findElements.find(1); // return False 
findElements.find(2); // return True 

示例 2：
输入：
["FindElements","find","find","find"]
[[[-1,-1,-1,-1,-1]],[1],[3],[5]]
输出：
[null,true,true,false]
解释：
FindElements findElements = new FindElements([-1,-1,-1,-1,-1]);
findElements.find(1); // return True
findElements.find(3); // return True
findElements.find(5); // return False

示例 3：
输入：
["FindElements","find","find","find","find"]
[[[-1,null,-1,-1,null,-1]],[2],[3],[4],[5]]
输出：
[null,true,false,false,true]
解释：
FindElements findElements = new FindElements([-1,null,-1,-1,null,-1]);
findElements.find(2); // return True
findElements.find(3); // return False
findElements.find(4); // return False
findElements.find(5); // return True
 
提示：
TreeNode.val == -1
二叉树的高度不超过 20
节点的总数在 [1, 10^4] 之间
调用 find() 的总次数在 [1, 10^4] 之间
0 <= target <= 10^6

又是需要优化的一题，说运行时间太长了
或许可以观察一下这个结构，在查找的时候不需要一查到底，因为这棵树是递增的，所以查到一定地方就可以跳过了

能用但是还是太慢
官方题解用一个别的数据类型来进行存储就避免了查找树节点时的递归了，直接返回target in xxx就可以了，避免自己写查找算法
还有一种很巧妙的方式就是使用二进制来进行判断，更精准的观察树的存储规律，从而可以精确的确定查找的路径规划
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.root.val = 0
        self.preorder_traversal(self.root.left, self.root.val, 1)
        self.preorder_traversal(self.root.right, self.root.val, 2)

    def preorder_traversal(self, root, val_pre, add_val):
        """前序遍历(根->左->右)"""
        if root is None:
            # 最后一层不是树了！有没有是数但是不是树的？
            return
        else:
            root.val = val_pre*2 + add_val
        # 递归遍历左子树
        self.preorder_traversal(root.left, root.val, 1)
        # 递归遍历右子树
        self.preorder_traversal(root.right, root.val, 2)

    def find(self, target: int) -> bool:
        if self.preorder_find(self.root, target) == None:
            return False
        else:
            return True
    
    def preorder_find(self, root: Optional[TreeNode], target):
        if root is None:
            return

        if root.val == target:
            return root
        elif root.val > target:
            return
        else:
            # 用一个变量来接受返回，找到头都找不到才返回差的，和人生一样！不然就一层层找下去吧
            left_out = self.preorder_find(root.left, target)
            right_out = self.preorder_find(root.right, target)
            return left_out or right_out



# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)