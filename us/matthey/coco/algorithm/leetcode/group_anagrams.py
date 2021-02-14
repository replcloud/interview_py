import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        amap = collections.defaultdict(list)
        for s in strs:
            amap[''.join(sorted(s))].append(s)
        print(amap)
        return [v for v in amap.values()]
