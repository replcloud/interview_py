class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getHead(l: list):
    dummmy = ListNode(-1)
    curr = dummmy
    for x in l:
        curr.next = ListNode(x)
        curr = curr.next
    return dummmy.next

def printLinkedList(head: ListNode):
    if head:
        print(head.val, end='')
        head = head.next
    while head:
        print("->" + str(head.val), end='')
        head = head.next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return None
        if not head.next: return head
        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy
        next = curr.next
        while next:
            if next.next and next.val == next.next.val:
                dupval = next.val
                while next and next.val == dupval:
                    next = next.next
                curr.next = next
            else:
                curr = curr.next
                next = next.next
        return dummy.next


if __name__ == '__main__':
    input = [1, 2, 3, 3, 4, 4, 5]
    input = [1, 1]
    head = getHead(input)
    output = Solution().deleteDuplicates(head)
    printLinkedList(output)
