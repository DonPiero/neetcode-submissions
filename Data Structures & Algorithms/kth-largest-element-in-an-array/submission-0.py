class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        res = []
        for n in nums:
            maxHeap.append(-n)

        heapq.heapify(maxHeap)
        k -= 1
        while k:
            heapq.heappop(maxHeap)
            k -= 1

        return -1 * heapq.heappop(maxHeap)