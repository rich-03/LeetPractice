# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None:
            return t2
        elif t2 is None:
            return t1
        t1.val += t2.val
        t1.left = Solution().mergeTrees(t1.left, t2.left)
        t1.right = Solution().mergeTrees(t1.right, t2.right)

        return t1
