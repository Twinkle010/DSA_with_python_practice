# represent graph using adjacent list
# using python dicts


class Graph():
    def __init__(self, gdict=None) -> None:
        if gdict is None:
            # intialise
            self.gdict = {}
        else:
            self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def addVertex(self, vertex):
        if vertex not in self.gdict.keys():
            self.gdict[vertex] = []
        else:
            print("vertex already exists")
            return
    
    def removeEdge(self, vertex, edge):
        self.gdict[vertex].remove(edge)

    def removeVertex(self, vertex):
        self.gdict.pop(vertex)


customDict = {
    "a": ["b"]
}
customGraph = Graph(customDict)

customGraph.addEdge("a", "c")
customGraph.addVertex("b")
customGraph.addEdge("b", "c")
print(customGraph.gdict)
customGraph.removeEdge("b", "c")
print(customGraph.gdict)
customGraph.removeVertex("b")
print(customGraph.gdict)




## option2:
# adding an edge means connecting between two vertices, so add in both verticces