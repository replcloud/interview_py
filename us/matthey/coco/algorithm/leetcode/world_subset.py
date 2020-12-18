from collections import Counter
from typing import List

from collections import Counter

from collections import Counter


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        # res = []
        # cntA = {}
        # for a in A:
        #     cntA[a] = Counter(a)
        # for a in A:
        #     subset = True
        #     for b in B:
        #         cnt = Counter(b)
        #         for key in cnt.keys():
        #             if key not in cntA[a].keys():
        #                 subset = False
        #                 break
        #             if cnt[key] > cntA[a][key]:
        #                 subset = False
        #                 break
        #         if subset is False:
        #             break
        #     if subset is True:
        #         res.append(a)
        # return res

        def get_required_char_counts(B: List[str]):
            required_char_counter = Counter()
            for b in B:
                b_counter = Counter(b)
                for letter in b_counter:
                    required_char_counter[letter] = max(required_char_counter[letter], b_counter[letter])
            return required_char_counter

        required_char_counter = get_required_char_counts(B)
        res = []
        for a in A:
            is_subset = True
            aCounter = Counter(a)
            for letter in required_char_counter:
                if aCounter[letter] < required_char_counter[letter]:
                    is_subset = False
                    break
            if is_subset:
                res.append(a)
        return res
    

if __name__ == '__main__':
    A = ["amazon", "apple", "facebook", "google", "leetcode"]
    B = ["e", "o"]
    print(Solution().wordSubsets(A, B))
