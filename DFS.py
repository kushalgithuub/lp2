graph={
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '4':['8'],
    '2':[],
    '8':[]
}


visited=set()

def DFS(visited,graph,node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            DFS(visited,graph,neighbour)
print("The DFS traversal is : ")
DFS(visited,graph,'5')       