class Graph:

    def __init__(self, directed=False):
        self.directed = directed
        self.adjList = dict()
    
    def __repr__(self):
        graphStr = ""

        for node, neighbors in self.adjList.items():
            graphStr += f"{node} -> {neighbors}\n"
        return graphStr

    def addNode(self, node):
        if node not in self.adjList:
            self.adjList[node] = set()
        else:
            raise ValueError("Node exists already!")

    def removeNode(self, node):
        if node not in self.adjList:
            raise ValueError("Node does not exist!")
        
        for neighbors in self.adjList.values():
            neighbors.discard(node)
        
        del self.adjList[node]

    def addEdge(self, fromNode, toNode, weight=None):
        if fromNode not in self.adjList:
            self.addNode(fromNode)

        if toNode not in self.adjList:
            self.addNode(toNode)

        if weight is None:
            self.adjList[fromNode].add(toNode)
            if not self.directed:
                self.adjList[toNode].add(fromNode)
        else:
            self.adjList[fromNode].add((toNode, weight))
            if not self.directed:
                self.adjList[toNode].add((fromNode, weight))

    def removeEdge(self, fromNode, toNode):
        if fromNode in self.adjList:
            if toNode in self.adjList[fromNode]:
                self.adjList[fromNode].remove(toNode)
            else:
                raise ValueError("Edge does noy exist!")
            
            if not self.directed:
                if fromNode in self.adjList[toNode]:
                    self.adjList[toNode].remove(fromNode)
        else:
            raise ValueError("Edge does not exist")

    def getNeighbors(self, node):
        return self.adjList.get(node, set())

    def hasNode(self, node):
        return node in self.adjList

    def hasEdge(self, fromNode, toNode):
        if fromNode in self.adjList:
            return toNode in self.adjList[fromNode]
        return False

    def getNodes(self):
        return list(self.adjList.keys())

    def getEdges(self):
        edges = []

        for fromNode, neighbors in self.adjList.items():
            for toNode in neighbors:
                edges.append(fromNode, toNode)

    def bfs(self, start):
        visited = set()
        queue = [start]
        order = []

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                order.append(node)
                neighbors = self.getNeighbors(node)
                for neighbor in neighbors:
                    if isinstance(neighbor, tuple):
                        neighbor = neighbor[0]
                    if neighbor not in visited:
                        queue.append(neighbor)
        
        return order


    def dfs(self, start):
        visited = set()
        stack = [start]
        order = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                order.append(node)
                neighbors = self.getNeighbors(node)
                for neighbor in sorted(neighbors, reverse=True):
                    if isinstance(neighbor, tuple):
                        neighbor = neighbor[0]
                    if neighbor not in visited:
                        stack.append(neighbor)
        
        return order
    
    def dijkstra(self, start):
        import heapq
        distances = {node: float("inf") for node in self.adjList}
        distances[start] = 0
        heap = [(0, start)]

        while heap:
            currentDistance, currentNode = heapq.heappop(heap)
            if currentDistance > distances[currentNode]:
                continue
            neighbors = self.adjList.get(currentNode, set())
            for neighbor in neighbors:
                if isinstance(neighbor, tuple):
                    to, weight = neighbor
                else:
                    to, weight = neighbor, 1
                distance = currentDistance + weight
                if distance < distances[to]:
                    distances[to] = distance
                    heapq.heappush(heap, (distance, to))
        return distances

    def shortestPath(self, start, end):
        import heapq
        distances = {node: float("inf") for node in self.adjList}
        previous = {node: None for node in self.adjList}
        distances[start] = 0
        heap = [(0, start)]
        while heap:
            currentDistance, currentNode = heapq.heappop(heap)
            if currentDistance > distances[currentNode]:
                continue
            neighbors = self.adjList.get(currentNode, set())
            for neighbor in neighbors:
                if isinstance(neighbor, tuple):
                    to, weight = neighbor
                else:
                    to, weight = neighbor, 1
                distance = currentDistance + weight
                if distance < distances[to]:
                    distances[to] = distance
                    previous[to] = currentNode
                    heapq.heappush(heap, (distance, to))
        
        path = []
        node = end
        while node is not None:
            path.append(node)
            node = previous.get(node)
        path.reverse()
        if path[0] == start:
            return path
        return []

    def toAdjMatrix(self):
        nodes = self.getNodes()
        index = {node: i for i, node in enumerate(nodes)}
        size = len(nodes)
        matrix = [[0 for _ in range(size)] for _ in range(size)]

        for fromNode, neighbors in self.adjList.items():
            for toNode in neighbors:
                if isinstance(toNode, tuple):
                    to, weight = toNode
                    matrix[index[fromNode]][index[to]] = weight
                else:
                    matrix[index[fromNode]][index[toNode]] = 1
        return matrix

def main():
    graph = Graph(directed=True)

    #graph.addNode("A")
    #graph.addNode("B")
    #graph.addNode("C")
    #graph.addNode("D")
    #graph.addNode("E")
    #graph.addNode("F")
    #graph.addNode("G")
    #graph.addNode("H")
    #graph.addNode("I")
#
    graph.addEdge("A", "B", 1)
    graph.addEdge("A", "C", 10)
    graph.addEdge("B", "C", 1)
    graph.addEdge("B", "D", 1)
    graph.addEdge("D", "C", 1)
    graph.addEdge("A", "E", 1)
    graph.addEdge("E", "F", 1)
    graph.addEdge("G", "F", 1)
    graph.addEdge("F", "H", 1)
    graph.addEdge("H", "I", 1)
    graph.addEdge("I", "G", 100)

    print(graph)

    import numpy as np

    print(np.array(graph.toAdjMatrix()))

    print("BFS From A:", graph.bfs("A"))
    print("DFS From A:", graph.dfs("A"))
    print("Dijkstra From A:", graph.dijkstra("A"))
    print("Shortest Path From A to C:", graph.shortestPath("A", "C"))


if __name__ == "__main__":
    main()