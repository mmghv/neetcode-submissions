class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = 0
        maxPile = 0

        for pile in piles:
            maxPile = max(maxPile, pile)

        start, end = 1, maxPile

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