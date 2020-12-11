# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy_head = ListNode(-1, head)
        dummy_head.next = head
        current = dummy_head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return dummy_head.next


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(1, node1)
    Solution().removeElements(node2, 1)
    print(node2)