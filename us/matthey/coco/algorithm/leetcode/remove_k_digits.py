class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []
        attemps = k
        for c in num:
            while st and int(st[-1]) > int(c) and attemps > 0:
                st.pop()
                attemps -= 1
            st.append(c)
        return "".join(st[:len(num) - k]).lstrip("0") if "".join(st[:len(num) - k]).lstrip("0") != "" else "0"

if __name__ == '__main__':
    num = "1432219"
    k = 3
    print((Solution().removeKdigits(num, k)))