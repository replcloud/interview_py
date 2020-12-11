class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        res = []
        opened = 0
        for c in S:
            if c == '(' and opened > 0: res.append(c)
            elif c == ')' and opened > 1: res.append(c)
            opened += 1 if c == '(' else -1
        return "".join(res)