# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next = l2
        else:
            point.next = l1
        return head.next

    def mergeKLists(self, lists) -> ListNode:
        interval = 1
        N = len(lists)
        while interval < N:
            for i in range(0, N - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if N > 0 else None


if __name__ == '__main__':
    t = Solution();
    node1 = ListNode(1)
    node2 = ListNode(4)
    node3 = ListNode(5)
    node4 = ListNode(1)
    node5 = ListNode(3)
    node6 = ListNode(4)
    node7 = ListNode(2)
    node8 = ListNode(6)
    node1.next = node2
    node2.next = node3

    node4.next = node5
    node5.next = node6

    node7.next = node8
    lists = [node1, node4,node7]
    head = t.mergeKLists(lists)
    while head:
        print(head.val)
        head = head.next
