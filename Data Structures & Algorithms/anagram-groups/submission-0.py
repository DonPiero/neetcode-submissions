class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictio = {}

        for s in strs:
            helper = [0] * 26
            for i in s:
                helper[ord(i) - ord('a')] += 1
            helper = tuple(helper)
            if helper in dictio:
                dictio[helper].append(s)
            else:
                dictio[helper] = [s]

        result = []
        for i in dictio.values():
            result.append(i)
        
        return result


