from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = defaultdict(int)
        freqMap = defaultdict(list)
        res = []
        for num in nums:
            numMap[num] += 1
        for num in numMap:
            freqMap[numMap[num]].append(num)
        
        for f in range(len(nums), 0, -1):
            if f in freqMap:
                res.extend(freqMap[f])
            if len(res) >= k: break

        return res