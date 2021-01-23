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


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head: return None
        if not head.next: return head
        c = 1
        first = head
        for i in range(k):
            if first.next:
                first = first.next
                c += 1
            else:
                first = head
                break

        if k > c:
            k = k % c
            for i in range(k):
                first = first.next

        second = head

        while first.next:
            first = first.next
            if second.next:
                second = second.next
            else:
                second = head

        first.next = head
        head = second.next
        second.next = None

        return head


if __name__ == '__main__':
    input = [1, 2]
    k = 20  # 00000000
    k = 2
    head = getHead(input)
    output = Solution().rotateRight(head, k)
    print(output)
