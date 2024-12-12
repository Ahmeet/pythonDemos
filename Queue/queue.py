class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.front = None
        self.rear = None
        self.size = 0
    
    # O(1) - constant time
    def __len__(self) -> int:
        return self.size
    
    # O(n) - linear time
    def __repr__(self):
        items = []

        currentItem = self.front

        while currentItem is not None:
            items.append(str(currentItem.value))
            currentItem = currentItem.next

        return ", ".join(items)

    # O(1) - constant time
    def enqueue(self, value):
        newNode = Node(value)
        if self.rear is None:
            self.front = self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode
        
        self.size += 1

    # O(1) - constant time
    def dequeue(self):
        if self.front is None:
            raise IndexError("Queue is empty!")
        
        dequeueValue = self.front.value
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        self.size -= 1
        return dequeueValue

    # O(1) - constant time
    def peek(self):
        if self.front is None:
            raise IndexError("Queue is empty!")
        
        return self.front.value

    # O(1) - constant time
    def isEmpty(self):
        return self.front is None

def main():
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.enqueue(50)
    queue.enqueue(60)

    print(queue)

    print(len(queue))
          
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())

    print(queue)
    print(len(queue))

if __name__ == "__main__":
    main()