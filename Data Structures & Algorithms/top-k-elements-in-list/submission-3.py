class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictio = {}
        for i in nums:
            if i not in dictio:
                dictio[i] = 1
            else:
                dictio[i] += 1
        
        result = [[] for _ in range(len(nums) + 1)]
        for i in dictio:
            result[dictio[i]].append(i)

        final = []
        i = len(result) - 1
        while k:
            if result[i]:
                final.append(result[i].pop())
                k -= 1
            else: 
                i -= 1

        return final


        