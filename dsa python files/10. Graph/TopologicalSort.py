from collections import defaultdict
class Graph:
    def __init__(self, numberOfVertices) -> None:
        self.graph = defaultdict(list)
        self.numberOfVertices = numberOfVertices

    def addVertex(self, vertex):
        self.graph[vertex] = []

    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def topologicalSortUtil(self, vertex, visited, stack):
        # util fn to iterate through the nodes
        #mark node as visited
        visited.append(vertex)

        for i in self.graph[vertex]:
            # go deep till end
            if i not in visited:
                visited.append(i)
        
        # push to stack
        stack.insert(0, vertex)

    def topologicalSort(self, vertex):

        visited = []
        stack = []
        
        for key in list(self.graph): # iterate through keys to cover if any left out 
            self.topologicalSortUtil(key, visited, stack)

        print(f"sorted: {stack}")


customGraph = Graph(5)
customGraph.addVertex('A')
customGraph.addVertex('B')
customGraph.addVertex('C')
customGraph.addVertex('D')
customGraph.addVertex('E')
customGraph.addEdge('A', 'B')
customGraph.addEdge('A', 'C')
# customGraph.addEdge('B', 'A')
customGraph.addEdge('B', 'D')
customGraph.addEdge('B', 'E')
customGraph.addEdge('C', 'D')
customGraph.addEdge('D', 'E')

print(customGraph.graph)

print("-----")

print(customGraph.topologicalSort('A'))


# time: O(V+E)
# space: O(V+E) since we've created two lists to insert all vertices and indices