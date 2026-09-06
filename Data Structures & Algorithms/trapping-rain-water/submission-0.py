class Solution:
    def trap(self, height: List[int]) -> int:
        bars = []
        totalAmount = 0
        for i, h in enumerate(height):
            if not h: continue
            processedH = 0
            while bars and processedH < h:
                prevBar = bars[-1]
                prevH = height[prevBar]
                if prevH <= h: bars.pop()
                minH = min(h, prevH)
                if minH > processedH:
                    w = i - prevBar - 1
                    totalAmount += w * (minH - processedH)
                    processedH = minH
            bars.append(i)
        return totalAmount



