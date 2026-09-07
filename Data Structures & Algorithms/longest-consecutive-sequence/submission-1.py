class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxi = 0

        for n in numsSet:
            if (n - 1) not in numsSet:
                length = 0
                while (n + length) in numsSet:
                    length += 1
                maxi = max(length, maxi)
        
        return maxi