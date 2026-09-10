class Solution:
    def search(self, nums: List[int], target: int) -> int:
        startIdx, n = 0, len(nums)

        l, r = 0, n-1
        while l <= r:
            if nums[l] < nums[r]:
                if nums[l] < nums[startIdx]: startIdx = l
                break
            mid = (l+r) // 2
            if nums[mid] < nums[startIdx]:
                startIdx = mid
                r = mid-1
            else:
                l = mid+1

        l, r = 0, n-1
        while l <= r:
            mid = (l+r) // 2
            midRotated = (mid + startIdx) % n
            if nums[midRotated] == target:
                return midRotated
            elif nums[midRotated] > target:
                r = mid-1
            else:
                l = mid+1
        return -1