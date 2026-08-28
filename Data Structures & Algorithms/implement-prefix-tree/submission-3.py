class TreeNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()
        
    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            key = ord(c) - 97
            if not cur.children[key]:
                cur.children[key] = TreeNode()
            cur = cur.children[key]
        cur.endOfWord = True


    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            key = ord(c) - 97
            if not cur.children[key]:
                return False
            cur = cur.children[key]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            key = ord(c) - 97
            if not cur.children[key]:
                return False
            cur = cur.children[key]
        return True
        
        