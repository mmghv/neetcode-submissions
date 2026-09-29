class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if len(s2) < n: return False

        freq, noneZeroCount = [0]*26, 0
        for c in s1: freq[ord(c)-ord('a')] += 1
        for f in freq: noneZeroCount += 0 if f == 0 else 1

        for i in range(len(s2)):
            i2 = ord(s2[i])-ord('a')
            if freq[i2] == 0: noneZeroCount += 1
            freq[i2] -= 1
            if freq[i2] == 0: noneZeroCount -= 1

            if i >= n-1:
                if noneZeroCount == 0: return True

                i3 = ord(s2[i-(n-1)]) - ord('a')
                if freq[i3] == 0: noneZeroCount += 1
                freq[i3] += 1
                if freq[i3] == 0: noneZeroCount -= 1

        return False
