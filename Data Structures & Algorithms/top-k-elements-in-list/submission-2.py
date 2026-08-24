from collections import defaultdict, Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = Counter(nums)
        freqMap = defaultdict(list)
        res = []
        
        for num in numMap:
            freqMap[numMap[num]].append(num)
        
        for f in range(len(nums), 0, -1):
            if f in freqMap:
                res.extend(freqMap[f])
            if len(res) >= k: break

        return res