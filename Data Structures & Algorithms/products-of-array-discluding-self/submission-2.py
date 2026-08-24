# O(n) no division
from collections import Counter
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numMap = Counter(nums)
        initialProduct = 1

        for num, f in numMap.items():
            if f > 1:
                initialProduct *= num ** (f-1)
        
        for num in numMap:
            remainingProduct = 1
            for num2 in numMap:
                if num != num2: remainingProduct *= num2
            numMap[num] = initialProduct * remainingProduct
            
        return [numMap[num] for num in nums]