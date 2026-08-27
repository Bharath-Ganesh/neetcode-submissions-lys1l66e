class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        low = 1
        high = max(piles)
        ans = -1
        while low <= high:
            min_banana = (low + high) // 2
            if self.minEatingSpeedPossible(min_banana, piles, h):
                ans = min_banana
                high = min_banana - 1
            else:
                low = min_banana + 1
        return ans

    def minEatingSpeedPossible(self, min_banana, piles, h):
        total_hours = 0
        for pile in piles:
            total_hours += (pile + (min_banana - 1)) // min_banana
        return total_hours <= h