class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comps = {}
        idx1, idx2 = 0, 0
        for idx2, num in enumerate(nums):
            idx1 = comps.get(num, -1)
            if idx1>=0: break
            comps[target-num] = idx2
        return [idx1, idx2]


