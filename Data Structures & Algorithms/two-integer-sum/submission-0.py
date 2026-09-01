class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        result = [0] * 2
        for i in range(len(nums)):
            if ((target - nums[i] in table)):
                result[0] = table[target - nums[i]]
                result[1] = i
                return result
            table[nums[i]] = i
        