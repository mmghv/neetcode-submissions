from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        m = Counter()
        for c in s:
            m[c] = (m[c] if c in m else 0) +1
        for c in t:
            m[c] = (m[c] if c in m else 0) -1
        for c in m:
            if m[c] != 0: return False
        return True

