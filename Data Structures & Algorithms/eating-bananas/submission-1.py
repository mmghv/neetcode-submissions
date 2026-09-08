class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 1, max(piles)

        while start <= end:
            k = start + (end - start) // 2
            hours = 0
            for pile in piles:
                hours += -(-pile // k)
            if hours > h:
                start = k+1
            else:
                end = k-1
        return start