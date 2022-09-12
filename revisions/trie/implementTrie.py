# trie is just a tree of characters


class Node:
    def __init__(self):
        self.children = {}
        self.isWord = {}


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:

        curr = self.root

        for c in word:

            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]

        curr.isWord = True

    def search(self, word: str) -> bool:

        curr = self.root

        for c in word:

            if c not in curr.children:
                return False
            curr = curr.children[c]

        return curr.isWord

    def startsWith(self, prefix: str) -> bool:

        curr = self.root

        for c in prefix:

            if c not in curr.children:
                return False
            curr = curr.children[c]

        return True
