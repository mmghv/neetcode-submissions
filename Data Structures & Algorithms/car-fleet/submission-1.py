class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [car for car in zip(position, speed)]
        cars.sort(reverse=True)
        fleets = []
        for car in cars:
            arrive_after = (target - car[0]) / car[1]
            if len(fleets) == 0 or arrive_after > fleets[-1]:
                fleets.append(arrive_after)
        return len(fleets)