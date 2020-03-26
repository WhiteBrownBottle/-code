# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
        if head.val == val:
            head = head.next
        tmp = head
        while tmp:
            while tmp.next and tmp.next.val != val:
                tmp = tmp.next
            tmp2 = tmp
            while tmp2.next and tmp2.next.val == val:
                tmp2 = tmp2.next
            tmp.next = tmp2.next
            tmp = tmp2.next
        return head


if __name__ == '__main__':
    head = ListNode(1)
    second = ListNode(2)
    third = ListNode(6)
    four = ListNode(3)
    five = ListNode(4)
    six = ListNode(5)
    seven = ListNode(6)
    head.next = second
    second.next = third
    third.next = four
    four.next = five
    five.next = six
    six.next = seven
    seven.next = None
    sol = Solution()
    output = sol.removeElements(head, 6)
    print(output)




