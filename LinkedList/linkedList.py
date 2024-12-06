class Node:

    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    
    def __init__(self) -> None:
        self.head = None

    def __repr__(self) -> str:
        pass

    def __contains__(self):
        pass

    def __len__(self):
        pass

    # O(n) - linear time
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = Node(value)

    # O(1) - constant time
    def prepend(self,value):
        firstNode = Node(value)
        firstNode.next = self.head
        self.head = firstNode

    # O(n) - linear time
    def insert(self, value, index):
        if index == 0:
            self.prepend(value)
        else:
            if self.head is None:
                raise ValueError("Index out of bounds")
            else:
                last = self.head

                for i in range(index-1):
                    if last.next is None:
                        raise ValueError("Index out of bounds")
                    last = last.next
                
                newNode = Node(value)
                newNode.next = last.next
                last.next = newNode

    def delete(self, value):
        pass

    def pop(self, index):
        pass

    def get(self, index):
        pass

    def print(self):
        pass


if __name__ == "__main__":
    pass