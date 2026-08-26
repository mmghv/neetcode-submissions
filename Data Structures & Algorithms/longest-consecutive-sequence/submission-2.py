# set
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0

        for num in s:
            if num-1 in s: continue
            seq = 1
            while num+seq in s: seq += 1
            longest = max(longest, seq)
        return longest

