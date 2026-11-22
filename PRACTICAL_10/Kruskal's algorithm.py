
def kruskal(edges, vertices):
    edges.sort()

    parent = list(range(vertices))
    mst = []
    cost = 0

    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x

    for w, u, v in edges:
        root1 = find(u)
        root2 = find(v)

        if root1 != root2:
            mst.append((u, v, w))
            cost += w
            parent[root1] = root2

    print("Minimum Spanning Tree:")
    for u, v, w in mst:
        print(u, "-", v, ":", w)

    print("Minimum Cost:", cost)


edges = [
    (10, 0, 1),
    (6, 0, 2),
    (5, 0, 3),
    (15, 1, 3),
    (4, 2, 3)
]

kruskal(edges, 4)           
