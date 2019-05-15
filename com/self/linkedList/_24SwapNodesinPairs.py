# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # pre -> head
    # pre -> slow -> fast -> fast.next
    # pre -> fast -> slow -> fast.next
    def swapPairs(self, head: ListNode) -> ListNode:
        pre = ListNode(0)
        rel = pre
        pre.next = head
        while pre.next and pre.next.next:
            slow = pre.next
            fast = slow.next
            pre.next, fast.next, slow.next = fast, slow, fast.next
            pre = slow
        return rel.next


if __name__ == '__main__':
    t = Solution();
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    head = t.swapPairs(node1)
    while head:
        print(head.val)
        head = head.next
