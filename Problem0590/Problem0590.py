"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from typing import List


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return None
        ans = []

        def solver(node):
            for i in node.children:
                solver(i)
            ans.append(node.val)

        solver(root)
        return ans
