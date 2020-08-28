"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from typing import List


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []

        if root is None:
            return ans

        def recursion(root, ans):
            ans.append(root.val)
            for i in root.children:
                recursion(i, ans)
        recursion(root, ans)
        return ans
