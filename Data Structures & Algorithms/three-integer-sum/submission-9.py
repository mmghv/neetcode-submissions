# two pointers
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)-2):
            if nums[i] > 0: break
            if i and nums[i] == nums[i-1]: continue
            l, r = i+1, len(nums)-1
            while l < r:
                diff = -nums[i] - (nums[l] + nums[r])
                if diff == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]: l += 1
                elif diff > 0: l += 1
                else: r -= 1
        return res