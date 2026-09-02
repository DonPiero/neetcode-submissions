class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def recursive(word: str, curr: TrieNode()) -> bool:
            if not word:
                return curr.endOfWord
            elif word[0] == '.':
                for i in curr.children.values():
                    if recursive(word[1:], i):
                        return True
                return False
            else:
                if word[0] not in curr.children:
                    return False
                return recursive(word[1:], curr.children[word[0]])

        return recursive(word, self.root)
            

        
