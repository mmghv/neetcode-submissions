# O(n) no division
from collections import Counter
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        products = {}
        product = 1

        for num, f in counts.items():
            if f > 1:
                product *= num ** (f-1)
        
        for num in counts:
            otherProduct = 1
            for num2 in counts:
                if num != num2: otherProduct *= num2
            products[num] = product * otherProduct
            
        return [products[num] for num in nums]