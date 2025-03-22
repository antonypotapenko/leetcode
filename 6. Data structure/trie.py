class TrieNode:

    def __init__(self):
        self.children = {}   #[None for _ in range(26)]
        self.word_count = 0

    def insert(self, root, key):
        cur_node = root

        for char in key:
            if cur_node.childNode[ord(char) - ord('a')] == None:
                new_node = TrieNode()

class Trie:
    pass
