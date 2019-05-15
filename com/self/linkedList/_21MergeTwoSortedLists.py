# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        start = ListNode(0)
        head = start
        while l1 and l2:
            if l1.val <= l2.val:
                start.next = l1
                l1 =l1.next
                start =start.next
            else:
                start.next = l2
                l2 =l2.next
                start =start.next
        if l1:
            start.next = l1
        else:
            start.next = l2
        return head.next
if __name__ == '__main__':
    t =Solution();
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(1)
    node5 = ListNode(2)
    node6 = ListNode(4)
    node7 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node4.next = node5
    node5.next = node6
    node6.next = node7
    head = t.mergeTwoLists(node1,node4)
    while head:
        print(head.val)
        head =head.next
