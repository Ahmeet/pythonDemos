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
    
    # O(n) worst case, O(log n) average case, O(h) always -hegiht
    def __contains__(self, key):
        currentNode = self.root

        while currentNode is not None:
            if key < currentNode.key:
                currentNode = currentNode.left
            elif key > currentNode.key:
                currentNode = currentNode.right
            else:
                return True

    # o(n) - linear time
    def __iter__(self):
        yield from self._inOrderTraversal(self.root)

    # o(n) - linear time
    def __repr__(self):
        return str(list(self._inOrderTraversal(self.root)))

    # O(n) worst case, O(log n) average case, O(h) always -hegiht
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
                    if currentNode.right is None:
                        currentNode.right = Node(key)
                        currentNode.right.value = value
                        currentNode.right.parent = currentNode
                        break
                    else:
                        currentNode = currentNode.right
                else:
                    currentNode.value = value
                    break

    # O(n) worst case, O(log n) average case, O(h) always -hegiht
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

    # O(n) worst case, O(log n) average case, O(h) always -hegiht
    def delete (self, key):
        node = self.search(key)

        if node is None:
            raise KeyError("Node with this key does not exist!")
        self._delete(node)

    # O(n) linear time
    def traverse(self, order):
        if order == "inorder":
            yield from self._inOrderTraversal(self.root)
        elif order == "preorder":
            yield from self._preOrderTraversal(self.root)
        elif order == "postorder":
            yield from self._postOrderTraversal(self.root)
        else:
            raise ValueError("Unknown order!")

    def _delete(self, node):
        # Node is leaf node
        if node.left is None and node.right is None:
            if node.parent is None:
                self.root = None
            else:
                if node.parent.right == node:
                    node.parent.right = None
                else:
                    node.parent.left = None
                node.parent = None

        # Node has one child node
        elif node.left is None or node.right is None:
            childNode = node.left if node.left is not None else node.right
            if node.parent is None:
                childNode.parent = None
                self.root = childNode
            else:
                if node.parent.right == node:
                    node.parent.right = childNode
                else:
                    node.parent.left = childNode
                childNode.parent = node.parent
            node.parent = node.left = node.right = None

        # Node has two children nde
        else:
            successor = self._successor(node)

            node.key = successor.key
            node.value = successor.value
            self._delete(successor)

    def _successor(self, node):
        if node is None:
            raise ValueError(" Cannot find successor of None!")
        
        if node.right is None:
            return None
        else:
            currentNode = node.right
            while currentNode.left is not None:
                currentNode = currentNode.left
            return currentNode

    def _predecessor(self, node):
        if node is None:
            raise ValueError(" Cannot find predecessor of None!")
        
        if node.left is None:
            return None
        else:
            currentNode = node.left
            while currentNode.right is not None:
                currentNode = currentNode.right
            return currentNode

    def _inOrderTraversal(self, node):
        # left root right
        if node is not None:
            yield from self._inOrderTraversal(node.left)
            yield (node.key, node.value)
            yield from self._inOrderTraversal(node.right)

    def _preOrderTraversal(self, node):
        # root left rigt
        if node is not None:
            yield (node.key, node.value)
            yield from self._preOrderTraversal(node.left)
            yield from self._preOrderTraversal(node.right)

    def _postOrderTraversal(self, node):
        # left right root
        if node is not None:
            yield from self._postOrderTraversal(node.left)
            yield from self._postOrderTraversal(node.right)
            yield (node.key, node.value)

def main():
    bst = BinarySearchTree()

    bst.insert(10, "x")
    bst.insert(5, "x")
    bst.insert(22, "x")
    bst.insert(2, "x")
    bst.insert(9, "x")
    bst.insert(12, "x")
    bst.insert(30, "x")
    bst.insert(11, "x")
    bst.insert(15, "x")
    bst.insert(30, "x")
    bst.insert(23, "x")
    bst.insert(35, "x")

    bst.delete(22)

    for i in bst.traverse("preorder"):
        print(i)
    
    print(bst)

    print(bst.search(30))

if __name__ == "__main__":
    main()