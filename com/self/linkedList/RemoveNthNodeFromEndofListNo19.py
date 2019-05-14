# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
##快慢指针，快指针比慢指针快N+1个节点
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        start = ListNode(0)
        slow,fast = start,start
        start.next = head
        for i in range(n+1):
            fast = fast.next
        while fast :
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return start.next
if __name__ == '__main__':
    t =Solution();
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    head = t.removeNthFromEnd(node1,2)
    while head:
        print(head.val)
        head =head.next