class Solution:
    def isHappy(self, n: int) -> bool:
        antiLoop = set()
        while n != 1:
            sum = 0
            while n:
                helper = n % 10
                sum += (helper * helper)
                n = n // 10
            if sum in antiLoop:
                return False
            else: 
                antiLoop.add(sum)
                n = sum 
        return True
        