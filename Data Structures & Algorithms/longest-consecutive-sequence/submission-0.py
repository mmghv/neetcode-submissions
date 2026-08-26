class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = {}
        longest = 0
        for num in nums:
            if num in m: continue
            seq = 1
            start, end = num, num

            # below
            if num-1 in m:
                seq += m[num-1]
                start -= seq-1
            # above
            if num+1 in m:
                seq += m[num+1]
                end = start + seq - 1

            m[start], m[end], m[num] = seq, seq, seq
            if seq > longest: longest = seq

        return longest

