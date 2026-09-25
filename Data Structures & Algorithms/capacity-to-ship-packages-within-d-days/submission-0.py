class Solution:
    def shipWithinDays(self, weights, days):
        low = max(weights)
        high = sum(weights)

        while low < high:
            mid = (low + high) // 2

            current = 0
            required_days = 1

            for weight in weights:
                if current + weight > mid:
                    required_days += 1
                    current = 0

                current += weight

            if required_days <= days:
                high = mid
            else:
                low = mid + 1

        return low