class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.parent = None
        self.key = key
        self.value = None

    def __repr__(self):
        return f"({self.key}, {self.value})"
    
class BinarySearchTree:

    def __init__(self):
        self.root = None

    def __contains__(self, key):
        currentNode = self.root

        while currentNode is not None:
            if key < currentNode.key:
                currentNode = currentNode.left
            elif key > currentNode.key:
                currentNode = currentNode.right
            else:
                return True
    def __iter__(self):
        pass

    def __repr__(self):
        pass

    def insert(self, key, value):
        if self.root is None:
            self.root = Node(key)
            self.root.value = value
        else:
            currentNode = self.root

            while True:
                if key < currentNode.key:
                    if currentNode.left is None:
                        currentNode.left = Node(key)
                        currentNode.left.value = value
                        currentNode.left.parent = currentNode
                        break
                    else:
                        currentNode = currentNode.left
                elif key > currentNode.key:

    def search(self, key):
        currentNode = self.root
        
        while True:
            if currentNode is None or currentNode.key == key:
                return currentNode
            elif key < currentNode.key:
                if currentNode.left is None:
                    return None
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    return None
                else:
                    currentNode = currentNode.right


    def delete (self, key):
        pass

    def traverse(self, order):
        pass

    def _delete(self, key):
        pass

    def _successor(self, node):
        pass

    def _predecessor(self, node):
        pass

    def _inOrderTraversal(self):
        pass

    def _preOrderTraversal(self):
        pass

    def _postOrderTraversal(self):
        pass
