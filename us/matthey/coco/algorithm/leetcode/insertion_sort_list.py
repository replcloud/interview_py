# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def makeList(l: list):
    node = None
    for x in l[::-1]:
        node = ListNode(x, node)
    return node

def printNode(head: ListNode):
    while head:
        print(head.val, '->', sep=' ')
        head = head.next
    print()

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # https://leetcode.com/problems/insertion-sort-list/discuss/190913/Java-Python-with-Explanations
        dummy = ListNode(0)
        dummy.next = head

        while head and head.next:
            if head.val > head.next.val:
                nodeToInsert = head.next
                nodeToInsertPre = dummy
                while nodeToInsertPre.next.val < nodeToInsert.val:
                    nodeToInsertPre = nodeToInsertPre.next
                head.next = nodeToInsert.next
                nodeToInsert.next = nodeToInsertPre.next
                nodeToInsertPre.next = nodeToInsert
            else:
                head = head.next
        return dummy.next


if __name__ == '__main__':
    input = [-1,5,3,4,0]
    head = makeList(input)
    printNode(head)
    Solution().insertionSortList(head)
    printNode(head)
    # [4,2,1,3]

