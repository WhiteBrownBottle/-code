# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        if head.next is None:
            return head.val
        ans = head
        while head is not None:
            if head.next is not None and head.next.val == head.val:
                head.next = head.next.next
            else:
                head = head.next
        return ans



if __name__ == '__main__':
    pass