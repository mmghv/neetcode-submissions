class Solution:
    def isPalindrome(self, s: str) -> bool:
        i1, i2 = 0, len(s)-1
        while i1 < i2:
            if not s[i1].isalnum():
                i1 += 1
                continue
            if not s[i2].isalnum():
                i2 -= 1
                continue
            if s[i1].lower() != s[i2].lower():
                return False
            i1 += 1
            i2 -= 1
        return True