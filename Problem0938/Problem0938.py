# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.sum = 0

        def dfs(node, L, R):
            if not node: return 0
            if L <= node.val <= R: self.sum += node.val

            dfs(node.left, L, R)
            dfs(node.right, L, R)

        dfs(root, L, R)
        return self.sum
