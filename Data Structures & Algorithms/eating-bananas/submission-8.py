class Solution:
    def eatSpeed(self, mid: int, piles: List[int]) -> int:
        result = 0 
        for p in piles: 
            if p - mid > 0:
                result += (p // mid)
                if p % mid:
                    result += 1
            else: 
                result += 1
        return result 

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        result = r

        while l <= r:
            mid = l + (r - l) // 2
            speed = self.eatSpeed(mid, piles)
            if speed > h:
                l = mid + 1
            else: 
                result = min(mid, result)
                r = mid - 1
        
        return result