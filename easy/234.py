# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        slow = head
        fast = head
        pre = head
        prepre = None

        while fast and fast.next:
            # pre记录翻转的前半个列表，slow是原表一步步走
            pre = slow
            slow = slow.next
            fast = fast.next.next
            pre.next = prepre
            prepre = pre

        if fast:
            slow = slow.next

        while slow and pre:
            if slow.val != pre.val:
                return False
            slow = slow.next
            pre = pre.next
        return True
