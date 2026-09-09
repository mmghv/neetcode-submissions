# short-circuit improvement
class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        start, end = 0, len(nums)-1
        while start <= end:
            if nums[start] < nums[end]:
                return min(res, nums[start])
            mid = (start + end) // 2
            if nums[mid] < res:
                res = nums[mid]
                end = mid-1
            else:
                start = mid+1
        return res
