# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        def reverse(nowNode: ListNode, lastNode: ListNode):
            if nowNode.next:
                nextNode = nowNode.next
            nowNode.next = lastNode
            return nextNode, nowNode
        a, b = reverse(head, None)
        while a.next:
            a, b = reverse(a, b)
        a.next = b
        return a


if __name__ == '__main__':
    one = ListNode(1)
    two = ListNode(2)
    three = ListNode(3)
    four = ListNode(4)
    five = ListNode(5)
    one.next = two
    two.next = three
    three.next = four
    four.next = five
    sol = Solution()
    output = sol.reverseList(one)
    print(output)


