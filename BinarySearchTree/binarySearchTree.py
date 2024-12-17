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
        pass

    def __iter__(self):
        pass

    def __repr__(self):
        pass

    def insert(self, key, value):
        pass

    def search(self, key):
        pass