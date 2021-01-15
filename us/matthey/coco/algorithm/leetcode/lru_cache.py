from collections import OrderedDict, deque


class LRUCache:
    # Implement with deque 496 ms 23.3 MB
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.q = deque()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.q.remove(key)
            self.q.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.q.remove(key)
        self.cache[key] = value
        self.q.append(key)
        if len(self.q) > self.capacity:
            evicted = self.q.popleft()
            del self.cache[evicted]

    """
    # Implement with OrderedDict 176 ms 23.3 MB
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
    """

if __name__ == '__main__':
    c = LRUCache(2)
    c.put(2, 1)
    c.put(2, 2)
    print(c.get(2))
    c.put(1, 1)
    c.put(4, 1)
    print(c.get(2))
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)