class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sums = []
        
        def dfs(i, currSum):
            if currSum >= target or i >= len(nums):
                if currSum == target: 
                    res.append(sums.copy())
                return 
            
            sums.append(nums[i])
            dfs(i, currSum + nums[i])

            sums.pop()
            dfs(i + 1, currSum)

        dfs(0, 0)
        return res