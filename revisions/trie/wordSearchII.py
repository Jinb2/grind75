class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):

        curr = self

        for c in word:

            if c not in curr.children:
                curr.children[c] = TrieNode()

            curr = curr.children[c]

        curr.isWord = True


class Solution:
    # use a trie to help us with word search
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # create our starting point
        root = TrieNode()

        # add the words to trie
        for w in words:
            root.addWord(w)

        rows, cols = len(board), len(board[0])
        # all the words we find
        res = []

        # we keep track of the row col we are at
        # the current character we are at and so far how many words we are able to construct
        def dfs(r, c, node, word):

            # base case if its not in bounds
            if (
                r not in range(rows)
                or c not in range(cols)
                or board[r][c] not in node.children
            ):
                return

            # move to the next char
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.isWord:
                res.append(word)
                # we might reach thsi word again so we dont want dupes
                node.isWord = False

            # mark as visited
            tmp = board[r][c]
            board[r][c] = None
            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            # unmark it after our dfs
            board[r][c] = tmp

        for row in range(rows):
            for col in range(cols):
                dfs(row, col, root, "")

        return res
