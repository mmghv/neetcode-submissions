class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        l, r = 0, len(heights)-1
        while l < r:
            h1 = heights[l]
            h2 = heights[r]
            maxArea = max(maxArea, (r - l) * min(h1, h2))
            if h1 < h2:
                l += 1
            else:
                r -= 1
        return maxArea
