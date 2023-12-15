# Single Source Shortest Path Problem 

# using BFS

# traverse through all vertices through its adjacent ele like in BFS
# mark the node as visited while dequeuing 
# update the parent of the vertex to currVertex
# this way, even if there're multiple paths to a node, the parent gets updated when we reached to this node frst time, so to 
# find the shortest path, go backtracking parents and indeed will find the shortes path

class Graph:
    def __init__(self, gdict=None) -> None:
        if gdict:
            self.gdict = gdict
        else:
            self.gdict = {}

    def sssp_bfs(self, start, end):
        # start to end find shortest route
        queue = []
        queue.append([start])
        while queue: # O(V)
            # get frst ele out of queue
            path = queue.pop(0)
            # get last node in path if path contains multiple nodes and chekc if we reached end  
            # so get 
            node = path[-1]
            if node == end:
                # i.e if we have reached end
                return path
            for adjacent in self.gdict.get(node, []): #O(E)
                # get adjacent nodes of curr vertex
                new_path = list(path)
                # append the adjacent node to new path 
                new_path.append(adjacent)
                # append the whole path of nodes to queue
                queue.append(new_path)



customdict = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': ['E'], 'E': []}
customGraph = Graph(customdict)
print(customGraph.sssp_bfs('A', 'B'))
print(customGraph.sssp_bfs('A', 'D'))
print(customGraph.sssp_bfs('A', 'E'))

# Time: O(E)
# because in case of sssp, we visit only connected vertices, not any isolated vertices
# Space: O(E) since we're inserting edges and vertices, number of edges are more than vertices.