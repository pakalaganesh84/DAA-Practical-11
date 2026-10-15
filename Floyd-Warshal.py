INF = float('inf')

graph = [
    [0,   5,   INF, 10],
    [INF, 0,   3,   INF],
    [INF, INF, 0,   1],
    [INF, INF, INF, 0]
]

n = len(graph)

for k in range(n):
    for i in range(n):
        for j in range(n):

            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

print("Shortest distance matrix:")

for row in graph:
    for distance in row:
        if distance == INF:
            print("INF", end="  ")
        else:
            print(distance, end="    ")
    print()
