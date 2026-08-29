class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [car for car in zip(position, speed)]
        cars.sort(reverse=True)
        fleets = 0
        last_time = -1
        for p, s in cars:
            time = (target - p) / s
            if time > last_time:
                last_time = time
                fleets += 1
        return fleets
