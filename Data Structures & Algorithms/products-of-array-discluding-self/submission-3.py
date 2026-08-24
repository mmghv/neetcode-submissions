# O(n) prefix/suffix
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProducts = [1] * len(nums)
        suffixProducts = [1] * len(nums)

        prod = 1
        for i in range(len(nums)):
            prefixProducts[i] *= prod
            prod *= nums[i]
        
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            suffixProducts[i] *= prod
            prod *= nums[i]

        return [prefixProducts[i] * suffixProducts[i] for i in range(len(nums))]