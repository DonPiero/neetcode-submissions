class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        contor = {}

        if len(s) != len(t):
            return False
            
        for i in s: 
            if i not in contor:
                contor[i] = 0
            contor[i] += 1
        
        for j in t:
            if (j not in contor) or (contor[j] == 0):
                return False
            contor[j] -= 1
        
        return True
            