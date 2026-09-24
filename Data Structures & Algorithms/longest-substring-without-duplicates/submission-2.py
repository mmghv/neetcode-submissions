class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        start, maxLen = 0, 0
        for i, c in enumerate(s):
            found = m.get(c, -1)
            if found >= start:
                maxLen = max(maxLen, i-start)
                start = found+1
            m[c] = i
        return max(maxLen, len(s)-start)