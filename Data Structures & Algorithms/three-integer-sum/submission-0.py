from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = set()
        m = defaultdict(list)
        for i, num in enumerate(nums):
            m[num].append(i)

        for i, num1 in enumerate(nums):
            for j in range(i+1, len(nums)):
                num2 = nums[j]
                num3 = 0 - (num1+num2)
                if any(k != i and k != j for k in m[num3]):
                    s.add(tuple(sorted([num1, num2, num3])))
        return [list(triplets) for triplets in s]