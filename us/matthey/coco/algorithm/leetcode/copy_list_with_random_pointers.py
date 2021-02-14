# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return None
        cur = head
        l = []
        d = {}
        count = 0
        while cur:
            if cur not in d:
                nn = Node(cur.val)
                d[cur] = nn
            else:
                nn = d[cur]
            if cur.random:
                if not cur.random in d:
                    nr = Node(cur.random.val)
                    d[cur.random] = nr
                    nn.random = nr
                else:
                    nn.random = d[cur.random]
            l.append(nn)
            if count != 0:
                l[count - 1].next = l[count]
            count += 1
            cur = cur.next
        return l[0]
