# left child of a node is 2 * index + 1
# right child of a node is 2 * index + 2
# parent of a node is (index - 1) // 2 if index != 0

class MinHeap:
    
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def __repr__(self):
        return str(self.heap)

    # O(h) = O(log n) -h is height
    def insert(self, key, value):
        self.heap.append([key, value])
        self._siftUp(len(self.heap) - 1)

    # O(1) - constant time
    def peekMin(self):
        if not self.heap:
            raise IndexError("Empty Heap")
        else:
            return self.heap[0]

    # O(h) = O(log n) -h is height
    def extractMin(self):
        if not self.heap:
            raise IndexError("Empty Heap")
        minElement = self.heap[0]
        lastElement = self.heap.pop()

        if self.heap:
            self.heap[0] = lastElement
            self._siftDown(0)
        
        return minElement

    # O(n) - linear time
    def heapify(self, elements):
        self.heap = list(elements)

        for i in reversed(range(self._parent(len(self.heap) - 1 ) + 1)):
            self._siftDown(i)

    # O(n) - linear time
    def meld(self, otherHeap):
        combinedHeap = self.heap + otherHeap.heap

        self.heapify(combinedHeap)

        otherHeap.heap = []

    # O(1) - constant time
    def _parent(self, index):
        return (index - 1) // 2 if index != 0 else None

    # O(1) - constant time
    def _left(self, index):
        left = (2 * index) + 1
        return left if left < len(self.heap) else None

    # O(1) - constant time
    def _right(self, index):
        right = (2 * index) + 2
        return right if right < len(self.heap) else None

    # O(log n) -logarithmic time
    def _siftUp(self, index):
        # Called swim operation
        parentIndex = self._parent(index)

        while (parentIndex is not None) and (self.heap[index][0] < self.heap[parentIndex][0]):
            self.heap[index], self.heap[parentIndex] = self.heap[parentIndex], self.heap[index]
            index = parentIndex
            parentIndex = self._parent(index)

    # O(log n) -logarithmic time
    def _siftDown(self, index):
        # Called sink operation
        while True:
            smallest = index
            left = self._left(index)
            right = self._right(index)

            if left is not None and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left

            if right is not None and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right

            if smallest == index:
                break
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest

def main():
    minHeap = MinHeap()
    minHeap.heapify([[10, "10"], [9, "9"], [8, "8"], [7, "7"], [6, "6"], [5, "5"],
                     [4, "4"], [3, "3"], [2, "2"], [1, "1"]])
    
    print(minHeap)

    # Heap in python
    import heapq
    myList = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    heapq.heapify(myList)
    print(myList)

    print(minHeap.extractMin())
    print(minHeap.extractMin())
    print(minHeap.extractMin())

    print(heapq.heappop(myList))
    print(heapq.heappop(myList))
    print(heapq.heappop(myList))

    minHeap.insert(2, "2")
    print(minHeap)

    heapq.heappush(myList, 2)
    print(myList)

    minHeap2 = MinHeap()
    minHeap2.heapify([[5, "5"], [7, "7"], [2, "2"]])
    minHeap.meld(minHeap2)
    print(minHeap)

class MaxHeap:
    pass

if __name__ == "__main__":
    main()
