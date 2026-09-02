from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, num1 in enumerate(nums):
            if num1 > 0: break
            if i and num1 == nums[i-1]: continue
            comps = set()
            found = set()

            for j in range(i+1, len(nums)):
                num2 = nums[j]
                num3 = 0 - (num1+num2)

                if num2 in comps and (num2, num3) not in found:
                    res.append([num1, num2, num3])
                    found.add((num2, num3))
                    comps.remove(num2)

                if num3 >= num2: comps.add(num3)

        return res