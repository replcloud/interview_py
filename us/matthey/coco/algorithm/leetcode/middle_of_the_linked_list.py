# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head:
            return None
        p1 = head
        p2 = head

        while p2:
            if not p2.next:
                break
            p1 = p1.next
            p2 = p2.next.next
        return p1