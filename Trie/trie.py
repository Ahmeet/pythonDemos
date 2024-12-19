# Trie = Prefix Tree = retrieval

class Node:

    def __init__(self):
        self.children = dict()
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    # O(m) - linear time -m is the length of the word
    def insert(self, word):
        currentNode = self.root
        
        for c in word:
            if c not in currentNode.children:
                currentNode.children[c] = Node()

            currentNode = currentNode.children[c]
        
        currentNode.isEndOfWord = True

    # O(m) - linear time -m is the length of the word
    def search(self, word):
        currentNode = self.root

        for c in word:
            if c not in currentNode.children:
                return False
            
            currentNode = currentNode.children[c]
        
        return currentNode.isEndOfWord
    
    # O(m) - linear time -m is the length of the word
    def delete(self, word):
        self._delete(self.root, word, 0)

    # O(m) - linear time -m is the length of the word
    def hasPRefix(self, prefix):
        currentNode = self.root

        for c in prefix:
            if c not in currentNode.children:
                return False
            currentNode = currentNode.children[c]
        
        return True
    
    # O(m + k) - linear time -m is the length of the word -k is the total number of characters in all suffixes
    def startsWith(self, prefix):
        words = []
        currentNode = self.root

        for c in prefix:
            if c not in currentNode.children:
                return words
            currentNode = currentNode.children[c]
        
        def _dfs(currentNode, path):
            if currentNode.isEndOfWord:
                words.append("".join(path))
            for c, childNode in currentNode.children.items():
                _dfs(childNode, path + [c])

        _dfs(currentNode, list(prefix))

        return words
    
    #(n) - linear time -n is the number of nodes in the Trie
    def listWords(self):
        words = []

        def _dfs(currentNode, path):
            if currentNode.isEndOfWord:
                words.append("".join(path))
            for c, childNode in currentNode.children.items():
                _dfs(childNode, path + [c])

        _dfs(self.root, [])

        return words


    def _delete(self, currentNode, word, index):
        if index == len(word):
            if not currentNode.isEndOfWord:
                return False
            
            currentNode.isEndOfWord = False

            return len(currentNode.children) == 0
        
        c = word[index]
        node = currentNode.children.get(c)

        if node is None:
            return False
        
        deleteCurrentNode = self._delete(node, word, index + 1)
        if deleteCurrentNode:
            del currentNode.children[c]
            return len(currentNode.children) == 0 and not currentNode.isEndOfWord
        
        return False
        



def main():
    trie = Trie()

    trie.insert("hello")
    trie.insert("henry")
    trie.insert("mike")
    trie.insert("minimal")
    trie.insert("minimum")

    print(trie.listWords())

    print(trie.hasPRefix("mi"))

    print(trie.startsWith("mi"))

    trie.delete("minimal")

    print(trie.startsWith("mi"))

    print(trie.search("minimum"))
    print(trie.search("minimal"))
    print(trie.search("mini"))

    trie.insert("mini")

    print(trie.startsWith("mi"))

if __name__ == "__main__":
    main()
