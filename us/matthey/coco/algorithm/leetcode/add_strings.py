class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # Use recursion
        if len(num1) == 0: return num2
        if len(num2) == 0: return num1
        sum = int(num1[-1]) + int(num2[-1])
        carry = sum // 10
        if carry != 0:
            return self.addStrings(self.addStrings(num1[:-1], num2[:-1]), str(carry)) + str(sum % 10)
        return self.addStrings(num1[:-1], num2[:-1]) + str(sum % 10)