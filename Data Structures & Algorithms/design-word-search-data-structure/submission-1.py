class Node:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        
        curr.word = True

    def search(self, word: str) -> bool:
        def dfs(i, root):
            curr = root

            for j in range(i, len(word)):
                if word[j] == ".":
                    for child in curr.children.values():
                        if dfs(j + 1, child):
                            return True
                    return False
                else:
                    if word[j] not in curr.children:
                        return False
                    curr = curr.children[word[j]]
            return curr.word
        
        return dfs(0, self.root)
                





