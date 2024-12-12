class Node:

    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.previous = None


class DoublyLinkedList:
    
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __repr__(self) -> str:
        if self.head is None:
            return "[]"
        else:
            last = self.head
            
            returnString = f"[{last.value}"
            
            while last.next:
                last = last.next
                returnString += f", {last.value}"
            returnString +="]"
            
            return returnString

    # O(n) - linear time
    def __contains__(self, value):
        last = self.head
        while last is not None:
            if last.value == value:
                return True
            last = last.next
        return False
            
    # O(n) - linear time
    def __len__(self):
        last = self.head
        counter = 0
        while last is not None:
            counter += 1
            last = last.next
        return counter

    # O(1) - constant time
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            lastNode = Node(value)
            lastNode.previous = self.tail
            self.tail.next = lastNode
            self.tail = lastNode

    # O(1) - constant time
    def prepend(self,value):
        if self.head is None:
            self.head = Node(value)
            self.tail = Node(value)
        else:
            firstNode = Node(value)
            firstNode.next = self.head
            self.head.previous = firstNode
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
                newNode.previous = last
                if last.next is not None:
                    last.next.previous = newNode
                last.next = newNode
    
    # O(n) - linear time
    def delete(self, value):
        last = self.head
        
        # we can add else block to raise exception if the list is empty or entered value is not in the list
        if last is not None:
            if last.value == value:
                self.head = last.next
            else:
                while last.next:
                    if last.next.value == value:
                        if last.next.next is not None:
                            last.next.next.previous = last
                        last.next = last.next.next
                        break
                    last = last.next
                    
    # O(n) - linear time                
    def pop(self, index):
        if self.head is None:
            raise ValueError("Index out of bounds")

        else:
            last = self.head
            if index == 0:
                last.next.previous = None
                self.head = last.next
            else:
                for i in range(index-1):
                    if last.next is None:
                        raise ValueError("Index out of bounds")
                    last = last.next
                
                if last.next is None:
                    raise ValueError("Index out of bounds")
                else:
                    if last.next.next is not None:
                        last.next.next.previous = last
                    last.next = last.next.next
                
    # O(n) - linear time
    def get(self, index):
        if self.head is None:
            raise ValueError("Index out of bounds")
        else:
            last = self.head
            for i in range(index):
                if last.next is None:
                    raise ValueError("Index out of bounds")
                last = last.next
            return last.value

if __name__ == "__main__":
    dll = DoublyLinkedList()

    dll.append(10)

    dll.insert(5, 1)
    dll.insert(20, 1)
    dll.insert(18, 1)
    dll.insert(22, 1)
    dll.insert(88, 1)
    dll.insert(97, 1)

    dll.prepend(100)

    dll.insert(200, 1)

    dll.delete(18)
    dll.delete(22)
    dll.delete(5)

    dll.pop(1)
    dll.pop(0)

    print(dll)

    print(dll.get(1))

    print(29 in dll)
    print(800 in dll)