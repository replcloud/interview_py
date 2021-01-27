from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        st = []
        for t in tokens:
            if t not in operators:
                st.append(int(t))
            else:
                if len(st) >= 2:
                    operand2 = st.pop()
                    operand1 = st.pop()
                    if t == "+":
                        res = operand1 + operand2
                    elif t == "-":
                        res = operand1 - operand2
                    elif t == "*":
                        res = operand1 * operand2
                    elif t == "/":
                        if operand1 / operand2 > 0:
                            res = floor(operand1 / operand2)
                        else:
                            res = ceil(operand1 / operand2)
                    st.append(res)
        if st and len(st) == 1: return st[0]

if __name__ == '__main__':
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    tokens = ["4","-2","/","2","-3","-","-"]
    print((Solution().evalRPN(tokens)))