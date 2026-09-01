class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        contor = [0] * 26

        if len(s) != len(t):
            return False

        for i in range(len(s)): 
            contor[ord(s[i]) - ord('a')] += 1
            contor[ord(t[i]) - ord('a')] -= 1
        
        for j in contor:
            if j != 0:
                return False
        
        return True
            