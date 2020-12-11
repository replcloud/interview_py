class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        st = []
        for c in S:
            if st and c == st[-1]:
                st.pop()
            else:
                st += c
        return ''.join(st)