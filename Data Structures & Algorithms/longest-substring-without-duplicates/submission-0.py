class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        maxi, result, l = 0, 0, 0 
        for r in range(len(s)):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
                maxi -= 1
                
            sett.add(s[r])
            maxi += 1
            result = max(maxi, result)
        
        return result
