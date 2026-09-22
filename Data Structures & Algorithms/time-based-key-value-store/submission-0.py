from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        vals = self.map[key]
        l, r = 0, len(vals)-1
        found = -1
        while l <= r:
            mid = l + ((r-l)//2)
            ts = vals[mid][0]
            if timestamp < ts:
                r = mid-1
            else:
                found = mid
                if timestamp == ts:
                    break
                else:
                    l = mid+1
        return "" if found < 0 else vals[found][1]
