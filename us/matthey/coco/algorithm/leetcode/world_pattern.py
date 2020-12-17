class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        d = dict()
        for p in pattern:
            if p not in d:
                if words[0] in d.values():
                    return False
                d[p] = words[0]
            else:
                if d[p] != words[0]:
                    return False
            words = words[1:]
        return True if len(words) == 0 else False
    
if __name__ == '__main__':
    p = "abba"
    # s = "dog cat cat dog"
    s = "dog dog dog dog"
    print(Solution().wordPattern(p, s))