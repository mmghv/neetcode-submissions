class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if len(s2) < n: return False

        freq, noneZeroCount = [0]*26, 0
        for c in s1:
            i = ord(c) - ord('a')
            if freq[i] == 0: noneZeroCount += 1
            freq[i] += 1

        for i in range(len(s2)):
            inx = ord(s2[i]) - ord('a')
            if freq[inx] == 0: noneZeroCount += 1
            freq[inx] -= 1
            if freq[inx] == 0: noneZeroCount -= 1

            if i >= n-1:
                if noneZeroCount == 0: return True

                inx = ord(s2[i-(n-1)]) - ord('a')
                if freq[inx] == 0: noneZeroCount += 1
                freq[inx] += 1
                if freq[inx] == 0: noneZeroCount -= 1

        return False
