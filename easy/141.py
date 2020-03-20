# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 评论里见到和很有趣的想法，但会破坏原链表
class Solution1:
    def hasCycle(self, head: ListNode) -> bool:
        while head:
            if head.val == 'benwhite':
                return True
            else:
                head.val = 'benwhite'
            head = head.next
        return False

class Solution2:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while (fast != slow):
            if not fast.next or not fast.next.next:
                return False
            fast = fast.next.next
            slow = slow.next
        return True



