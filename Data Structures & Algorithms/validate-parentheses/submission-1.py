class Solution:
    def isValid(self, s: str) -> bool:
        stack = [None] * len(s)
        match = {']': '[', '}': '{', ')': '('}
        i = 0
        for p in s:
            if p in ('[', '{', '('):
                stack[i] = p
                i += 1
            elif i and stack[i-1] == match[p]:
                i -= 1
            else:
                return False
        return i == 0
