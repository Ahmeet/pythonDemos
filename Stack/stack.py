class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:

    def __init__(self):
        self.top = None
        self.size = 0
    
    # O(1) - constant time
    def __len__(self):
        return self.size
    
    # O(n) - linear time
    def __repr__(self):
        items = []

        currentItem = self.top

        while currentItem is not None:
            items.append(str(currentItem.value))
            currentItem = currentItem.next

        return ", ".join(items)

    # O(1) - constant time
    def push(self, value):
        newNode = Node(value)
        newNode.next = self.top
        self.top = newNode
        self.size += 1

    # O(1) - constant time
    def pop(self):
        if self.top is None:
            raise ValueError("Stack is empty!")
        
        popValue = self.top.value
        self.top = self.top.next

        self.size -= 1

        return popValue
    
    # O(1) - constant time
    def peek(self):
        if self.top is None:
            raise ValueError("Stack is empty!")
        
        return self.top.value

    # O(1) - constant time
    def isEmpty(self):
        return self.top is None

def main():
    stack = Stack()

    stack.push(10)
    stack.push(14)
    stack.push(16)
    stack.push(6)
    stack.push(12)

    print(stack)

    print(stack.peek())

    print(stack.isEmpty())

    print(stack.pop())
    print(stack)
    print(stack.pop())
    print(stack)
    print(stack.pop())
    print(stack)
    print(stack.pop())
    print(stack)
    print(stack.pop())
    print(stack)

    print(stack.isEmpty())

if __name__ == "__main__":
    main()



