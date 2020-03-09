# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return  l1
        head = ListNode(None)
        l3 = head
        while l1 and l2:
            if l1.val < l2.val:
                l3.next = l1
                l1 = l1.next
                l3 = l3.next
            else:
                l3.next = l2
                l2 = l2.next
                l3 = l3.next
        l3.next = l1 if l1 else l2
        return head.next





if __name__ == '__main__':
    sol = Solution()
    output = sol.mergeTwoLists()
    print(output)