class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        rects = [] # (rx, rh)
        max_area = 0
        n = len(heights)
        h = 0
        for x in range(n+1):
            prev_h = h
            h = heights[x] if x < n else 0
            if h == prev_h: continue
            start = x
            if h < prev_h:
                while rects and h < rects[-1][1]:
                    rx, rh = rects.pop()
                    max_area = max(max_area, rh*(x-rx))
                if rects and rects[-1][1] == h: continue
                for i in range(x-1, -1, -1):
                    if heights[i] < h: break
                    start = i
            if h: rects.append((start, h))
        return max_area