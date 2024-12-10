class Node:

    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.previous = None


class LinkedList:
    
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __repr__(self) -> str:
        if self.head is None:
            return "[]"
        else:
            last = self.head
            
            returnString = f"{last.value}"
            
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
                        last.next = last.next.next
                        break
                    last = last.next
                    
    # O(n) - linear time                
    def pop(self, index):
        if self.head is None:
            raise ValueError("Index out of bounds")
        else:
            last = self.head
            
            for i in range(index-1):
                if last.next is None:
                    raise ValueError("Index out of bounds")
                last = last.next
            
            if last.next is None:
                raise ValueError("Index out of bounds")
            else:
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
    pass