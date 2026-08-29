class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = [(position[i],speed[i]) for i in range(n)]
        cars.sort()
        fleets = []
        for i in range(n-1, -1, -1):
            arrive_after = (target - cars[i][0]) / cars[i][1]
            if len(fleets) == 0 or arrive_after > fleets[-1]:
                fleets.append(arrive_after)
        return len(fleets)