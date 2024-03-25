# Beats 99.95% Memory

class Solution:
    def isPalindrome(self, x: int) -> bool:
        tmp: int = x
        reversed: int = 0
        while(tmp > 0):
            lastDigit = tmp%10
            tmp -= lastDigit
            reversed = reversed*10 + lastDigit
            tmp = tmp/10
        if (reversed == x):
            return True
        return False