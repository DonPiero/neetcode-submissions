class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        
        while digits[i] == 9:
            if i == 0:
                digits[i] = 0
                return [1] + digits
            digits[i] = 0
            i -= 1
        
        digits[i] += 1
        return digits
