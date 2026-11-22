# Graph Representation using Dictionary

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Depth First Search (DFS)
def DFS(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=" ")

    for neighbour in graph[start]:
        if neighbour not in visited:
            DFS(graph, neighbour, visited)


# Breadth First Search (BFS)
def BFS(graph, start):
    visited = set()
    queue = [start]

    visited.add(start)

    while queue:
        vertex = queue.pop(0)
        print(vertex, end=" ")

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


print("DFS Traversal:")
DFS(graph, 'A')

print("\nBFS Traversal:")
BFS(graph, 'A')
