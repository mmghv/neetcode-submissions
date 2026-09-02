from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        for i, num1 in enumerate(nums):
            if num1 > 0: break
            for j in range(i+1, len(nums)):
                num2 = nums[j]
                num3 = 0 - (num1+num2)
                if num3 < num2: break
                # binary search
                kMin, kMax = j+1, len(nums)-1
                while kMax >= kMin:
                    k = kMin + (kMax-kMin)//2
                    diff = num3 - nums[k]
                    if diff == 0:
                        res.add((num1, num2, num3))
                        break
                    elif diff > 0: kMin = k if k > kMin else k+1
                    else: kMax = k if k < kMax else k-1
                
        return [list(triplets) for triplets in res]