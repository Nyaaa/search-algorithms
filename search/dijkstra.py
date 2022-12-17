from search.errors import PathNotFound, VertexNotFound


def search(graph: dict, start: str, stop: str) -> list:
    """Basic Dijkstra"""
    distances = {vertex: float('infinity') for vertex in graph}
    traversed = {vertex: False for vertex in graph}
    parents = {vertex: None for vertex in graph}
    distances[start] = 0
    pointer = stop
    path = []

    if start not in graph:
        raise VertexNotFound(start)
    elif stop not in graph:
        raise VertexNotFound(stop)

    for _ in range(len(distances)):
        shortest = min([k for k in traversed.keys() if not traversed[k]], key=lambda x: distances[x])

        for vertex in graph[shortest].keys():
            if distances[vertex] > distances[shortest] + graph[shortest][vertex]:
                distances[vertex] = distances[shortest] + graph[shortest][vertex]
                parents[vertex] = shortest
        traversed[shortest] = True

    while pointer is not None:
        path.append(pointer)
        pointer = parents[pointer]

    if distances[stop] == float('infinity'):
        raise PathNotFound(stop)

    # print(distances)
    path.reverse()
    return path
