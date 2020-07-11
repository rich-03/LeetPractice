# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False

        s = head  # s stands for the slower pointer
        f = head.next  # f stands for the faster pointer

        while s is not None and f is not None and f.next is not None:
            if s == f:
                return True
            s = s.next
            f = f.next.next
        return False
