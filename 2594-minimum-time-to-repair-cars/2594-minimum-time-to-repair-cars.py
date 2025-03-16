class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
    
        left, right = 1, min(ranks) * cars * cars
        result = right

        while left <= right:
            mid = (left + right) // 2
            total_cars = 0

            for rank in ranks:
               
                max_cars = int(math.isqrt(mid // rank))
                total_cars += max_cars

            if total_cars >= cars:
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result

            