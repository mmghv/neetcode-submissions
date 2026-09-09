class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        start, end = 0, len(nums)-1
        for i, num in enumerate(nums):
            mid = (start + end) // 2
            if num < res:
                res = num
                start = mid+1
            else:
                end = mid-1
        return res
