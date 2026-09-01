class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i, j = 0, len(s) - 1
        while i < j:
            while (ord(s[i]) < ord('A') or ord(s[i]) > ord('Z')) and (ord(s[i]) < ord('a') or ord(s[i]) > ord('z')) and (ord(s[i]) < ord('0') or ord(s[i]) > ord('9')) and i < j: 
                i += 1
            while (ord(s[j]) < ord('A') or ord(s[j]) > ord('Z')) and (ord(s[j]) < ord('a') or ord(s[j]) > ord('z')) and (ord(s[j]) < ord('0') or ord(s[j]) > ord('9')) and i < j: 
                j -= 1
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
            
        return True
