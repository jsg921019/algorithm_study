
graph = [[float('inf') if i != j else 0 for i in range(N)] for j in range(N)]

for i, j, c in edges:
    graph[i-1][j-1] = min(graph[i-1][j-1], c)

def floyd(graph):
    N = len(graph)
    for p in range(N):
        for s in range(N):
            for e in range(N):
                graph[s][e] = min(graph[s][e], graph[s][p] + graph[p][e])

    return graph