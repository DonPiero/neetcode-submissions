class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1: 
            first = heapq.heappop(stones) * -1
            second = heapq.heappop(stones) * -1
            potential = (first - second) * -1
            if potential < 0:
                heapq.heappush(stones, potential)
        
        if len(stones) > 0:
            return heapq.heappop(stones) * -1
        return 0