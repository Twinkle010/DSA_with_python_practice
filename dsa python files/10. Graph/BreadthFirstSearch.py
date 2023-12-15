from collections import deque
class Graph():

    def __init__(self) -> None:
        self.adjacency_list = {
            'A': ['B','C'],
            'B': ['A', 'E'],
            'C': ['A', 'D'],
            'D': ['C', 'E'],
            'E': ['B', 'D']
        }

    def bfs(self, vertex):
        # make a set of visited nodes
        visited = set()
        # make a queue of nodes to visit next
        # queue = []
        queue = deque([vertex])
        # current node is visited and in queue to visit its neighbour nodes
        visited.add(vertex)
        queue.append(vertex)
        while queue:   #-> O(V)
            # get neighbours of vertex in quue and keep adding to visited nodes
            # currentVertex = queue.pop(0) -> O(n)
            currentVertex = queue.popleft() # O(1)
            print(f"currentVertex: {currentVertex}")
            adjacent_nodes = self.adjacency_list[currentVertex] #O(2E) since each edge will be visited twice
            for node in adjacent_nodes:
                if node not in visited:
                    visited.add(node)
                    queue.append(node)

    def dfs(self, vertex):
        visited = set()
        stack = []

        stack.append(vertex)
        while stack:    #O(V)
            curr_vertex = stack.pop() #O(1)
            if curr_vertex not in visited: #O(1)
                visited.add(curr_vertex)
                print(f"currentVertex: {curr_vertex}")
            for adjacent_nodes in self.adjacency_list[curr_vertex]: #O(E)
                if adjacent_nodes not in visited:
                    stack.append(adjacent_nodes)


customGraph  = Graph()

customGraph.bfs('A')

print("------")

customGraph.bfs('B')

# time: O(V+E)
print("-------")

customGraph.dfs('A')
#Time: O(V+E)