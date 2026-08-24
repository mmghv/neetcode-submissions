# O(n) With division
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        foundZero = False
        product = 1
        for num in nums:
            if num == 0 and not foundZero:
                foundZero = True
            else:
                product *= num
        return [product if num == 0 else 0 if foundZero else int(product/num) for num in nums]